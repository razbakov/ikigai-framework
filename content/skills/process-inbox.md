---
title: Process Inbox
description: Process messages and notifications through GTD methodology. Classify, route, and act on every item until the inbox is empty.
category: operations
agent: maya
complexity: beginner
---

# Process Inbox

This skill implements the Getting Things Done (GTD) inbox processing workflow. It takes all incoming messages and notifications, classifies each one, and routes them to the appropriate project, agent, or reference file. The goal is inbox zero — every item processed, nothing left ambiguous.

The GTD methodology ensures nothing falls through the cracks. Each item gets exactly one of five treatments: do it now (if under 2 minutes), delegate it, defer it, file it for reference, or trash it.

## How It Works

1. **Collect** — Pull unprocessed messages from all configured sources: Telegram saved messages, email, notifications, and any other input channels.
2. **Clarify** — For each item, answer: "Is this actionable?" If yes, determine the next physical action. If no, classify as reference, someday/maybe, or trash.
3. **Classify** — Tag each item with a GTD type:
   - **Action** — has a clear next step, becomes a task card
   - **Content Idea** — a thought worth developing into content
   - **Reference** — useful information to file for later
   - **Someday/Maybe** — interesting but not now
   - **Trash** — irrelevant, archive and move on
4. **Route** — Send actions to the task board with the right project and agent assignment. File references in the appropriate project docs. Queue content ideas for the content pipeline.
5. **React** — Mark processed items as handled in the source system so they don't get reprocessed.

## When to Use

- During every daily review (morning inbox sweep)
- Whenever the inbox count feels overwhelming
- After returning from vacation or time away
- As part of the weekly review to catch anything missed during the week

## Requirements

- **Telegram** — for processing saved messages (if using Telegram as an inbox)
- **Notion** — for creating task cards and routing items to the project board
- Configured data export scripts for each input source
- A clear project list so items can be routed correctly
