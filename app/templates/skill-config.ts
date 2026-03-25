export function generateSkillConfig(slug: string, name: string, description: string): string {
  return `---
name: ${name}
slug: ${slug}
version: 1.0.0
---

# ${name}

${description}

## Trigger

This skill is activated when:
- Manually invoked via \`/${slug}\`
- Scheduled as part of a recurring workflow
- Triggered by another agent's handoff

## Process

1. **Gather context** — Collect relevant inputs and current state
2. **Analyze** — Assess the situation using S3 framework
3. **Execute** — Perform the core task
4. **Verify** — Check the output meets quality standards
5. **Report** — Summarize what was done and any follow-up items

## Inputs

- Current project state
- Relevant files and data sources
- Previous execution history (if recurring)

## Outputs

- Task completion summary
- Any created or modified files
- Follow-up items (if any)

## Quality Checklist

- [ ] Output matches the skill description
- [ ] No placeholder or TODO items remain
- [ ] Results are verified (tests pass, links work, etc.)
- [ ] Follow-up items are tracked in the task board
`
}
