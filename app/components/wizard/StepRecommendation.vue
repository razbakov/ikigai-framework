<script setup lang="ts">
import { useWizardStore } from '~/stores/wizard'
import { getRecommendations } from '~/utils/recommendation-engine'
import { AGENTS } from '~/types/agent'

const store = useWizardStore()

const recommendations = computed(() => getRecommendations(store.painPoints))

const colorMap: Record<string, string> = {
  maya: 'border-l-[var(--color-maya)]',
  viktor: 'border-l-[var(--color-viktor)]',
  luna: 'border-l-[var(--color-luna)]',
  marco: 'border-l-[var(--color-marco)]',
  sage: 'border-l-[var(--color-sage)]',
  kai: 'border-l-[var(--color-kai)]',
}

const iconColorMap: Record<string, string> = {
  maya: 'text-[var(--color-maya)]',
  viktor: 'text-[var(--color-viktor)]',
  luna: 'text-[var(--color-luna)]',
  marco: 'text-[var(--color-marco)]',
  sage: 'text-[var(--color-sage)]',
  kai: 'text-[var(--color-kai)]',
}

onMounted(() => {
  store.initAgentsFromRecommendations()
})
</script>

<template>
  <div class="space-y-8">
    <div>
      <h2 class="text-2xl font-bold mb-2">Your Recommended Team</h2>
      <p class="text-muted-foreground">
        Based on your pain points, here are the agents ranked by relevance to your challenges.
        You will customize them in the next step.
      </p>
    </div>

    <div class="space-y-4">
      <div
        v-for="rec in recommendations"
        :key="rec.agentId"
        class="bg-card border border-border border-l-4 rounded-lg p-5"
        :class="colorMap[rec.agentId]"
      >
        <div class="flex items-start justify-between">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-lg bg-muted flex items-center justify-center">
              <Icon
                :name="AGENTS.find(a => a.id === rec.agentId)?.icon || 'lucide:user'"
                class="w-5 h-5"
                :class="iconColorMap[rec.agentId]"
              />
            </div>
            <div>
              <h3 class="font-semibold">{{ rec.name }}</h3>
              <p class="text-sm text-muted-foreground">{{ rec.role }}</p>
            </div>
          </div>
          <div class="text-right">
            <div class="text-2xl font-bold" :class="rec.score > 0 ? 'text-primary' : 'text-muted-foreground'">
              {{ rec.percentage }}%
            </div>
            <div class="text-xs text-muted-foreground">match</div>
          </div>
        </div>

        <p class="mt-3 text-sm text-muted-foreground">
          {{ rec.reason }}
        </p>

        <div v-if="rec.matchedPainPoints.length > 0" class="mt-3 flex flex-wrap gap-1.5">
          <span
            v-for="pp in rec.matchedPainPoints"
            :key="pp"
            class="text-xs px-2 py-1 rounded-full bg-primary/10 text-primary"
          >
            {{ pp }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
