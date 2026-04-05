#!/usr/bin/env python3
"""
Send a Telegram message to Alex via an agent's bot.

Used by Claude Code sessions for proactive agent->Alex communication.

Usage:
  python3 telegram-send.py --agent maya "Your daily review is ready"
  python3 telegram-send.py --agent maya --file /tmp/reply.txt
  python3 telegram-send.py --agent maya --react 288064 🫡

Requires: OWNER_TELEGRAM_ID and <AGENT>_BOT_TOKEN in ~/.config/telegram/.env
"""
import asyncio
import os
import re
import sys
from pathlib import Path

ENV_FILE = Path.home() / ".config" / "telegram" / ".env"

# CUSTOMIZE: Update agent names and token env vars to match user's team
AGENT_TOKEN_MAP = {
    "maya": "MAYA_BOT_TOKEN",
    "viktor": "VIKTOR_BOT_TOKEN",
    "luna": "LUNA_BOT_TOKEN",
    "marco": "MARCO_BOT_TOKEN",
    "sage": "SAGE_BOT_TOKEN",
    "kai": "KAI_BOT_TOKEN",
}


def load_env(path):
    if path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def get_bot(agent: str):
    """Return (Bot, token) for an agent, or exit on error."""
    from telegram import Bot

    token_key = AGENT_TOKEN_MAP.get(agent.lower())
    if not token_key:
        print(f"Unknown agent: {agent}. Available: {', '.join(AGENT_TOKEN_MAP)}")
        sys.exit(1)

    token = os.environ.get(token_key)
    if not token:
        print(f"No token for {agent} ({token_key}). Check .env")
        sys.exit(1)

    return Bot(token=token)


def get_chat_id(override: int | None = None) -> int:
    """Return chat_id from --chat override or OWNER_TELEGRAM_ID."""
    if override:
        return override
    chat_id = int(os.environ.get("OWNER_TELEGRAM_ID", "0"))
    if chat_id == 0:
        print("OWNER_TELEGRAM_ID not set in .env")
        sys.exit(1)
    return chat_id


async def react_to_message(agent: str, chat_id: int, message_id: int, emoji: str):
    from telegram import ReactionTypeEmoji

    bot = get_bot(agent)
    await bot.set_message_reaction(
        chat_id=chat_id,
        message_id=message_id,
        reaction=[ReactionTypeEmoji(emoji)],
    )
    print(f"Reacted to msg {message_id} with {emoji}")


def strip_markdown_escapes(text: str) -> str:
    """Remove MarkdownV2 backslash escapes — we send plain text, no escaping needed."""
    return re.sub(r'\\([_*\[\]()~`>#+=|{}.!\-])', r'\1', text)


async def send_message(agent: str, chat_id: int, text: str):
    bot = get_bot(agent)
    text = strip_markdown_escapes(text)
    # Detect HTML tags and set parse_mode accordingly
    has_html = bool(re.search(r'<[a-z]+[ />]', text, re.IGNORECASE))
    parse_mode = "HTML" if has_html else None
    chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
    for chunk in chunks:
        try:
            await bot.send_message(chat_id=chat_id, text=chunk, parse_mode=parse_mode)
        except Exception:
            # Fallback to plain text if HTML parsing fails (malformed tags)
            await bot.send_message(chat_id=chat_id, text=chunk)
    print(f"Sent via {agent}: {text[:80]}...")


def main():
    load_env(ENV_FILE)

    if "--agent" not in sys.argv or len(sys.argv) < 4:
        print("Usage: telegram-send.py --agent <name> <message>")
        print(f"Agents: {', '.join(AGENT_TOKEN_MAP)}")
        sys.exit(1)

    idx = sys.argv.index("--agent")
    agent = sys.argv[idx + 1]

    # Parse --chat override (for group chats)
    chat_id_override = None
    if "--chat" in sys.argv:
        chat_idx = sys.argv.index("--chat")
        chat_id_override = int(sys.argv[chat_idx + 1])
    chat_id = get_chat_id(chat_id_override)

    # React mode: --react <message_id> <emoji>
    if "--react" in sys.argv:
        react_idx = sys.argv.index("--react")
        msg_id = int(sys.argv[react_idx + 1])
        emoji = sys.argv[react_idx + 2]
        asyncio.run(react_to_message(agent, chat_id, msg_id, emoji))
        return

    # Support --file flag for reading message from file (avoids shell quoting issues)
    if "--file" in sys.argv:
        file_idx = sys.argv.index("--file")
        file_path = sys.argv[file_idx + 1]
        message = Path(file_path).read_text().strip()
    else:
        # Collect remaining args, excluding known flags and their values
        skip = set()
        for flag in ("--agent", "--chat"):
            if flag in sys.argv:
                fi = sys.argv.index(flag)
                skip.add(fi)
                skip.add(fi + 1)
        remaining = [a for i, a in enumerate(sys.argv[1:], 1) if i not in skip]
        message = " ".join(remaining)

    if not message:
        print("No message provided")
        sys.exit(1)

    asyncio.run(send_message(agent, chat_id, message))


if __name__ == "__main__":
    main()
