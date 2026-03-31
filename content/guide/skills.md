---
title: Skills System
description: Discover how skills work — reusable workflows your agents can execute on demand.
---

Skills are the building blocks of what your agents can do. Each skill is a documented, repeatable workflow with clear triggers, inputs, processes, and outputs.

## Anatomy of a Skill

Every skill file (`SKILL.md`) contains:

### Trigger
How the skill gets activated — manually via a slash command (`/daily-review`), on a schedule, or through another agent's handoff.

### Process
A step-by-step procedure the agent follows:
1. Gather context
2. Analyze requirements and constraints
3. Execute the core task
4. Verify quality
5. Report results

### Inputs and Outputs
What the skill needs to start and what it produces when done.

### Quality Checklist
A verification checklist to ensure the output meets standards.

## Skill Categories

Skills are organized into six categories, one per agent domain:

| Category | Agent | Example Skills |
|----------|-------|---------------|
| Operations | Maya | Daily Review, Inbox Processing, Weekly Review |
| Engineering | Viktor | Code Review, Deploy, Tech Debt Audit |
| Content | Luna | Blog Post, Social Media, SEO Audit |
| Strategy | Marco | OKR Review, Market Research, Pricing |
| Personal | Sage | Check-in, Journal Prompt, Energy Audit |
| Community | Kai | Contact Enrichment, Follow-up, Event Planning |

## Skill Complexity

Each skill has a complexity rating:

- **Simple** — Can be completed in a few minutes with minimal context
- **Moderate** — Requires gathering context and making judgment calls
- **Advanced** — Multi-step process that may span multiple sessions

## Creating Custom Skills

You can create your own skills by adding a `SKILL.md` file to the `.claude/skills/<skill-slug>/` directory. Follow the template structure and include all sections (trigger, process, inputs, outputs, quality checklist).

Browse the [Skills Catalog](/skills) to see all available skills.
