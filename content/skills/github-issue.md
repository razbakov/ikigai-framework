---
title: Implement GitHub Issue
description: Take a GitHub issue and implement it end-to-end — from reading the spec to opening a pull request.
category: engineering
agent: viktor
complexity: intermediate
---

# Implement GitHub Issue

This skill takes a GitHub issue number and handles the full development cycle: read the spec, create a feature branch, write the code, run tests, and open a pull request. It is the core engineering workflow that turns backlog items into shipped code.

The agent reads the issue carefully, plans the implementation, works in an isolated git worktree, follows your project's coding conventions, and produces a clean PR with a descriptive summary. It handles edge cases, writes tests, and runs CI checks before requesting review.

## How It Works

1. **Read the issue** — Parse the GitHub issue for requirements, acceptance criteria, and any linked context (related issues, design docs, screenshots).
2. **Plan the approach** — Identify which files need changes, estimate scope, and decide on the implementation strategy. For non-trivial work, write a brief plan before coding.
3. **Create a branch** — Set up an isolated git worktree with a descriptively named branch. This keeps your main branch clean.
4. **Implement and test** — Write the code following project conventions. Add or update tests to cover the changes. Run the full test suite.
5. **Open a PR** — Create a pull request that references the issue, describes the changes, and includes a test plan. Request review and update the issue status.

## When to Use

- When you have a well-specified GitHub issue ready for implementation
- For bug fixes with clear reproduction steps
- For feature work where the requirements are defined in the issue
- When you want to parallelize development — dispatch multiple issues to separate agent sessions

## Requirements

- **GitHub** — repository access with permission to create branches and PRs
- A well-written issue with clear acceptance criteria (garbage in, garbage out)
- Project must have a working test suite (the agent runs tests to verify its work)
- `CLAUDE.md` in the repo with project-specific coding conventions
