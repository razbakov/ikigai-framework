<script setup lang="ts">
import type { AgentDefinition } from '~/types/agent'

defineProps<{
  agent: AgentDefinition
}>()

const colorMap: Record<string, string> = {
  maya: 'border-t-[var(--color-maya)] bg-[var(--color-maya)]/5',
  viktor: 'border-t-[var(--color-viktor)] bg-[var(--color-viktor)]/5',
  luna: 'border-t-[var(--color-luna)] bg-[var(--color-luna)]/5',
  marco: 'border-t-[var(--color-marco)] bg-[var(--color-marco)]/5',
  sage: 'border-t-[var(--color-sage)] bg-[var(--color-sage)]/5',
  kai: 'border-t-[var(--color-kai)] bg-[var(--color-kai)]/5',
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
  <div
    class="rounded-xl border border-border border-t-4 p-6 transition-all hover:shadow-lg hover:-translate-y-1"
    :class="colorMap[agent.color]"
  >
    <div class="flex items-start justify-between mb-4">
      <div class="flex items-center gap-3">
        <div
          class="w-10 h-10 rounded-lg flex items-center justify-center bg-muted"
        >
          <Icon :name="agent.icon" class="w-5 h-5" :class="iconColorMap[agent.color]" />
        </div>
        <div>
          <h3 class="font-semibold text-lg">{{ agent.name }}</h3>
          <p class="text-sm text-muted-foreground">{{ agent.role }}</p>
        </div>
      </div>
      <span class="text-xs px-2 py-1 rounded-full bg-muted text-muted-foreground font-mono">
        {{ agent.personality }}
      </span>
    </div>
    <p class="text-sm text-muted-foreground mb-4 line-clamp-2">
      {{ agent.description }}
    </p>
    <ul class="space-y-2">
      <li
        v-for="resp in agent.responsibilities"
        :key="resp"
        class="flex items-start gap-2 text-sm"
      >
        <Icon name="lucide:check" class="w-4 h-4 mt-0.5 shrink-0 text-primary" />
        <span>{{ resp }}</span>
      </li>
    </ul>
  </div>
</template>
