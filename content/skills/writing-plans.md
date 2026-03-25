---
title: Write Implementation Plans
description: Design detailed implementation plans from specs or requirements before writing any code.
category: engineering
agent: viktor
complexity: intermediate
---

# Write Implementation Plans

This skill produces a structured implementation plan before any code is written. It takes a feature spec, requirements doc, or even a rough idea and breaks it down into phases, files to change, risks to mitigate, and acceptance criteria to verify. The plan becomes the blueprint that the executing agent follows.

Planning before coding catches architectural mistakes early, when they're cheap to fix. It also makes it possible to review the approach before investing hours in implementation.

## How It Works

1. **Understand the goal** — Read the input (issue, spec, requirements, or conversation) and clarify the desired outcome. Ask questions if the spec is ambiguous.
2. **Map the solution** — Identify which parts of the codebase need changes. Outline the technical approach, data flow, and component interactions.
3. **Break into phases** — Split the work into ordered phases, each with a clear deliverable. Earlier phases lay groundwork; later phases build on it.
4. **Identify risks** — Call out unknowns, dependencies, and potential failure points. Propose mitigations or spikes for high-uncertainty areas.
5. **Define acceptance criteria** — For each phase, specify how to verify it's done. Include test cases, manual checks, and performance expectations.

## When to Use

- Before starting any non-trivial feature (more than a few hours of work)
- When multiple files or components need coordinated changes
- For architectural decisions that affect the project long-term
- When you want to review the approach before committing engineering time
- Before dispatching sub-agents — the plan becomes their instructions

## Requirements

- A clear feature spec, requirements document, or well-written issue
- Access to the codebase for the agent to understand existing patterns
- `CLAUDE.md` with project architecture notes (helps the agent make better plans)
- Time for you to review the plan before execution begins
