<script setup lang="ts">
import type { SkillEntry } from '~/types/skill'
import { AGENTS } from '~/types/agent'

const props = defineProps<{
  skill: SkillEntry
}>()

const defaultAgentDef = computed(() => AGENTS.find(a => a.id === props.skill.defaultAgent))

const categoryColors: Record<string, string> = {
  operations: 'bg-[var(--color-maya)]/10 text-[var(--color-maya)]',
  engineering: 'bg-[var(--color-viktor)]/10 text-[var(--color-viktor)]',
  content: 'bg-[var(--color-luna)]/10 text-[var(--color-luna)]',
  strategy: 'bg-[var(--color-marco)]/10 text-[var(--color-marco)]',
  personal: 'bg-[var(--color-sage)]/10 text-[var(--color-sage)]',
  community: 'bg-[var(--color-kai)]/10 text-[var(--color-kai)]',
}

const complexityColors: Record<string, string> = {
  simple: 'bg-green-500/10 text-green-400',
  moderate: 'bg-yellow-500/10 text-yellow-400',
  advanced: 'bg-red-500/10 text-red-400',
}
</script>

<template>
  <NuxtLink
    :to="`/skills/${skill.slug}`"
    class="block bg-card border border-border rounded-lg p-5 hover:shadow-lg hover:-translate-y-0.5 transition-all"
  >
    <div class="flex items-start justify-between mb-3">
      <h3 class="font-semibold">{{ skill.name }}</h3>
      <span class="text-xs px-2 py-0.5 rounded-full" :class="complexityColors[skill.complexity]">
        {{ skill.complexity }}
      </span>
    </div>
    <p class="text-sm text-muted-foreground mb-4 line-clamp-3">
      {{ skill.description }}
    </p>
    <div class="flex items-center justify-between">
      <span class="text-xs px-2 py-1 rounded-full capitalize" :class="categoryColors[skill.category]">
        {{ skill.category }}
      </span>
      <div v-if="defaultAgentDef" class="flex items-center gap-1 text-xs text-muted-foreground">
        <Icon :name="defaultAgentDef.icon" class="w-3.5 h-3.5" />
        {{ defaultAgentDef.name }}
      </div>
    </div>
  </NuxtLink>
</template>
