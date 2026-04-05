---
title: Getting Started
description: Install the setup skill, answer 10 questions, meet your team.
---

## Prerequisites

1. **Claude Code** — install via `npm install -g @anthropic-ai/claude-code`
2. **An Anthropic API key** — Claude Code prompts you on first run

## Setup (2 minutes)

```bash
# Install the setup skill
claude install-skill https://github.com/razbakov/ikigai-team/tree/main/skills/setup-ikigai

# Run the wizard
claude "/setup-ikigai"
```

The wizard asks ~10 questions: your name, projects, OKRs, and optional integrations (Telegram, Notion). Then it generates your full team.

## What Gets Generated

```
~/Orgs/your-org/
  CLAUDE.md                    # Rules, agent table, decision matrix
  .claude/agents/              # 6 agent definitions (source of truth)
    maya.md                    # Chief of Staff
    viktor.md                 # CTO
    luna.md                   # Content & Growth
    marco.md                  # Strategy & Business
    sage.md                   # Personal Coach
    kai.md                    # Community & Partnerships
  ops/sessions/                # Daily review logs
  ops/inbox/                   # Processed inbox items
  contacts/                    # CRM
  profile.md                   # Your personality and coaching prefs
  now.md                       # Current focus and health plan
```

## Start Using It

```bash
cd ~/Orgs/your-org
claude --agent maya
```

Talk to Maya. She dispatches to the right agent. Or go direct:

```bash
claude --agent viktor    # Engineering tasks
claude --agent luna      # Content creation
claude --agent marco     # Strategy questions
claude --agent sage      # Coaching check-in
claude --agent kai       # Contact processing
```

## Next Steps

- [Agents](/guide/agents) — how agent personas and domains work
- [Skills](/guide/skills) — installable workflows for each agent
- [Telegram Bots](/guide/telegram-bots) — message agents from your phone
- [S3 Governance](/guide/s3-governance) — how decisions and domains are structured
