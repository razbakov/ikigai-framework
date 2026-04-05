#!/bin/bash
# Start/stop Telegram agent bots in tmux.
#
# Usage:
#   .bin/telegram-bots.sh              # Start all bots in tmux
#   .bin/telegram-bots.sh --agent maya # Start only Maya's bot
#   .bin/telegram-bots.sh --kill       # Stop all bots
#   .bin/telegram-bots.sh --status     # Check if running

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
SESSION_NAME="agent-bots"
VENV="$HOME/.config/telegram/venv"

if [[ "${1:-}" == "--kill" ]]; then
  if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
    tmux kill-session -t "$SESSION_NAME"
    echo "Killed session: $SESSION_NAME"
  else
    echo "No session '$SESSION_NAME' running."
  fi
  exit 0
fi

if [[ "${1:-}" == "--status" ]]; then
  if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
    echo "Running: $SESSION_NAME"
    tmux capture-pane -t "$SESSION_NAME" -p | tail -5
  else
    echo "Not running."
  fi
  exit 0
fi

# Check if session already exists
if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
  echo "Session '$SESSION_NAME' already running."
  echo "  Attach:  tmux attach -t $SESSION_NAME"
  echo "  Kill:    $0 --kill"
  exit 0
fi

# Build command
AGENT_FLAG=""
if [[ "${1:-}" == "--agent" ]]; then
  AGENT_FLAG="--agent ${2:-maya}"
fi

# Start in tmux
tmux new-session -d -s "$SESSION_NAME" -c "$PROJECT_DIR" \
  "$VENV/bin/python3 $SCRIPT_DIR/telegram-bots.py $AGENT_FLAG"

echo "Agent bots started in tmux session: $SESSION_NAME"
echo "  Attach:  tmux attach -t $SESSION_NAME"
echo "  Logs:    tmux capture-pane -t $SESSION_NAME -p"
echo "  Kill:    $0 --kill"
