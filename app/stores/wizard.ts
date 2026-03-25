import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { WizardState, WizardProject, WizardAgent } from '~/types/wizard'
import { PAIN_POINTS } from '~/types/wizard'
import { AGENTS } from '~/types/agent'

export const useWizardStore = defineStore('wizard', () => {
  const mission = ref('')
  const vision = ref('')
  const projects = ref<WizardProject[]>([{ name: '', description: '', techStack: '' }])
  const painPoints = ref<string[]>([])
  const agents = ref<WizardAgent[]>([])
  const selectedSkills = ref<Record<string, string[]>>({})
  const step = ref(1)

  const currentStep = computed(() => step.value)

  const recommendedAgents = computed(() => {
    const scores: Record<string, number> = {}
    for (const pp of painPoints.value) {
      const painPoint = PAIN_POINTS.find(p => p.id === pp)
      if (painPoint) {
        for (const agentId of painPoint.agents) {
          scores[agentId] = (scores[agentId] || 0) + 1
        }
      }
    }
    return AGENTS
      .map(agent => ({
        ...agent,
        score: scores[agent.id] || 0,
        matchedPainPoints: painPoints.value.filter(pp => {
          const p = PAIN_POINTS.find(x => x.id === pp)
          return p?.agents.includes(agent.id)
        }),
      }))
      .sort((a, b) => b.score - a.score)
  })

  function isStepValid(s: number): boolean {
    switch (s) {
      case 1:
        return mission.value.trim().length > 10
      case 2:
        return projects.value.some(p => p.name.trim().length > 0)
      case 3:
        return painPoints.value.length >= 1
      case 4:
        return true
      case 5:
        return agents.value.some(a => a.enabled)
      case 6:
        return true
      case 7:
        return true
      default:
        return false
    }
  }

  function setMission(value: string) {
    mission.value = value
  }

  function setVision(value: string) {
    vision.value = value
  }

  function addProject() {
    if (projects.value.length < 5) {
      projects.value.push({ name: '', description: '', techStack: '' })
    }
  }

  function removeProject(index: number) {
    if (projects.value.length > 1) {
      projects.value.splice(index, 1)
    }
  }

  function togglePainPoint(id: string) {
    const idx = painPoints.value.indexOf(id)
    if (idx === -1) {
      painPoints.value.push(id)
    } else {
      painPoints.value.splice(idx, 1)
    }
  }

  function setAgents(agentList: WizardAgent[]) {
    agents.value = agentList
  }

  function toggleSkill(agentId: string, skillSlug: string) {
    if (!selectedSkills.value[agentId]) {
      selectedSkills.value[agentId] = []
    }
    const idx = selectedSkills.value[agentId].indexOf(skillSlug)
    if (idx === -1) {
      selectedSkills.value[agentId].push(skillSlug)
    } else {
      selectedSkills.value[agentId].splice(idx, 1)
    }
  }

  function setStep(s: number) {
    step.value = s
  }

  function initAgentsFromRecommendations() {
    agents.value = recommendedAgents.value.map(a => ({
      id: a.id,
      enabled: a.score > 0,
      customName: a.name,
      customRole: a.role,
      assignedProjects: [],
    }))
    for (const agent of agents.value) {
      const def = AGENTS.find(a => a.id === agent.id)
      if (def && agent.enabled) {
        selectedSkills.value[agent.id] = [...def.defaultSkills]
      }
    }
  }

  function reset() {
    mission.value = ''
    vision.value = ''
    projects.value = [{ name: '', description: '', techStack: '' }]
    painPoints.value = []
    agents.value = []
    selectedSkills.value = {}
    step.value = 1
  }

  function getState(): WizardState {
    return {
      mission: mission.value,
      vision: vision.value,
      projects: projects.value,
      painPoints: painPoints.value,
      agents: agents.value,
      selectedSkills: selectedSkills.value,
    }
  }

  return {
    mission,
    vision,
    projects,
    painPoints,
    agents,
    selectedSkills,
    step,
    currentStep,
    recommendedAgents,
    isStepValid,
    setMission,
    setVision,
    addProject,
    removeProject,
    togglePainPoint,
    setAgents,
    toggleSkill,
    setStep,
    initAgentsFromRecommendations,
    reset,
    getState,
  }
}, {
  persist: true,
})
