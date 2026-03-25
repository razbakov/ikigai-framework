<script setup lang="ts">
import { useWizardStore } from '~/stores/wizard'
import { PAIN_POINTS } from '~/types/wizard'
import { AGENTS } from '~/types/agent'

const store = useWizardStore()

function getAgentNames(agentIds: readonly string[]) {
  return agentIds.map((id) => {
    const agent = AGENTS.find(a => a.id === id)
    return agent?.name || id
  })
}

const iconColorMap: Record<string, string> = {
  maya: 'text-[var(--color-maya)]',
  viktor: 'text-[var(--color-viktor)]',
  luna: 'text-[var(--color-luna)]',
  marco: 'text-[var(--color-marco)]',
  sage: 'text-[var(--color-sage)]',
  kai: 'text-[var(--color-kai)]',
}
</script>

<template>
  <div class="space-y-8">
    <div>
      <h2 class="text-2xl font-bold mb-2">What Are Your Biggest Challenges?</h2>
      <p class="text-muted-foreground">
        Select the pain points that resonate with you. This helps us recommend the right
        agents for your situation.
      </p>
      <p class="text-sm text-muted-foreground mt-1">
        Selected: {{ store.painPoints.length }} / {{ PAIN_POINTS.length }}
      </p>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
      <button
        v-for="pp in PAIN_POINTS"
        :key="pp.id"
        class="text-left p-4 rounded-lg border transition-all"
        :class="store.painPoints.includes(pp.id)
          ? 'border-primary bg-primary/10 ring-1 ring-primary'
          : 'border-border hover:border-muted-foreground/30 bg-card'"
        @click="store.togglePainPoint(pp.id)"
      >
        <div class="flex items-start gap-3">
          <div
            class="w-5 h-5 rounded border-2 flex items-center justify-center shrink-0 mt-0.5 transition-colors"
            :class="store.painPoints.includes(pp.id)
              ? 'border-primary bg-primary'
              : 'border-muted-foreground/30'"
          >
            <Icon
              v-if="store.painPoints.includes(pp.id)"
              name="lucide:check"
              class="w-3 h-3 text-primary-foreground"
            />
          </div>
          <div>
            <p class="text-sm font-medium leading-tight">{{ pp.label }}</p>
            <div class="flex gap-1 mt-2">
              <span
                v-for="agentId in pp.agents"
                :key="agentId"
                class="text-xs px-1.5 py-0.5 rounded bg-muted"
                :class="iconColorMap[agentId]"
              >
                {{ getAgentNames([agentId])[0] }}
              </span>
            </div>
          </div>
        </div>
      </button>
    </div>
  </div>
</template>
