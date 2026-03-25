---
title: Sprint Planning
description: Plan upcoming sprints by reviewing the backlog, estimating stories, and creating balanced milestones.
category: engineering
agent: viktor
complexity: intermediate
---

# Sprint Planning

Sprint Planning transforms your unstructured backlog into a focused, time-boxed plan. The agent reviews open issues, estimates effort, groups work by theme, and creates a GitHub milestone with a balanced workload. The result is a clear list of what gets done this sprint and what waits.

This skill works best when your backlog has well-written issues with acceptance criteria. If issues are vague, the agent will flag them for clarification rather than estimating blindly.

## How It Works

1. **Review the backlog** — Scan all open issues across relevant repositories. Filter by labels, priorities, and dependencies to identify candidates for the sprint.
2. **Estimate effort** — Assign story points based on complexity, unknowns, and scope. Uses historical data from previous sprints if available to improve accuracy.
3. **Balance the sprint** — Select issues that fit within your available capacity. Mix high-impact features with necessary maintenance. Avoid overcommitting.
4. **Create the milestone** — Set up a GitHub milestone with the selected issues, target date, and sprint goals. Assign issues to team members or agents.
5. **Produce the sprint brief** — Generate a summary document with sprint goals, issue list, estimated velocity, and any risks or dependencies to watch.

## When to Use

- At the start of each sprint cycle (typically every 1-2 weeks)
- After a major milestone when you need to replan the next batch of work
- When the backlog has grown large and needs prioritization
- Before dispatching parallel agent sessions to ensure work is well-distributed

## Requirements

- **GitHub** — repository access with issues and milestones enabled
- A backlog of open issues with labels indicating priority and type
- Previous sprint data helps calibrate estimates (optional but valuable)
- Clear OKRs or goals to prioritize against
