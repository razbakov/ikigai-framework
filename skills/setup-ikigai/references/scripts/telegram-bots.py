#!/usr/bin/env python3
"""
Telegram Bot Runner for Agent Team.

Runs 6 Telegram bots (Maya, Viktor, Luna, Marco, Sage, Kai) in a single process.
Each bot receives messages from Alex, processes them through Claude Code with the
agent's persona and full tool access, and sends the response back.

Usage:
  # Activate venv first:
  source ~/.config/telegram/venv/bin/activate

  python3 telegram-bots.py              # Run all bots with tokens in .env
  python3 telegram-bots.py --dry-run    # Print config without starting bots
  python3 telegram-bots.py --agent maya # Run only Maya's bot

Tokens stored in ~/.config/telegram/.env:
  MAYA_BOT_TOKEN=...
  VIKTOR_BOT_TOKEN=...
  etc.
  OWNER_TELEGRAM_ID=...
"""
import asyncio
import json
import logging
import os
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from telegram import ReactionTypeEmoji, Update
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ENV_FILE = Path.home() / ".config" / "telegram" / ".env"
# CUSTOMIZE: Set to the user's org path
PROJECT_DIR = Path.home() / "Orgs" / "ikigai"
load_dotenv(ENV_FILE)

# Ensure Homebrew binaries (tmux, claude) are in PATH for all subprocess calls
for p in ("/opt/homebrew/bin", str(Path.home() / ".local" / "bin")):
    if p not in os.environ.get("PATH", ""):
        os.environ["PATH"] = f"{p}:{os.environ.get('PATH', '')}"

# CUSTOMIZE: Env var name for the owner's Telegram user ID
OWNER_TELEGRAM_ID = int(os.environ.get("OWNER_TELEGRAM_ID", "0"))

