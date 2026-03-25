---
title: S3 Governance for Agent Teams
description: Define clear ownership domains for each agent using Sociocracy 3.0 patterns. Prevents overlap and ensures accountability.
---

# S3 Governance for Agent Teams

Sociocracy 3.0 (S3) provides a practical framework for organizing your AI agent team. It solves the core problem of multi-agent systems: who does what, who decides what, and what happens when domains overlap.

## What is Sociocracy 3.0

S3 is a governance framework built on three principles:

- **Effectiveness** — devote time only to what brings you closer to your goals
- **Consent** — raise and resolve objections to decisions that affect you
- **Equivalence** — involve people in making decisions that affect them

For AI agents, we adapt these principles to create clear ownership, explicit constraints, and a decision-making protocol that keeps you in control.

## Domains: Clear Ownership

Each agent owns a **domain** — a clearly defined area of responsibility. A domain includes:

- **Driver** — why this domain exists (the need it serves)
- **Key responsibilities** — what the agent handles day-to-day
- **Constraints** — what the agent cannot do without your approval

Example for Maya (Chief of Staff):

| Element | Definition |
|---------|-----------|
| **Driver** | You need a reliable system to stay on track without spending time on coordination |
| **Responsibilities** | Daily reviews, inbox processing, calendar management, task dispatch |
| **Constraints** | Cannot make strategic decisions, cannot create content, cannot cancel meetings |

## Drivers: Why Each Agent Exists

Every agent should be justified by a clear **driver** — a statement of the organizational need it addresses. If you can't articulate why an agent exists, you probably don't need it yet.

Good drivers follow the pattern: *"[Situation] requires [response] because [consequence of inaction]."*

- "Multiple projects need engineering progress, but you can't write every line of code." (Viktor)
- "Raw ideas exist but aren't reaching people. You need to build an audience." (Luna)
- "Without intentional reflection, the pattern of burning out repeats." (Sage)

## Constraints: What Agents Cannot Do

Constraints are more important than responsibilities. They define the safety boundaries:

- **Financial constraints** — no agent commits money without approval
- **Communication constraints** — no agent represents you externally
- **Irreversible action constraints** — no agent deletes, publishes, or deploys without consent
- **Domain boundary constraints** — agents stay in their lane

These constraints should be explicit in each agent's CLAUDE.md configuration.

## Consent-Based Decisions

The decision protocol for your agent team:

1. **Agent proposes** — the agent identifies a need and suggests a response
2. **You review** — check the proposal against your goals and constraints
3. **Objections** — if something feels wrong, the agent adjusts
4. **Consent** — silence is not consent; you explicitly approve or reject

In practice, this means agents present plans and wait for your "go ahead" before executing irreversible actions.

## The Decision Authority Matrix

Define three tiers of agent autonomy:

| Tier | Examples | Protocol |
|------|----------|----------|
| **Autonomous** | Read files, search code, draft plans | Agent acts freely |
| **Inform** | Create branches, run tests, process inbox | Agent acts and reports |
| **Approve** | Publish content, merge PRs, send messages | Agent proposes and waits |

## When to Adjust Domains

Review agent domains quarterly or when you notice:

- **Overlap** — two agents working on the same thing
- **Gaps** — work falling through the cracks
- **Overreach** — an agent acting outside its constraints
- **Atrophy** — a domain that no longer serves a real need

The quarterly retro is a good time to evaluate whether your agent team structure still matches your actual needs.

## Next Steps

With governance in place, explore the [full skill catalog](/skills) to equip your agents with the capabilities they need.
