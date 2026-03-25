import JSZip from 'jszip'
import { saveAs } from 'file-saver'
import type { WizardState } from '~/types/wizard'
import { generateClaudeMd } from '~/templates/claude-md'
import { generateAgentTeamMd } from '~/templates/agent-team-md'
import { generateSkillConfig } from '~/templates/skill-config'
import { SKILLS } from '~/types/skill'

export async function packageFiles(state: WizardState): Promise<void> {
  const zip = new JSZip()

  zip.file('CLAUDE.md', generateClaudeMd(state))
  zip.file('initiatives/agent-team.md', generateAgentTeamMd(state))

  const enabledAgents = state.agents.filter(a => a.enabled)

  for (const agent of enabledAgents) {
    const agentSkills = state.selectedSkills[agent.id] || []
    for (const skillSlug of agentSkills) {
      const skill = SKILLS.find(s => s.slug === skillSlug)
      if (skill) {
        zip.file(
          `skills/${agent.id}/${skill.slug}/SKILL.md`,
          generateSkillConfig(skill.slug, skill.name, skill.description),
        )
      }
    }
  }

  zip.file('README.md', `# AI Cabinet Setup\n\nGenerated configuration for your AI agent team.\n\n## Quick Start\n\n1. Copy \`CLAUDE.md\` to the root of your project\n2. Copy \`initiatives/agent-team.md\` to your project\n3. Copy skill files from \`skills/\` to your \`.claude/\` directory\n4. Start a Claude Code session and reference your agent team\n\nSee the [AI Cabinet Guide](https://ai-cabinet.netlify.app/guide) for detailed setup instructions.\n`)

  const blob = await zip.generateAsync({ type: 'blob' })
  saveAs(blob, 'ai-cabinet-config.zip')
}

export function getFileList(state: WizardState): string[] {
  const files: string[] = ['CLAUDE.md', 'initiatives/agent-team.md', 'README.md']

  const enabledAgents = state.agents.filter(a => a.enabled)
  for (const agent of enabledAgents) {
    const agentSkills = state.selectedSkills[agent.id] || []
    for (const skillSlug of agentSkills) {
      files.push(`skills/${agent.id}/${skillSlug}/SKILL.md`)
    }
  }

  return files
}
