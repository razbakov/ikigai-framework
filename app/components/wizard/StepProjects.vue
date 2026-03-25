<script setup lang="ts">
import { useWizardStore } from '~/stores/wizard'

const store = useWizardStore()
</script>

<template>
  <div class="space-y-8">
    <div>
      <h2 class="text-2xl font-bold mb-2">Your Projects</h2>
      <p class="text-muted-foreground">
        List the projects your agents will work on. This helps them understand your technical
        landscape and assign responsibilities.
      </p>
    </div>

    <div class="space-y-4">
      <div
        v-for="(project, index) in store.projects"
        :key="index"
        class="p-4 bg-card border border-border rounded-lg space-y-3"
      >
        <div class="flex items-center justify-between">
          <span class="text-sm font-medium text-muted-foreground">
            Project {{ index + 1 }}
          </span>
          <button
            v-if="store.projects.length > 1"
            class="p-1 rounded hover:bg-destructive/10 text-muted-foreground hover:text-destructive transition-colors"
            @click="store.removeProject(index)"
          >
            <Icon name="lucide:trash-2" class="w-4 h-4" />
          </button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <input
            v-model="project.name"
            type="text"
            placeholder="Project name"
            class="px-3 py-2 rounded-md bg-muted border border-input text-foreground placeholder:text-muted-foreground/50 focus:ring-2 focus:ring-ring outline-none text-sm"
          >
          <input
            v-model="project.description"
            type="text"
            placeholder="Short description"
            class="px-3 py-2 rounded-md bg-muted border border-input text-foreground placeholder:text-muted-foreground/50 focus:ring-2 focus:ring-ring outline-none text-sm"
          >
          <input
            v-model="project.techStack"
            type="text"
            placeholder="Tech stack (e.g., Nuxt, React)"
            class="px-3 py-2 rounded-md bg-muted border border-input text-foreground placeholder:text-muted-foreground/50 focus:ring-2 focus:ring-ring outline-none text-sm"
          >
        </div>
      </div>

      <button
        v-if="store.projects.length < 5"
        class="inline-flex items-center gap-2 px-4 py-2 rounded-lg border border-dashed border-border hover:bg-muted transition-colors text-sm text-muted-foreground"
        @click="store.addProject()"
      >
        <Icon name="lucide:plus" class="w-4 h-4" />
        Add Project
      </button>
    </div>
  </div>
</template>
