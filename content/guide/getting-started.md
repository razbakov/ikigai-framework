---
title: Getting Started
description: Set up your AI Cabinet configuration and deploy your first agents.
---

# Getting Started

This guide walks you through setting up AI Cabinet in your project.

## Prerequisites

Before you begin, make sure you have:

- **Claude Code** installed and configured on your machine
- A project directory where you want to deploy your agents
- Basic familiarity with markdown files and project configuration

## Step 1: Generate Your Configuration

Visit the [onboarding wizard](/onboard) to create your configuration. You will:

1. Define your mission and vision
2. List your active projects
3. Select your pain points
4. Review agent recommendations
5. Customize agent roles and names
6. Pick skills for each agent
7. Download a ZIP file with everything configured

## Step 2: Extract the Files

Unzip the downloaded `ai-cabinet-config.zip` into your project root:

```bash
unzip ai-cabinet-config.zip -d /path/to/your/project
```

This creates:
- `CLAUDE.md` — Your main project configuration
- `initiatives/agent-team.md` — Agent team definitions
- `skills/` — Individual skill configurations for each agent

## Step 3: Start Using Your Agents

Open Claude Code in your project directory. Your agents are now available through the configuration in `CLAUDE.md`.

Try these commands:
- "Ask Maya to run the daily review"
- "Have Viktor review the latest PR"
- "Get Luna to draft a blog post about our launch"

## Step 4: Iterate

Your AI Cabinet configuration is a living document. As you work with your agents:

- Adjust agent roles based on what works
- Add or remove skills as your needs change
- Update your mission and vision as your goals evolve

## Next Steps

- [Understanding Agents](/guide/agents) — Learn how agents think and operate
- [Skills System](/guide/skills) — Deep dive into the skills framework
- [S3 Framework](/guide/s3-framework) — The decision-making framework behind your agents
