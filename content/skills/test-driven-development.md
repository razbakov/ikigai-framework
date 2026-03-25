---
title: Test-Driven Development
description: Write failing tests first, then implement the minimum code to make them pass. Red-green-refactor for reliable software.
category: engineering
agent: viktor
complexity: intermediate
---

# Test-Driven Development

This skill enforces the TDD cycle: write a failing test first, implement just enough code to make it pass, then refactor. It produces well-tested, minimal implementations where every line of code exists because a test demanded it.

TDD works especially well with AI agents because it provides a clear, machine-verifiable feedback loop. The agent knows exactly when the work is done — when all tests pass.

## How It Works

1. **Understand the requirement** — Read the feature spec or issue and identify the behaviors that need to be tested. Focus on inputs and expected outputs, not implementation details.
2. **Write the failing test** — Create a test that describes the desired behavior. Run it to confirm it fails (red). A test that passes immediately isn't testing anything new.
3. **Write minimal code** — Implement the simplest possible code that makes the failing test pass (green). Resist the urge to add anything the test doesn't require.
4. **Refactor** — Clean up the implementation without changing behavior. The tests act as a safety net — if they still pass after refactoring, the behavior is preserved.
5. **Repeat** — Pick the next behavior, write a failing test, make it pass, refactor. Build up the feature incrementally, one tested behavior at a time.

## When to Use

- For any new feature where the requirements are clear enough to write tests
- When fixing bugs — write a test that reproduces the bug first, then fix it
- For refactoring — ensure existing behavior is covered by tests before changing code
- When working on critical paths (payments, authentication, data processing) where correctness matters most

## Requirements

- A working test framework configured in your project (Jest, Vitest, pytest, etc.)
- Clear requirements or acceptance criteria to derive test cases from
- `CLAUDE.md` with testing conventions (file naming, patterns, assertion style)
- The discipline to not skip the "write test first" step — it's tempting but defeats the purpose
