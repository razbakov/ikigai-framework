## Agent Proactivity

Top-manager agents initiate work; the Commander reviews and redirects. Proactivity
converts a passive reply system into a self-driving circle without sacrificing direction.

This rule sits on top of `agent-protocols.md` (message format + default-consent) and
`agent-team.md` (roles). Read those first.

### Two trigger types

- **Cadence triggers** (cron) — each manager wakes on their own schedule, scans their
  domain, decides whether anything is review-ready or redirect-worthy. Predictable, easy
  to debug.
- **Event triggers** — domain events wake the manager out-of-cycle (new contact arrives,
  DAU drops, deadline approaches, inbox message lands, PR opened). Quieter but harder to
  reason about.

Use cadence as the primary trigger. Add events only where waiting for the next cycle
would cause real damage.

### Review-ready threshold

A cycle does not have to produce a message. The manager only sends to the Commander if:

- A decision is needed (ship-or-not, approve-or-not, redirect-or-not), OR
- A delivered outcome is worth surfacing (PR merged, content published, contact processed), OR
- A drift is worth flagging (KR slipping, deadline missed, anomaly detected).

If the cycle finds nothing in those three categories, the manager logs "nothing to surface"
in their state and stays silent. **Proactivity is not noise.** A daily silent cycle is a
healthy cycle.

### Reply patterns

The Commander steers with short replies. The manager parses these and adjusts the next cycle:

| Reply | Effect |
|---|---|
| `ok` / `ship it` / `yes` | Consent now — don't wait for the time-box |
| `no` / `change X` / `do Y instead` | Revise and resend the same review-ready message |
| `pause` / `hold` | Skip the next cycle; resume on next Commander signal |
| `focus: <theme>` | Set the focus signal for upcoming cycles |

Silence past the time-box → consent (per `agent-protocols.md`).

The **focus signal** is the redirect channel. All managers read the most recent focus
signal at the start of each cycle and re-sort their domain accordingly. A manager whose
domain doesn't match the current focus runs a short cycle (or skips it) instead of forcing
unrelated asks through.

### Digest discipline

Six managers running daily cycles can flood the Commander. The Chief-of-Staff role
consolidates: instead of six review-ready messages, the Commander gets **one daily digest**
where each manager has a short slot (or a "nothing to surface" line).

Digest shape:

- One ping per day to the Commander
- Each manager's slot ≤ 5 lines, in review-ready format (Why · What · Media · Asking)
- Each open ask carries its own time-box; replying to one item ages others normally
- Out-of-cycle event triggers can still send their own message (they're urgent by definition)

The digest cadence and the consolidating manager (typically Chief of Staff) are
instance-level config. The protocol is: **one daily digest > six daily pings.**

### Cadence config (instance-level)

Specific cadences depend on the Commander's rhythm and risk tolerance, so they live in
each manager's agent file at `.claude/agents/<name>.md` under a **Cadence** section, not
in this framework rule.

Each manager's Cadence entry should answer:

- **When** does the cycle wake (cron expression or natural-language schedule)?
- **What** does the cycle scan (state, KRs, inboxes, dashboards)?
- **Threshold** — what counts as review-ready in this manager's domain?
- **Output** — does the manager submit to the daily digest, or send out-of-cycle?

If a manager has no Cadence section, they are reactive-only.
