<script setup lang="ts">
import { useWizardStore } from '~/stores/wizard'
import { AGENTS } from '~/types/agent'

const store = useWizardStore()

const iconColorMap: Record<string, string> = {
  maya: 'text-[var(--color-maya)]',
  viktor: 'text-[var(--color-viktor)]',
  luna: 'text-[var(--color-luna)]',
  marco: 'text-[var(--color-marco)]',
  sage: 'text-[var(--color-sage)]',
  kai: 'text-[var(--color-kai)]',
}

function toggleAgent(agentId: string) {
  const agent = store.agents.find(a => a.id === agentId)
  if (agent) {
    agent.enabled = !agent.enabled
  }
}

function toggleProject(agentId: string, projectName: string) {
  const agent = store.agents.find(a => a.id === agentId)
  if (!agent) return
  const idx = agent.assignedProjects.indexOf(projectName)
  if (idx === -1) {
    agent.assignedProjects.push(projectName)
  } else {
    agent.assignedProjects.splice(idx, 1)
  }
}
</script>

<template>
  <div class="space-y-8">
    <div>
      <h2 class="text-2xl font-bold mb-2">Customize Your Agents</h2>
      <p class="text-muted-foreground">
        Enable or disable agents, give them custom names, and assign them to specific projects.
      </p>
    </div>

    <div class="space-y-4">
      <div
        v-for="agent in store.agents"
        :key="agent.id"
        class="bg-card border border-border rounded-lg overflow-hidden transition-opacity"
        :class="agent.enabled ? '' : 'opacity-50'"
      >
        <div class="p-5">
          <div class="flex items-start justify-between mb-4">
            <div class="flex items-center gap-3">
              <Icon
                :name="AGENTS.find(a => a.id === agent.id)?.icon || 'lucide:user'"
                class="w-6 h-6"
                :class="iconColorMap[agent.id]"
              />
              <div>
                <h3 class="font-semibold">{{ AGENTS.find(a => a.id === agent.id)?.name }}</h3>
                <p class="text-xs text-muted-foreground">
                  {{ AGENTS.find(a => a.id === agent.id)?.role }}
                </p>
              </div>
            </div>
            <button
              class="relative w-12 h-6 rounded-full transition-colors"
              :class="agent.enabled ? 'bg-primary' : 'bg-muted'"
              @click="toggleAgent(agent.id)"
            >
              <span
                class="absolute top-1 w-4 h-4 rounded-full bg-white transition-transform"
                :class="agent.enabled ? 'left-7' : 'left-1'"
              />
            </button>
          </div>

          <div v-if="agent.enabled" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label class="block text-xs font-medium text-muted-foreground mb-1">
                  Custom Name
                </label>
                <input
                  v-model="agent.customName"
                  type="text"
                  class="w-full px-3 py-2 rounded-md bg-muted border border-input text-sm focus:ring-2 focus:ring-ring outline-none"
                  :placeholder="AGENTS.find(a => a.id === agent.id)?.name"
                >
              </div>
              <div>
                <label class="block text-xs font-medium text-muted-foreground mb-1">
                  Custom Role
                </label>
                <input
                  v-model="agent.customRole"
                  type="text"
                  class="w-full px-3 py-2 rounded-md bg-muted border border-input text-sm focus:ring-2 focus:ring-ring outline-none"
                  :placeholder="AGENTS.find(a => a.id === agent.id)?.role"
                >
              </div>
            </div>

            <div v-if="store.projects.some(p => p.name.trim())">
              <label class="block text-xs font-medium text-muted-foreground mb-2">
                Assign to Projects
                <span class="font-normal">(leave empty for all)</span>
              </label>
              <div class="flex flex-wrap gap-2">
                <button
                  v-for="project in store.projects.filter(p => p.name.trim())"
                  :key="project.name"
                  class="text-xs px-3 py-1.5 rounded-full border transition-colors"
                  :class="agent.assignedProjects.includes(project.name)
                    ? 'border-primary bg-primary/10 text-primary'
                    : 'border-border hover:border-muted-foreground/50'"
                  @click="toggleProject(agent.id, project.name)"
                >
                  {{ project.name }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
