<script setup lang="ts">
import type { SkillEntry } from '~/types/skill'

defineProps<{
  skills: SkillEntry[]
}>()
</script>

<template>
  <div>
    <div v-if="skills.length === 0" class="text-center py-12 text-muted-foreground">
      <Icon name="lucide:search-x" class="w-10 h-10 mx-auto mb-3 opacity-50" />
      <p>No skills match your filters.</p>
    </div>
    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <SkillsSkillCard
        v-for="skill in skills"
        :key="skill.slug"
        :skill="skill"
      />
    </div>
  </div>
</template>
