---
title: Setting Up Your First Agent
description: Create Maya (Chief of Staff) as your foundation agent. She handles the daily rhythm that everything else builds on.
---

# Setting Up Your First Agent

Start with Maya — the Chief of Staff. She's the foundation agent because every other agent depends on operational rhythm. Without daily reviews, inbox processing, and task dispatch, nothing else works reliably.

## Why Maya First

Maya handles the "glue work" of your solo founder life:

- **Daily reviews** that show you what happened and what's next
- **Inbox processing** that triages messages into actionable tasks
- **Task dispatch** that launches other agents when work is approved
- **OKR tracking** that keeps strategic goals visible

Everything else — engineering, content, strategy — only works if there's a system feeding tasks in and reviewing outputs.

## Creating the CLAUDE.md

Create a `CLAUDE.md` file in your project root with Maya's persona:

```markdown
## Agent: Maya — Chief of Staff

**Personality:** ISTJ — methodical, reliable, detail-oriented.
**Tone:** Calm, organized, concise. Reports facts, not opinions.

### Responsibilities
- Run daily check-ins and weekly reviews
- Process inbox through GTD methodology
- Manage calendar and scheduling
- Track OKR progress
- Coordinate other agents

### Constraints
- Does NOT make strategic decisions
- Does NOT create content
- Does NOT write code
- Cannot cancel external meetings without approval
```

## Setting Up the Agent Team File

Create an `agent-team.md` that defines your full cabinet. Even though you're starting with Maya, the file maps out the entire team so agents know who handles what:

```markdown
# Agent Team

| Agent | Role | Domain |
|-------|------|--------|
| Maya | Chief of Staff | Operations, coordination |
| Viktor | CTO | Engineering, architecture |
| Luna | Content & Growth | Content, SEO, social |
| Marco | Strategy & Business | OKRs, prioritization |
| Sage | Personal Coach | Wellbeing, reflection |
| Kai | Community & Partnerships | Events, networking |
```

## Running Your First Daily Review

Test Maya with a daily review:

```bash
claude "Run a daily review for today. Check my calendar,
summarize what happened, and propose a plan for tomorrow."
```

Maya should gather available data, organize it, and present a structured review.

## Tips for Agent Personas

- **Be specific about constraints.** What the agent cannot do is more important than what it can.
- **Define the tone.** "Concise and factual" produces very different output than "warm and encouraging."
- **Use MBTI as a shorthand.** It gives the AI a personality anchor without lengthy descriptions.
- **Test with real tasks.** Run the agent on actual work, not hypotheticals. Adjust the persona based on results.

## Next Steps

Once Maya is running daily reviews, you can optionally [set up Telegram bots](/guide/telegram-bots) for mobile access, or jump to [Daily Reviews & Scheduled Tasks](/guide/daily-reviews) to automate the cadence.
