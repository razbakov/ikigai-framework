# Ikigai Team — Framework Root

This file is the entry point of the Ikigai Team operating system: a wiki of governance rules, agent personas, and operating patterns that any human + AI commander can adopt.

It's designed to be **imported**, not copied. Your private brain repo (or any org/project repo) declares a single import line referencing this file's absolute path (e.g. `@` followed by `/Users/you/Projects/ikigai-team/CLAUDE.md`) and inherits the full framework. Updates land via `git pull` in this repo. There is no installer, no template renderer, no migration tool — just markdown referenced from markdown.

See https://github.com/razbakov/ikigai-team#getting-started for the exact import syntax for your environment.

---

## How to use this framework

You'll typically have three kinds of repo on disk:

1. **Brain / control center** (e.g. `~/Brain/` or `~/Orgs/<your-name>/`) — private. Holds your contacts, OKRs, daily reviews, project routing. Imports this framework and adds your private config.
2. **Org logbooks** (`~/Orgs/<OrgName>/`) — one per organisation you run. Governance, partnerships, contacts. Imports this framework + adds org-specific governance.
3. **Code projects** (`~/Projects/<project-name>/`) — actual code. Imports this framework + adds project tech stack rules.

Whichever door you enter through, you get the same restaurant: the same agent team, the same daily-review cadence, the same task discipline, the same Telegram protocols. That uniformity is the point.

---

## Framework rules (imported)

@rules/agent-team.md
@rules/agent-operations.md
@rules/agent-protocols.md
@rules/agent-proactivity.md
@rules/tasks-control-center.md
@rules/daily-review.md
@rules/telegram.md
@rules/content-publishing.md
@rules/contacts.md
@rules/skills.md
@rules/orgs-projects.md
@rules/shortcuts.md
@rules/general.md

---

## What this framework does NOT include

- **Your identity.** Names, OKRs, contact lists, project paths, API keys — all live in your private repo.
- **Your bot tokens.** Telegram bot handles and `*_BOT_TOKEN` env vars are per-instance. The framework ships only the *runner* code (`.bin/telegram-bots.py`) — you supply the tokens.
- **Your agent OKRs.** Agent personas in `.claude/agents/` describe role and personality only. Quarterly OKR ownership belongs in your private repo.
- **Anything time-bound.** "Q2 2026 priorities", current campaigns, this-week focus — all instance-side. The framework is timeless.

If you find personal data leaking into a framework rule, that's a bug — open an issue at https://github.com/razbakov/ikigai-team/issues.