logging.basicConfig(
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("agent-bots")

# ---------------------------------------------------------------------------
# Agent definitions
# ---------------------------------------------------------------------------

# CUSTOMIZE: Update agent names, token env vars, roles, and greetings
AGENTS = {
    "maya": {
        "token_env": "MAYA_BOT_TOKEN",
        "name": "Maya",
        "role": "Chief of Staff",
        "greeting": "Maya here. What do you need?",
    },
    "viktor": {
        "token_env": "VIKTOR_BOT_TOKEN",
        "name": "Viktor",
        "role": "CTO",
        "greeting": "Viktor here. What needs building?",
    },
    "luna": {
        "token_env": "LUNA_BOT_TOKEN",
        "name": "Luna",
        "role": "Head of Content & Growth",
        "greeting": "Luna here! What story are we telling today?",
    },
    "marco": {
        "token_env": "MARCO_BOT_TOKEN",
        "name": "Marco",
        "role": "Head of Strategy & Business",
        "greeting": "Marco here. Let's talk strategy.",
    },
    "sage": {
        "token_env": "SAGE_BOT_TOKEN",
        "name": "Sage",
        "role": "Personal Coach",
        "greeting": "Hey Alex. How are you, really?",
    },
    "kai": {
        "token_env": "KAI_BOT_TOKEN",
        "name": "Kai",
        "role": "Community & Partnerships",
        "greeting": "Kai here! Who are we connecting with?",
    },
}

# ---------------------------------------------------------------------------
# Persistent tmux sessions per agent
# ---------------------------------------------------------------------------

ANSI = re.compile(r'\x1b(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
TMUX_SESSION = "agent-bots"


def build_telegram_instructions(key: str) -> str:
    """Build Telegram reply protocol instructions (appended to agent's base prompt).

    The agent's persona and domain prompt now lives in .claude/agents/<key>.md.
    This function only provides the Telegram transport layer instructions.
    """
    # CUSTOMIZE: Update path to match the user's org path
    send_base = f"~/.config/telegram/venv/bin/python3 {PROJECT_DIR}/.bin/telegram-send.py --agent {key}"
    return f"""IMPORTANT — Telegram Reply Instructions:
You are running inside a Telegram bot. When you want to reply, you MUST use the Bash tool. Printing text to stdout does NOT reach the user.

Messages you receive start with [chat_id:NUMBER,msg_id:NUMBER]. Use those IDs for reactions and replies.
Always include --chat <chat_id> so your reply goes to the same chat (DM or group).

Step 1 — React to show your intent:
{send_base} --chat <chat_id> --react <msg_id> 🫡    # You will take action (run tasks, create files, dispatch agents, etc.)
{send_base} --chat <chat_id> --react <msg_id> 👌    # Conversational reply only, no action needed

Step 2 — Send your reply:
{send_base} --chat <chat_id> "Your reply here"

For longer replies, write to a file first:
cat > /tmp/agent-{key}-reply.txt << 'REPLY'
Your multi-line reply here.
REPLY
{send_base} --chat <chat_id> --file /tmp/agent-{key}-reply.txt

Rules:
- ALWAYS include --chat <chat_id> from the message tag. This ensures replies go to the right chat.
- ALWAYS react first, then reply. This tells Alex what to expect.
- ALWAYS reply via this command. Text you print to stdout does NOT reach Alex.
- Use plain text only. No markdown headers, no bullet markers, no code fences.
- Do not sign messages with your name — your bot identity is already visible in Telegram.
- If a task will take time, react with 🫡 immediately, then send updates as you go."""


SESSION_TTL_SECONDS = 4 * 3600  # Auto-restart sessions every 4 hours
RESPONSE_TIMEOUT_SECONDS = 120  # Restart if agent doesn't respond within 2 min


class AgentSession:
    """Persistent Claude interactive session running in a dedicated tmux window.

    Each agent lives in its own window inside the agent-bots tmux session.
    Messages are pasted in via load-buffer/paste-buffer to handle special chars.
    Agent replies directly via telegram-send.py (fire-and-forget).

    Self-healing features:
    - TTL: auto-restart every SESSION_TTL_SECONDS to prevent context bloat
    - Watchdog: if agent doesn't respond within RESPONSE_TIMEOUT_SECONDS,
      restart and re-send the message
    """

    def __init__(self, key: str):
        self.key = key
        self.agent = AGENTS[key]
        self.window = f"agent-{key}"
        self.target = f"{TMUX_SESSION}:{self.window}"
        self._lock = asyncio.Lock()
        self._started = False
        self._started_at: float = 0.0  # timestamp of last start/restart
        self._watchdog_task: asyncio.Task | None = None

    def _run(self, *cmd) -> subprocess.CompletedProcess:
        return subprocess.run(cmd, capture_output=True, text=True)

    def _pane(self) -> str:
        """Capture pane content (last 3000 lines), strip ANSI escape codes."""
        r = self._run("tmux", "capture-pane", "-t", self.target, "-p", "-S", "-3000")
        return ANSI.sub("", r.stdout)

    def _ready(self) -> bool:
        """Return True when Claude's ❯ idle prompt is visible."""
        # Check last 30 lines — the prompt may be followed by empty lines
        # from the tmux status bar area
        for line in reversed(self._pane().splitlines()[-30:]):
            # Strip regular whitespace and non-breaking spaces (\xa0)
            s = line.strip().strip("\xa0")
            if s == "❯" or s.startswith("❯ ") or s.startswith("❯\xa0"):
                return True
        return False

    def _window_exists(self) -> bool:
        r = self._run("tmux", "list-windows", "-t", TMUX_SESSION, "-F", "#{window_name}")
        return self.window in r.stdout.splitlines()

    def _session_age(self) -> float:
        """Return seconds since last start/restart."""
        if self._started_at == 0:
            return 0
        return time.time() - self._started_at

    def _needs_ttl_restart(self) -> bool:
        """Return True if session has exceeded its TTL."""
        return self._started_at > 0 and self._session_age() > SESSION_TTL_SECONDS

    def start(self) -> None:
        """Create tmux window and launch Claude interactive session."""
        if self._window_exists():
            log.info(f"[{self.key}] Window {self.window} already exists, reusing")
            self._started = True
            if self._started_at == 0:
                self._started_at = time.time()
            return

        claude_cmd = (
            f"claude --dangerously-skip-permissions "
            f"--agent {self.key} "
            f"--append-system-prompt {shlex.quote(build_telegram_instructions(self.key))}"
        )
        subprocess.run([
            "tmux", "new-window",
            "-t", TMUX_SESSION,
            "-n", self.window,
            "-c", str(PROJECT_DIR),
            claude_cmd,
        ])
        self._started = True
        self._started_at = time.time()
        log.info(f"[{self.key}] Launched in window {self.window} (initializing in background)")

    def stop(self) -> None:
        """Kill the tmux window."""
        if self._window_exists():
            self._run("tmux", "kill-window", "-t", self.target)
        self._started = False

    def restart(self) -> None:
        """Kill and recreate the window, clearing conversation history."""
        age = self._session_age()
        log.info(f"[{self.key}] Restarting (session age: {age/3600:.1f}h)")
        self.stop()
        self.start()

    async def _watchdog(self, message: str) -> None:
        """Monitor agent response after sending a message.

        If the agent hasn't started responding (pane unchanged) within
        RESPONSE_TIMEOUT_SECONDS, restart and re-send the message.
        """
        try:
            await asyncio.sleep(RESPONSE_TIMEOUT_SECONDS)
            # Check if agent is still showing the idle prompt with our message
            # (meaning it never started processing)
            if self._ready():
                log.warning(
                    f"[{self.key}] Agent unresponsive after {RESPONSE_TIMEOUT_SECONDS}s — "
                    f"restarting and re-sending message"
                )
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, self.restart)
                # Wait for fresh session to be ready
                for _ in range(60):
                    await asyncio.sleep(1)
                    if self._ready():
                        break
                # Re-send the message
                tmp = Path(f"/tmp/agent-{self.key}-msg.txt")
                tmp.write_text(message + "\n")
                self._run("tmux", "load-buffer", "-b", f"agent-{self.key}", str(tmp))
                self._run("tmux", "paste-buffer", "-b", f"agent-{self.key}", "-t", self.target)
                log.info(f"[{self.key}] Re-sent message after watchdog restart")
        except asyncio.CancelledError:
            pass  # Normal — agent responded in time, watchdog cancelled

    async def send(self, message: str) -> None:
        """Send a message to the Claude session (fire-and-forget).

        Claude replies directly via telegram-send.py, not via pane capture.
        Includes TTL check and watchdog for self-healing.
        """
        async with self._lock:
            if not self._started:
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, self.start)

            # TTL check — restart stale sessions before sending
            if self._needs_ttl_restart():
                age_h = self._session_age() / 3600
                log.info(f"[{self.key}] Session TTL exceeded ({age_h:.1f}h) — auto-restarting")
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, self.restart)
                # After restart, give the new session time to start before checking _ready()
                # Without this sleep, _ready() can pass on stale pane buffer from the old window
                await asyncio.sleep(5)

            # Wait for Claude to be ready (first message may arrive before init completes)
            # Agent startup loads .claude/agents/<name>.md + CLAUDE.md + MCP servers — can take 90-120s
            if not self._ready():
                log.info(f"[{self.key}] Waiting for Claude to initialize...")
                for _ in range(120):
                    await asyncio.sleep(1)
                    if self._ready():
                        break
                else:
                    log.warning(f"[{self.key}] Claude not ready after 120s — restarting")
                    loop = asyncio.get_event_loop()
                    await loop.run_in_executor(None, self.restart)
                    for _ in range(120):
                        await asyncio.sleep(1)
                        if self._ready():
                            break
                    else:
                        log.error(f"[{self.key}] Claude still not ready after restart — sending anyway")

            # Cancel any previous watchdog
            if self._watchdog_task and not self._watchdog_task.done():
                self._watchdog_task.cancel()

            # Send message via temp file + paste-buffer (handles special chars)
            tmp = Path(f"/tmp/agent-{self.key}-msg.txt")
            tmp.write_text(message + "\n")
            self._run("tmux", "load-buffer", "-b", f"agent-{self.key}", str(tmp))
            self._run("tmux", "paste-buffer", "-b", f"agent-{self.key}", "-t", self.target)
            log.info(f"[{self.key}] Sent message ({len(message)} chars), fire-and-forget")

            # Start watchdog to detect unresponsive agents
            self._watchdog_task = asyncio.create_task(self._watchdog(message))


