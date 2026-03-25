import { AGENTS } from '~/types/agent'
import { SKILLS } from '~/types/skill'
import { PAIN_POINTS } from '~/types/wizard'

export interface AgentRecommendation {
  agentId: string
  name: string
  role: string
  score: number
  maxScore: number
  percentage: number
  matchedPainPoints: string[]
  suggestedSkills: string[]
  reason: string
}

export function getRecommendations(selectedPainPoints: string[]): AgentRecommendation[] {
  const agentScores: Record<string, { count: number; matches: string[] }> = {}

  for (const agent of AGENTS) {
    agentScores[agent.id] = { count: 0, matches: [] }
  }

  for (const ppId of selectedPainPoints) {
    const pp = PAIN_POINTS.find(p => p.id === ppId)
    if (!pp) continue
    for (const agentId of pp.agents) {
      agentScores[agentId].count++
      agentScores[agentId].matches.push(pp.label)
    }
  }

  const maxPossible = selectedPainPoints.length || 1

  return AGENTS
    .map((agent) => {
      const { count, matches } = agentScores[agent.id]
      const percentage = Math.round((count / maxPossible) * 100)

      const suggestedSkills = SKILLS
        .filter(s => s.defaultAgent === agent.id)
        .map(s => s.slug)

      let reason = ''
      if (count === 0) {
        reason = `${agent.name} doesn't directly address your selected pain points, but can still add value to your team.`
      } else if (count === 1) {
        reason = `${agent.name} addresses one of your key challenges: "${matches[0]}".`
      } else {
        reason = `${agent.name} addresses ${count} of your challenges, including "${matches[0]}" and "${matches[1]}".`
      }

      return {
        agentId: agent.id,
        name: agent.name,
        role: agent.role,
        score: count,
        maxScore: maxPossible,
        percentage,
        matchedPainPoints: matches,
        suggestedSkills,
        reason,
      }
    })
    .sort((a, b) => b.score - a.score)
}
