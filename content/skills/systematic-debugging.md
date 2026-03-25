---
title: Systematic Debugging
description: Root cause analysis before applying fixes. Reproduces the issue, forms hypotheses, and verifies the fix addresses the actual cause.
category: engineering
agent: viktor
complexity: intermediate
---

# Systematic Debugging

This skill enforces a disciplined debugging methodology: reproduce first, hypothesize, narrow down, then fix. It prevents the common pattern of applying random fixes until something works, which often masks the real problem and introduces new bugs.

The agent treats debugging like a scientific investigation. Every hypothesis is tested. Every fix is verified against the root cause, not just the symptoms.

## How It Works

1. **Reproduce the issue** — Before anything else, create a reliable reproduction. If you can't reproduce it, you can't verify you fixed it. Document the exact steps, inputs, and environment.
2. **Form hypotheses** — Based on the error message, logs, and reproduction steps, list possible causes ranked by likelihood. Don't guess randomly — use the evidence to narrow the search.
3. **Binary search** — Systematically eliminate hypotheses. Use logging, breakpoints, or code bisection to narrow down the exact location and trigger. Cut the problem space in half with each test.
4. **Identify root cause** — Once located, understand why the bug exists, not just where. Is it a logic error? Race condition? Wrong assumption about an API? The root cause determines the right fix.
5. **Fix and verify** — Apply the minimal fix that addresses the root cause. Run the reproduction steps to confirm the issue is resolved. Add a regression test so it never comes back.

## When to Use

- For any bug that isn't immediately obvious from reading the error message
- When a fix attempt didn't work and you're tempted to try random things
- For intermittent bugs that are hard to reproduce
- When a bug might have security implications — you need to understand the full scope
- Before declaring "it works on my machine" — systematic reproduction reveals environment-specific issues

## Requirements

- Access to the codebase and ability to run the application locally
- Error logs, stack traces, or reproduction steps from the bug report
- A test framework to write regression tests after fixing
- Patience — systematic debugging is slower at the start but faster overall because you fix the right thing the first time