# Global sessions map, populated in main()
SESSIONS: dict = {}


# ---------------------------------------------------------------------------
# Telegram handlers
# ---------------------------------------------------------------------------

def make_handlers(agent_key: str):
    """Create Telegram handlers for a specific agent bot."""
    agent = AGENTS[agent_key]

    async def start(update: Update, context):
        if update.effective_user.id != OWNER_TELEGRAM_ID:
            await update.message.reply_text("This bot is private.")
            return
        await update.message.reply_text(agent["greeting"])

    async def handle_message(update: Update, context):
        if update.effective_user.id != OWNER_TELEGRAM_ID:
            await update.message.reply_text("This bot is private.")
            return

        text = update.message.text or update.message.caption or ""
        if not text:
            await update.message.reply_text(f"I can only process text messages for now.")
            return

        if agent_key not in SESSIONS:
            await update.message.reply_text("Bot not fully initialized yet. Try again in a moment.")
            return

        # Acknowledge receipt with 👀, then fire-and-forget to Claude
        # Claude will change reaction to 🫡 (action) or 👌 (reply only)
        await update.message.set_reaction(ReactionTypeEmoji("👀"))
        # Include chat_id and message_id so Claude replies to the right chat
        chat_id = update.message.chat_id
        msg_id = update.message.message_id

        # Extract quoted/replied-to message if present
        quoted = ""
        reply = update.message.reply_to_message
        if reply:
            reply_text = reply.text or reply.caption or ""
            reply_from = ""
            if reply.from_user:
                reply_from = reply.from_user.first_name or reply.from_user.username or ""
            if reply_text:
                quoted = f"\n[quoted message from {reply_from}]: {reply_text}\n"

        tagged_text = f"[chat_id:{chat_id},msg_id:{msg_id}] {text}{quoted}"
        await SESSIONS[agent_key].send(tagged_text)

    async def reset(update: Update, context):
        """Reset conversation context by restarting the tmux window."""
        if update.effective_user.id != OWNER_TELEGRAM_ID:
            return
        if agent_key not in SESSIONS:
            return
        await update.message.reply_text(f"Restarting {agent['name']}...")
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, SESSIONS[agent_key].restart)
        await update.message.reply_text(f"{agent['name']}: Context reset. Fresh conversation started.")

    return start, handle_message, reset


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def run_bot(agent_key: str):
    """Build and register handlers for a single agent bot."""
    agent = AGENTS[agent_key]
    token = os.environ.get(agent["token_env"])

    app = Application.builder().token(token).build()
    start, handle_message, reset = make_handlers(agent_key)

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    log.info(f"[{agent_key}] Bot started: {agent['name']} ({agent['role']})")
    return app


