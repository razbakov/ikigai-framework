<script setup lang="ts">
import { SKILLS } from '~/types/skill'
import { AGENTS } from '~/types/agent'

const route = useRoute()
const slug = computed(() => route.params.slug as string)

const skill = computed(() => SKILLS.find(s => s.slug === slug.value))
const agent = computed(() => skill.value ? AGENTS.find(a => a.id === skill.value!.defaultAgent) : null)

useHead({
  title: computed(() => skill.value ? `${skill.value.name} — Ikigai Team Skills` : 'Skill Not Found'),
})

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
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
    <div v-if="!skill" class="text-center py-20">
      <Icon name="lucide:search-x" class="w-12 h-12 mx-auto mb-4 text-muted-foreground" />
      <h1 class="text-2xl font-bold mb-2">Skill Not Found</h1>
      <p class="text-muted-foreground mb-6">The skill "{{ slug }}" doesn't exist in our catalog.</p>
      <NuxtLink to="/skills" class="text-primary hover:underline">Back to Skills</NuxtLink>
    </div>

    <div v-else>
      <NuxtLink to="/skills" class="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground mb-6">
        <Icon name="lucide:arrow-left" class="w-4 h-4" />
        Back to Skills
      </NuxtLink>

      <div class="mb-8">
        <div class="flex flex-wrap items-center gap-3 mb-4">
          <span class="text-xs px-2.5 py-1 rounded-full capitalize" :class="categoryColors[skill.category]">
            {{ skill.category }}
          </span>
          <span class="text-xs px-2.5 py-1 rounded-full" :class="complexityColors[skill.complexity]">
            {{ skill.complexity }}
          </span>
        </div>
        <h1 class="text-3xl font-bold mb-3">{{ skill.name }}</h1>
        <p class="text-lg text-muted-foreground">{{ skill.description }}</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div class="bg-card border border-border rounded-lg p-4">
          <h3 class="text-xs font-medium text-muted-foreground uppercase mb-2">Default Agent</h3>
          <div v-if="agent" class="flex items-center gap-2">
            <Icon :name="agent.icon" class="w-5 h-5" :class="iconColorMap[agent.color]" />
            <div>
              <p class="font-medium text-sm">{{ agent.name }}</p>
              <p class="text-xs text-muted-foreground">{{ agent.role }}</p>
            </div>
          </div>
        </div>
        <div class="bg-card border border-border rounded-lg p-4">
          <h3 class="text-xs font-medium text-muted-foreground uppercase mb-2">Trigger</h3>
          <p class="text-sm font-mono">/{{ skill.slug }}</p>
        </div>
        <div class="bg-card border border-border rounded-lg p-4">
          <h3 class="text-xs font-medium text-muted-foreground uppercase mb-2">Tags</h3>
          <div class="flex flex-wrap gap-1">
            <span v-for="tag in skill.tags" :key="tag" class="text-xs px-2 py-0.5 rounded bg-muted text-muted-foreground">
              {{ tag }}
            </span>
          </div>
        </div>
      </div>

      <div class="bg-card border border-border rounded-lg p-6 mb-8">
        <h2 class="text-lg font-semibold mb-4">How This Skill Works</h2>
        <ol class="space-y-3 text-sm text-muted-foreground">
          <li class="flex items-start gap-3">
            <span class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold shrink-0">1</span>
            <span><strong class="text-foreground">Gather context</strong> — Collect relevant inputs and current state from your project</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold shrink-0">2</span>
            <span><strong class="text-foreground">Analyze</strong> — Identify the driver, tension, and constraints using Sociocracy 3.0</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold shrink-0">3</span>
            <span><strong class="text-foreground">Execute</strong> — Perform the core task with quality checks</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold shrink-0">4</span>
            <span><strong class="text-foreground">Verify</strong> — Ensure output meets standards before marking complete</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold shrink-0">5</span>
            <span><strong class="text-foreground">Report</strong> — Summarize what was done and create follow-up items</span>
          </li>
        </ol>
      </div>

      <div class="flex gap-4">
        <NuxtLink
          to="/guide/getting-started"
          class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-primary text-primary-foreground text-sm font-medium hover:opacity-90 transition-opacity"
        >
          <Icon name="lucide:rocket" class="w-4 h-4" />
          Get Started
        </NuxtLink>
        <NuxtLink
          to="/skills"
          class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg border border-border text-sm hover:bg-muted transition-colors"
        >
          Browse More Skills
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
