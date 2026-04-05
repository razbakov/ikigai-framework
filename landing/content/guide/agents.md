---
title: Understanding Agents
description: Learn how AI agents work, their roles, personalities, and decision-making framework.
---

Ikigai Team agents are specialized AI personas, each with a defined domain of expertise, personality type, and set of responsibilities.

## What Makes an Agent?

Each agent has five defining attributes:

### 1. Role and Domain

Every agent owns a specific domain. Maya handles operations, Viktor handles engineering, Luna handles content, Marco handles strategy, Sage handles personal development, and Kai handles community. This division ensures clear ownership and avoids confusion about who handles what.

### 2. Personality (MBTI Type)

Each agent has a personality type that influences how they communicate and approach problems:

- **Maya (ISTJ)** — Methodical, reliable, detail-oriented
- **Viktor (INTJ)** — Strategic, analytical, systems-thinking
- **Luna (ENFP)** — Creative, enthusiastic, idea-generating
- **Marco (ENTJ)** — Decisive, goal-oriented, big-picture
- **Sage (INFJ)** — Empathetic, insightful, meaning-focused
- **Kai (ESFJ)** — Social, supportive, community-building

### 3. S3 Domain

Sociocracy 3.0 (S3) defines clear domains, drivers, and constraints for each agent. See the [S3 Governance guide](/guide/s3-governance) for details.

### 4. Skills

Skills are reusable workflows that an agent can execute. Each skill has a trigger, a process, and defined inputs and outputs. See the [Skills System guide](/guide/skills) for details.

### 5. Responsibilities

Three core responsibilities define what each agent owns day-to-day.

## How Agents Coordinate

When a task arrives:

1. **Domain routing** — The task is routed to the agent whose S3 domain it falls under
2. **Cross-domain tasks** — If a task spans multiple domains, the Chief of Staff (Maya by default) coordinates
3. **Escalation** — Unresolved blockers escalate to you, the human operator
4. **Review cycle** — All deliverables go to "To review" status before being marked done

## Customizing Agents

You can customize any agent by editing your configuration files:

- **Rename them** — Give agents names that feel right for your workflow
- **Adjust roles** — Modify their role description to match your needs
- **Assign projects** — Limit an agent's scope to specific projects
- **Pick skills** — Choose which workflows each agent can execute
