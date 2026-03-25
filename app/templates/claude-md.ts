import type { WizardState } from '~/types/wizard'
import { AGENTS } from '~/types/agent'

export function generateClaudeMd(state: WizardState): string {
  const enabledAgents = state.agents.filter(a => a.enabled)

  const projectList = state.projects
    .filter(p => p.name.trim())
    .map(p => `- **${p.name}**${p.description ? `: ${p.description}` : ''}${p.techStack ? ` (${p.techStack})` : ''}`)
    .join('\n')

  const agentRules = enabledAgents.map((a) => {
    const def = AGENTS.find(d => d.id === a.id)
    const skills = state.selectedSkills[a.id] || []
    return `### ${a.customName} — ${a.customRole}\n- **S3 Domain:** ${def?.s3Domain || 'General'}\n- **Skills:** ${skills.join(', ') || 'None assigned'}\n- **Assigned Projects:** ${a.assignedProjects.length ? a.assignedProjects.join(', ') : 'All projects'}`
  }).join('\n\n')

  return `# Project Configuration

**Mission:** ${state.mission || 'Define your mission'}

**Vision:** ${state.vision || 'Define your vision'}

## Projects

${projectList || '- No projects defined yet'}

## Agent Team

The following AI agents are configured for this workspace. Each agent has a defined S3 domain (Situation, Strategy, System) and a set of skills they can execute.

See \`initiatives/agent-team.md\` for full agent definitions, decision matrix, and communication flow.

${agentRules || 'No agents configured.'}

## Rules

- When a task falls within an agent's S3 domain, route it to that agent.
- Agents must create a PR as their final deliverable — work without a PR is invisible.
- Never set a task to "Done" without verification — always "To review" first.
- Each agent operates autonomously within their domain but escalates cross-domain decisions.
- Use plan mode for any non-trivial task (3+ steps or architectural decisions).
- After any correction: update lessons learned with the pattern to prevent recurrence.
`
}
