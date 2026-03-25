---
title: Installing Claude Code
description: Get Claude Code installed, authenticated, and understand the key concepts behind agent skills and configuration.
---

# Installing Claude Code

Claude Code is an AI coding assistant from Anthropic that runs in your terminal. It serves as the runtime for your AI agent team — each agent is a Claude Code session with specific instructions, skills, and personality.

## Installation

Install Claude Code globally using npm or Homebrew:

```bash
# Using npm
npm install -g @anthropic-ai/claude-code

# Using Homebrew
brew install claude-code
```

Verify the installation:

```bash
claude --version
```

## First Run & Authentication

Run Claude Code for the first time:

```bash
claude
```

You'll be prompted to authenticate with your Anthropic API key. Follow the on-screen instructions to complete setup. Your credentials are stored locally and never shared.

## Key Concepts

### CLAUDE.md — The Agent's Brain

Every project can have a `CLAUDE.md` file at its root. This file contains instructions that Claude Code reads at the start of every session. Think of it as the agent's personality, rules, and standard operating procedures.

You can also have a global `~/.claude/CLAUDE.md` that applies to all projects.

### Skills — Reusable Capabilities

Skills are markdown files (usually named `SKILL.md`) that define a repeatable process. They include trigger conditions, step-by-step instructions, templates, and integration points. Skills make your agents consistent and reliable.

### Hooks — Automated Triggers

Hooks let you run scripts before or after certain Claude Code events. Useful for preprocessing inputs or post-processing outputs.

### MCP Servers — External Integrations

Model Context Protocol (MCP) servers connect Claude Code to external tools like Notion, GitHub, Google Calendar, and browsers. They extend what your agents can do beyond the terminal.

## Recommended Setup

1. **Create a project directory** for your agent configuration
2. **Add a `CLAUDE.md`** with your personal rules and preferences
3. **Install MCP servers** for the tools you use (Notion, GitHub, etc.)
4. **Test with a simple task** like "summarize this file"

## Next Steps

Once Claude Code is running, head to [Setting Up Your First Agent](/guide/first-agent) to create Maya, your Chief of Staff.

## Resources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)
- [Anthropic API Console](https://console.anthropic.com/)
