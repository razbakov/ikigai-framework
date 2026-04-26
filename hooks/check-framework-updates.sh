#!/usr/bin/env bash
# Layer A — passive framework-updates notification.
#
# Fires on SessionStart. For each repo we manage on the user's behalf
# (the Ikigai framework + their personal skills library) we silently
# fetch new commits and, if there are any, emit a SHORT non-technical
# nudge into the session context.
#
# Hard rules:
#   - Never modify files (no `git pull`, no checkout).
#   - Never produce noise when nothing changed (silent success).
#   - Never use jargon: no "commits", "git", "HEAD", "origin", hashes.
#   - Soft-fail: missing repo, no network, detached HEAD → exit 0 quietly.
#
# Output format: a single JSON object on stdout consumed by Claude Code
# as a SessionStart hook (hookSpecificOutput.additionalContext).
#
# Throttle: at most once every 6 hours per repo, tracked via mtime on a
# stamp file under ~/.cache/ikigai-team/. This prevents spamming when a
# user opens many sessions in a row.

set -uo pipefail

CACHE_DIR="${IKIGAI_HOOK_CACHE_DIR:-${HOME}/.cache/ikigai-team}"
mkdir -p "$CACHE_DIR" 2>/dev/null || exit 0

THROTTLE_SECONDS="${IKIGAI_HOOK_THROTTLE_SECONDS:-$((6 * 60 * 60))}"

# Repos to watch. Format: "label|path".
# Override via IKIGAI_HOOK_REPOS env var (newline-separated entries) for tests.
if [[ -n "${IKIGAI_HOOK_REPOS:-}" ]]; then
  IFS=$'\n' read -r -d '' -a REPOS < <(printf '%s\0' "$IKIGAI_HOOK_REPOS")
else
  REPOS=(
    "Ikigai system|${HOME}/Projects/ikigai-team"
    "Skills library|${HOME}/.local/share/skill-mix/sources/skills@razbakov"
  )
fi

# Translate a commit subject into something a non-technical reader can parse.
# Strip conventional-commit prefixes and trailing tags; keep it short.
humanize() {
  local subject="$1"
  # Drop conventional-commit prefix (feat:, fix:, chore:, docs:, refactor:, etc.)
  subject="$(printf '%s' "$subject" | sed -E 's/^(feat|fix|chore|docs|refactor|perf|test|build|ci|style|revert)(\([^)]+\))?!?:[[:space:]]*//I')"
  # Drop trailing PR refs like (#123)
  subject="$(printf '%s' "$subject" | sed -E 's/[[:space:]]*\(#[0-9]+\)[[:space:]]*$//')"
  # Lowercase the first letter for natural prose flow
  if [[ -n "$subject" ]]; then
    local first="${subject:0:1}"
    subject="$(printf '%s' "$first" | tr '[:upper:]' '[:lower:]')${subject:1}"
  fi
  printf '%s' "$subject"
}

check_repo() {
  local label="$1"
  local repo="$2"

  [[ -d "$repo/.git" ]] || return 1

  # Throttle per-repo
  local stamp_name
  stamp_name="$(printf '%s' "$repo" | tr '/' '_')"
  local stamp="${CACHE_DIR}/${stamp_name}.lastcheck"
  if [[ -f "$stamp" ]]; then
    local now last age
    now=$(date +%s)
    last=$(stat -f %m "$stamp" 2>/dev/null || stat -c %Y "$stamp" 2>/dev/null || echo 0)
    age=$((now - last))
    if (( age < THROTTLE_SECONDS )); then
      return 1
    fi
  fi
  touch "$stamp" 2>/dev/null

  # Determine the upstream branch (usually origin/main). Bail if no upstream.
  local upstream
  upstream=$(git -C "$repo" rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null) || return 1
  [[ -n "$upstream" ]] || return 1

  # Fetch quietly. Cap at 5s so a slow network never blocks session start.
  # Use background-with-timeout pattern since `timeout` isn't ubiquitous on macOS.
  (
    git -C "$repo" fetch --quiet --no-tags 2>/dev/null
  ) &
  local fetch_pid=$!
  local waited=0
  while kill -0 "$fetch_pid" 2>/dev/null; do
    sleep 1
    waited=$((waited + 1))
    if (( waited >= 5 )); then
      kill "$fetch_pid" 2>/dev/null
      wait "$fetch_pid" 2>/dev/null
      return 1
    fi
  done
  wait "$fetch_pid" 2>/dev/null

  # How many new commits behind upstream?
  local behind
  behind=$(git -C "$repo" rev-list --count "HEAD..${upstream}" 2>/dev/null) || return 1
  [[ "$behind" =~ ^[0-9]+$ ]] || return 1
  (( behind > 0 )) || return 1

  # Pull up to 3 most recent commit subjects, humanize each.
  local raw_subjects
  raw_subjects=$(git -C "$repo" log --pretty=format:'%s' -n 3 "HEAD..${upstream}" 2>/dev/null) || return 1

  local highlights=""
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    local nice
    nice="$(humanize "$line")"
    [[ -n "$nice" ]] || continue
    highlights+="  - ${nice}"$'\n'
  done <<< "$raw_subjects"

  # Compose the friendly block.
  local plural="improvement"
  (( behind > 1 )) && plural="improvements"

  printf '**%s — %d new %s available**\n' "$label" "$behind" "$plural"
  if [[ -n "$highlights" ]]; then
    printf "What's new:\n%s" "$highlights"
  fi
  printf "\n"

  return 0
}

# Collect all friendly messages.
NOTICE=""
for entry in "${REPOS[@]}"; do
  label="${entry%%|*}"
  path="${entry##*|}"
  block="$(check_repo "$label" "$path" 2>/dev/null)" || continue
  [[ -n "$block" ]] || continue
  NOTICE+="${block}"$'\n'
done

if [[ -z "$NOTICE" ]]; then
  exit 0
fi

# Wrap with a single human-friendly call to action so Claude knows how to relay it.
FINAL=$'Heads up — your Ikigai setup has fresh updates waiting:\n\n'
FINAL+="$NOTICE"
FINAL+=$'\nWhen you have a moment, just say **"update my system"** and I\'ll pull these in for you. Nothing is required right now.'

# Emit as SessionStart additionalContext (JSON).
# Use python3 if available for safe JSON encoding; otherwise fall back to plain text.
if command -v python3 >/dev/null 2>&1; then
  python3 -c '
import json, sys
ctx = sys.argv[1]
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": ctx,
    }
}))
' "$FINAL"
else
  printf '%s\n' "$FINAL"
fi
