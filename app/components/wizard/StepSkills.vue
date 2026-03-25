<script setup lang="ts">
import { useWizardStore } from '~/stores/wizard'
import { AGENTS } from '~/types/agent'
import { SKILLS } from '~/types/skill'

const store = useWizardStore()

const enabledAgents = computed(() => store.agents.filter(a => a.enabled))

const searchQuery = ref('')

function getAgentSkills(agentId: string) {
  const agent = AGENTS.find(a => a.id === agentId)
  if (!agent) return []

  const categoryMap: Record<string, string> = {
    maya: 'operations',
    viktor: 'engineering',
    luna: 'content',
    marco: 'strategy',
    sage: 'personal',
    kai: 'community',
  }

  return SKILLS.filter((skill) => {
    const matchesCategory = skill.category === categoryMap[agentId] || skill.defaultAgent === agentId
    const matchesSearch = !searchQuery.value
      || skill.name.toLowerCase().includes(searchQuery.value.toLowerCase())
      || skill.description.toLowerCase().includes(searchQuery.value.toLowerCase())
    return matchesCategory && matchesSearch
  })
}

function isSkillSelected(agentId: string, skillSlug: string) {
  return (store.selectedSkills[agentId] || []).includes(skillSlug)
}

const iconColorMap: Record<string, string> = {
  maya: 'text-[var(--color-maya)]',
  viktor: 'text-[var(--color-viktor)]',
  luna: 'text-[var(--color-luna)]',
  marco: 'text-[var(--color-marco)]',
  sage: 'text-[var(--color-sage)]',
  kai: 'text-[var(--color-kai)]',
}

const complexityColors: Record<string, string> = {
  simple: 'bg-green-500/10 text-green-400',
  moderate: 'bg-yellow-500/10 text-yellow-400',
  advanced: 'bg-red-500/10 text-red-400',
}
</script>

<template>
  <div class="space-y-8">
    <div>
      <h2 class="text-2xl font-bold mb-2">Choose Skills for Each Agent</h2>
      <p class="text-muted-foreground">
        Select which skills each agent should have. Default skills are pre-selected based on
        the agent's role.
      </p>
    </div>

    <div class="relative">
      <Icon name="lucide:search" class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Filter skills..."
        class="w-full pl-10 pr-4 py-2.5 rounded-lg bg-muted border border-input text-sm focus:ring-2 focus:ring-ring outline-none"
      >
    </div>

    <div class="space-y-6">
      <div v-for="agent in enabledAgents" :key="agent.id">
        <div class="flex items-center gap-2 mb-3">
          <Icon
            :name="AGENTS.find(a => a.id === agent.id)?.icon || 'lucide:user'"
            class="w-5 h-5"
            :class="iconColorMap[agent.id]"
          />
          <h3 class="font-semibold">{{ agent.customName }}</h3>
          <span class="text-xs text-muted-foreground">
            ({{ (store.selectedSkills[agent.id] || []).length }} selected)
          </span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
          <button
            v-for="skill in getAgentSkills(agent.id)"
            :key="skill.slug"
            class="text-left p-3 rounded-lg border transition-all"
            :class="isSkillSelected(agent.id, skill.slug)
              ? 'border-primary bg-primary/5 ring-1 ring-primary'
              : 'border-border hover:border-muted-foreground/30 bg-card'"
            @click="store.toggleSkill(agent.id, skill.slug)"
          >
            <div class="flex items-start justify-between">
              <h4 class="text-sm font-medium">{{ skill.name }}</h4>
              <span class="text-xs px-1.5 py-0.5 rounded" :class="complexityColors[skill.complexity]">
                {{ skill.complexity }}
              </span>
            </div>
            <p class="text-xs text-muted-foreground mt-1 line-clamp-2">{{ skill.description }}</p>
          </button>
        </div>

        <div v-if="getAgentSkills(agent.id).length === 0" class="text-sm text-muted-foreground py-2">
          No skills match your search.
        </div>
      </div>
    </div>
  </div>
</template>
