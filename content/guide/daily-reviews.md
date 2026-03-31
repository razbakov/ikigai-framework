---
title: Daily Reviews & Scheduled Tasks
description: Set up the recurring rhythms that keep your projects on track — daily check-ins, weekly planning, and automated inbox processing.
---

The daily review is the heartbeat of your agent system. Without it, tasks pile up, inbox overflows, and you lose track of what matters. This guide sets up the recurring rhythms that keep everything moving.

## The Daily Review Workflow

A daily review has four phases:

### Morning (Data Gathering)
The agent collects everything that happened since the last review:
- Browser history (what sites you visited)
- AI session transcripts (what you worked on with Claude)
- New messages and notifications
- Calendar events for today
- Overdue tasks and approaching deadlines

### Planning
Based on the gathered data, the agent proposes a daily plan:
- Top 3 priorities for the day
- Blocked items that need your input
- Tasks ready for dispatch to other agents
- Meetings and time-boxed commitments

### Execution
Throughout the day, you work through the plan. Agents handle dispatched tasks in the background and report results.

### Evening Report
A summary of what was accomplished, what remains, and what to carry forward to tomorrow.

## Setting Up Scheduled Tasks

Claude Code supports scheduled tasks via remote triggers or the CronCreate tool within a session. Set up recurring tasks for your review cadence:

```bash
# Start a Claude Code session and use the /schedule skill
claude "/schedule daily-review --cron '0 6 * * *'"

# Or create a scheduled task via the API
claude "Create a scheduled task called daily-review
  that runs at 6 AM daily to gather all data sources
  and prepare the morning briefing."
```

## Weekly Review Cadence

The weekly review runs every Saturday and covers:

- **Progress against OKRs** — are you on track for quarterly goals?
- **Sprint retrospective** — what worked, what didn't?
- **Inbox cleanup** — any leftover items from the week?
- **Next week planning** — top priorities and commitments
- **Personal reflection** — how are you feeling about the work?

```bash
# Weekly review every Saturday at 10 AM — set up in a Claude Code session
claude "Create a scheduled task called weekly-review
  that runs every Saturday at 10 AM to evaluate progress
  against OKRs and plan next week."
```

## GTD Inbox Processing

Inbox processing follows the Getting Things Done methodology:

1. **Collect** — pull messages from all sources (email, Telegram, Slack)
2. **Clarify** — for each item: is it actionable? If yes, what's the next action?
3. **Organize** — route to the right project, agent, or reference file
4. **Reflect** — during reviews, check nothing fell through the cracks
5. **Engage** — work the prioritized list

The agent classifies each inbox item as:
- **Action** — becomes a task card with a clear next step
- **Reference** — saved for future lookup
- **Content Idea** — routed to your content pipeline
- **Someday/Maybe** — low priority, revisit during weekly review
- **Trash** — irrelevant, archive and move on

## Customizing to Your Needs

Every founder's rhythm is different. Adjust the defaults:

- **Morning person?** Move the review earlier
- **Multiple time zones?** Add timezone-aware scheduling
- **No Telegram?** Get reports in the terminal or via email
- **Different review frequency?** Some prefer twice-daily check-ins

The key is consistency. A simple review done every day beats an elaborate one done sporadically.

## Next Steps

Set up [S3 Governance](/guide/s3-governance) to define clear boundaries for what each agent can and cannot do autonomously.
