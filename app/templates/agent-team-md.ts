import type { WizardState } from '~/types/wizard'
import { AGENTS } from '~/types/agent'

export function generateAgentTeamMd(state: WizardState): string {
  const enabledAgents = state.agents.filter(a => a.enabled)

  const agentSections = enabledAgents.map((a) => {
    const def = AGENTS.find(d => d.id === a.id)
    if (!def) return ''

    const skills = state.selectedSkills[a.id] || []
    const projects = a.assignedProjects.length
      ? a.assignedProjects.join(', ')
      : 'All projects'

    return `### ${a.customName} — ${a.customRole}

- **Personality:** ${def.personality}
- **S3 Domain:** ${def.s3Domain}
- **Icon:** ${def.icon}

**Description:** ${def.description}

**Responsibilities:**
${def.responsibilities.map(r => `- ${r}`).join('\n')}

**Assigned Skills:** ${skills.join(', ') || 'None'}

**Assigned Projects:** ${projects}
`
  }).join('\n---\n\n')

  const decisionMatrix = enabledAgents.map((a) => {
    const def = AGENTS.find(d => d.id === a.id)
    return `| ${a.customName} | ${a.customRole} | ${def?.s3Domain || ''} | ${def?.painPointMatches.join(', ') || ''} |`
  }).join('\n')

  return `# Agent Team

This document defines your AI executive team. Each agent has a specific domain, personality, and set of skills.

## Team Overview

| Agent | Role | Domain | Handles |
|-------|------|--------|---------|
${decisionMatrix}

## Agent Definitions

${agentSections}

## Decision Matrix

When a task arrives, route it based on these rules:

1. **Identify the domain** — Which S3 domain does this task fall under?
2. **Check agent assignment** — Is there an agent assigned to this domain?
3. **Delegate or escalate** — If yes, delegate. If the task spans multiple domains, the Chief of Staff coordinates.

## Communication Flow

- **Daily standup:** ${enabledAgents.find(a => a.id === 'maya') ? enabledAgents.find(a => a.id === 'maya')?.customName : 'Chief of Staff'} runs the daily check-in
- **Cross-agent handoff:** Tasks that span domains go through the Chief of Staff
- **Escalation:** Unresolved blockers escalate to the human operator
- **Review cycle:** All deliverables go to "To review" status before being marked done

## S3 Framework

Each agent operates within the S3 (Situation-Strategy-System) framework:

- **Situation:** What tension or driver created this task?
- **Strategy:** What approach will resolve the tension?
- **System:** What repeatable process ensures this doesn't recur?

Every task card should include S3 analysis before work begins.
`
}
