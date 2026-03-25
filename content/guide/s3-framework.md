---
title: S3 Framework
description: The Situation-Strategy-System framework that guides how agents think and operate.
---

# S3 Framework

S3 stands for **Situation, Strategy, System**. It is the decision-making framework that guides how your AI agents approach every task.

## The Three Layers

### Situation
Before taking action, the agent analyzes the current situation:

- **Tension** — What is the gap between current state and desired state?
- **Driver** — What is causing this tension? Why does it matter now?
- **Requirement** — What would a successful resolution look like?

### Strategy
The agent then decides on an approach:

- **Response Options** — What are the possible approaches?
- **Selected Strategy** — Which approach best addresses the tension?
- **Trade-offs** — What are we accepting by choosing this approach?

### System
Finally, the agent thinks about sustainability:

- **Repeatable Process** — Can this be turned into a reusable workflow?
- **Feedback Loop** — How will we know if this is working?
- **Iteration Plan** — How will we improve this over time?

## S3 in Practice

Every task card in your project should include S3 analysis before work begins. This ensures agents do not jump straight to solutions without understanding the problem.

### Example: Bug Report

**Situation:**
- Tension: Users report a broken checkout flow
- Driver: A recent deploy changed the payment API
- Requirement: All users can complete checkout within 24 hours

**Strategy:**
- Options: Rollback deploy, hotfix the API call, add retry logic
- Selected: Hotfix the API call (fastest, most targeted)
- Trade-off: No retry logic for now (address in follow-up)

**System:**
- Process: Add integration tests for payment flow to CI
- Feedback: Monitor checkout success rate in analytics
- Iteration: Review payment resilience in next sprint

## Why S3 Matters

Without S3, agents (and humans) tend to jump straight to solutions. S3 forces a pause to understand:

1. Why are we doing this?
2. What is the best approach?
3. How do we prevent this from recurring?

This leads to better decisions, less rework, and a growing library of reusable systems.