async def main():
    # Parse args
    only_agent = None
    if "--agent" in sys.argv:
        idx = sys.argv.index("--agent") + 1
        only_agent = sys.argv[idx].lower()

    if "--dry-run" in sys.argv:
        print("Agent Bot Configuration:")
        print(f"  OWNER_TELEGRAM_ID: {OWNER_TELEGRAM_ID}")
        print(f"  PROJECT_DIR: {PROJECT_DIR}")
        print(f"  TMUX_SESSION: {TMUX_SESSION}")
        for key, agent in AGENTS.items():
            if only_agent and key != only_agent:
                continue
            token = os.environ.get(agent["token_env"], "")
            has_token = "SET" if token else "MISSING"
            window = f"agent-{key}"
            print(f"  {agent['name']:8s} [{agent['role']:30s}] token={has_token}  window={window}")
        return

    if OWNER_TELEGRAM_ID == 0:
        log.error("OWNER_TELEGRAM_ID not set in .env — bots won't respond to anyone")
        sys.exit(1)

    # Ensure the agent-bots tmux session exists
    r = subprocess.run(["tmux", "has-session", "-t", TMUX_SESSION], capture_output=True)
    if r.returncode != 0:
        subprocess.run(["tmux", "new-session", "-d", "-s", TMUX_SESSION, "-c", str(PROJECT_DIR)])
        log.info(f"Created tmux session: {TMUX_SESSION}")
    else:
        log.info(f"Tmux session {TMUX_SESSION} already exists")

    # Start persistent Claude sessions and Telegram bots
    agents_to_run = [only_agent] if only_agent else list(AGENTS.keys())
    apps = []
    for key in agents_to_run:
        token = os.environ.get(AGENTS[key]["token_env"])
        if not token:
            log.warning(f"[{key}] No token found ({AGENTS[key]['token_env']}), skipping")
            continue
        session = AgentSession(key)
        session.start()
        SESSIONS[key] = session
        app = await run_bot(key)
        if app:
            apps.append(app)

    if not apps:
        log.error("No bots started — check your .env tokens")
        sys.exit(1)

    log.info(f"Starting {len(apps)} bot(s) with persistent tmux sessions...")

    # Initialize and start all bots
    for app in apps:
        await app.initialize()
        await app.start()
        await app.updater.start_polling(drop_pending_updates=True)

    log.info("All bots running. Press Ctrl+C to stop.")

    # Keep running
    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, SystemExit):
        log.info("Shutting down...")
    finally:
        for app in apps:
            await app.updater.stop()
            await app.stop()
            await app.shutdown()


if __name__ == "__main__":
    # python-dotenv might not be in venv — handle gracefully
    try:
        from dotenv import load_dotenv
    except ImportError:
        # Manual .env loading
        def load_dotenv(path):
            if path.exists():
                for line in path.read_text().splitlines():
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ.setdefault(k.strip(), v.strip())
        load_dotenv(ENV_FILE)

    asyncio.run(main())
