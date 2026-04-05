<script setup lang="ts">
import { SKILLS } from '~/types/skill'

useHead({
  title: 'Skills — Ikigai Team',
  meta: [
    { name: 'description', content: 'Browse all available AI agent skills: operations, engineering, content, strategy, personal development, and community management.' },
  ],
})

const filters = ref({
  search: '',
  categories: [] as string[],
  agents: [] as string[],
  complexity: '',
})

const filteredSkills = computed(() => {
  return SKILLS.filter((skill) => {
    const matchesSearch = !filters.value.search
      || skill.name.toLowerCase().includes(filters.value.search.toLowerCase())
      || skill.description.toLowerCase().includes(filters.value.search.toLowerCase())
      || skill.tags.some(t => t.toLowerCase().includes(filters.value.search.toLowerCase()))

    const matchesCategory = filters.value.categories.length === 0
      || filters.value.categories.includes(skill.category)

    const matchesAgent = filters.value.agents.length === 0
      || filters.value.agents.includes(skill.defaultAgent)

    const matchesComplexity = !filters.value.complexity
      || skill.complexity === filters.value.complexity

    return matchesSearch && matchesCategory && matchesAgent && matchesComplexity
  })
})
</script>

<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
    <div class="mb-8">
      <h1 class="text-3xl font-bold">Skills Catalog</h1>
      <p class="mt-2 text-muted-foreground">
        Browse {{ SKILLS.length }} skills across 6 categories. Each skill is a reusable
        workflow your agents can execute.
      </p>
    </div>

    <div class="flex flex-col md:flex-row gap-8">
      <aside class="w-full md:w-64 shrink-0">
        <SkillsSkillFilters v-model="filters" />
      </aside>

      <div class="flex-1">
        <div class="mb-4 text-sm text-muted-foreground">
          Showing {{ filteredSkills.length }} of {{ SKILLS.length }} skills
        </div>
        <SkillsSkillBrowser :skills="filteredSkills" />
      </div>
    </div>
  </div>
</template>
