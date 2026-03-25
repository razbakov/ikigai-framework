<script setup lang="ts">
import { AGENTS } from '~/types/agent'

const props = defineProps<{
  modelValue: {
    search: string
    categories: string[]
    agents: string[]
    complexity: string
  }
}>()

const emit = defineEmits<{
  'update:modelValue': [value: typeof props.modelValue]
}>()

const categories = [
  { id: 'operations', label: 'Operations' },
  { id: 'engineering', label: 'Engineering' },
  { id: 'content', label: 'Content' },
  { id: 'strategy', label: 'Strategy' },
  { id: 'personal', label: 'Personal' },
  { id: 'community', label: 'Community' },
]

const complexities = [
  { id: '', label: 'All' },
  { id: 'simple', label: 'Simple' },
  { id: 'moderate', label: 'Moderate' },
  { id: 'advanced', label: 'Advanced' },
]

function updateSearch(value: string) {
  emit('update:modelValue', { ...props.modelValue, search: value })
}

function toggleCategory(id: string) {
  const cats = [...props.modelValue.categories]
  const idx = cats.indexOf(id)
  if (idx === -1) {
    cats.push(id)
  } else {
    cats.splice(idx, 1)
  }
  emit('update:modelValue', { ...props.modelValue, categories: cats })
}

function toggleAgent(id: string) {
  const ag = [...props.modelValue.agents]
  const idx = ag.indexOf(id)
  if (idx === -1) {
    ag.push(id)
  } else {
    ag.splice(idx, 1)
  }
  emit('update:modelValue', { ...props.modelValue, agents: ag })
}

function setComplexity(value: string) {
  emit('update:modelValue', { ...props.modelValue, complexity: value })
}
</script>

<template>
  <div class="space-y-6">
    <div>
      <label class="block text-sm font-medium mb-2">Search</label>
      <div class="relative">
        <Icon name="lucide:search" class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
        <input
          :value="props.modelValue.search"
          type="text"
          placeholder="Filter skills..."
          class="w-full pl-10 pr-4 py-2 rounded-md bg-muted border border-input text-sm focus:ring-2 focus:ring-ring outline-none"
          @input="updateSearch(($event.target as HTMLInputElement).value)"
        >
      </div>
    </div>

    <div>
      <h3 class="text-sm font-medium mb-2">Category</h3>
      <div class="space-y-1">
        <button
          v-for="cat in categories"
          :key="cat.id"
          class="flex items-center gap-2 w-full px-3 py-1.5 rounded text-sm transition-colors"
          :class="props.modelValue.categories.includes(cat.id) ? 'bg-primary/10 text-primary' : 'hover:bg-muted text-muted-foreground'"
          @click="toggleCategory(cat.id)"
        >
          <div
            class="w-4 h-4 rounded border flex items-center justify-center"
            :class="props.modelValue.categories.includes(cat.id) ? 'border-primary bg-primary' : 'border-muted-foreground/30'"
          >
            <Icon v-if="props.modelValue.categories.includes(cat.id)" name="lucide:check" class="w-3 h-3 text-primary-foreground" />
          </div>
          {{ cat.label }}
        </button>
      </div>
    </div>

    <div>
      <h3 class="text-sm font-medium mb-2">Agent</h3>
      <div class="space-y-1">
        <button
          v-for="agent in AGENTS"
          :key="agent.id"
          class="flex items-center gap-2 w-full px-3 py-1.5 rounded text-sm transition-colors"
          :class="props.modelValue.agents.includes(agent.id) ? 'bg-primary/10 text-primary' : 'hover:bg-muted text-muted-foreground'"
          @click="toggleAgent(agent.id)"
        >
          <div
            class="w-4 h-4 rounded border flex items-center justify-center"
            :class="props.modelValue.agents.includes(agent.id) ? 'border-primary bg-primary' : 'border-muted-foreground/30'"
          >
            <Icon v-if="props.modelValue.agents.includes(agent.id)" name="lucide:check" class="w-3 h-3 text-primary-foreground" />
          </div>
          <Icon :name="agent.icon" class="w-3.5 h-3.5" />
          {{ agent.name }}
        </button>
      </div>
    </div>

    <div>
      <h3 class="text-sm font-medium mb-2">Complexity</h3>
      <div class="space-y-1">
        <button
          v-for="c in complexities"
          :key="c.id"
          class="flex items-center gap-2 w-full px-3 py-1.5 rounded text-sm transition-colors"
          :class="props.modelValue.complexity === c.id ? 'bg-primary/10 text-primary' : 'hover:bg-muted text-muted-foreground'"
          @click="setComplexity(c.id)"
        >
          <div
            class="w-4 h-4 rounded-full border flex items-center justify-center"
            :class="props.modelValue.complexity === c.id ? 'border-primary' : 'border-muted-foreground/30'"
          >
            <div v-if="props.modelValue.complexity === c.id" class="w-2 h-2 rounded-full bg-primary" />
          </div>
          {{ c.label }}
        </button>
      </div>
    </div>
  </div>
</template>
