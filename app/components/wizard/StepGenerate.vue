<script setup lang="ts">
import { useWizardStore } from '~/stores/wizard'
import { getFileList, packageFiles } from '~/utils/file-packager'

const store = useWizardStore()
const isGenerating = ref(false)

const files = computed(() => getFileList(store.getState()))

const enabledAgentCount = computed(() => store.agents.filter(a => a.enabled).length)

const totalSkillCount = computed(() => {
  let count = 0
  for (const agentId in store.selectedSkills) {
    count += store.selectedSkills[agentId].length
  }
  return count
})

async function download() {
  isGenerating.value = true
  try {
    await packageFiles(store.getState())
  } finally {
    isGenerating.value = false
  }
}
</script>

<template>
  <div class="space-y-8">
    <div>
      <h2 class="text-2xl font-bold mb-2">Generate Your Configuration</h2>
      <p class="text-muted-foreground">
        Review what will be generated, then download your AI Cabinet configuration as a ZIP file.
      </p>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
      <div class="bg-card border border-border rounded-lg p-4 text-center">
        <div class="text-3xl font-bold text-primary">{{ enabledAgentCount }}</div>
        <div class="text-sm text-muted-foreground">Agents</div>
      </div>
      <div class="bg-card border border-border rounded-lg p-4 text-center">
        <div class="text-3xl font-bold text-primary">{{ totalSkillCount }}</div>
        <div class="text-sm text-muted-foreground">Skills</div>
      </div>
      <div class="bg-card border border-border rounded-lg p-4 text-center">
        <div class="text-3xl font-bold text-primary">{{ files.length }}</div>
        <div class="text-sm text-muted-foreground">Files</div>
      </div>
    </div>

    <div class="bg-card border border-border rounded-lg overflow-hidden">
      <div class="px-4 py-3 bg-muted/50 border-b border-border">
        <h3 class="text-sm font-medium">Files to generate</h3>
      </div>
      <div class="p-4">
        <ul class="space-y-1.5">
          <li
            v-for="file in files"
            :key="file"
            class="flex items-center gap-2 text-sm font-mono"
          >
            <Icon name="lucide:file-text" class="w-4 h-4 text-muted-foreground shrink-0" />
            <span class="text-muted-foreground">{{ file }}</span>
          </li>
        </ul>
      </div>
    </div>

    <div class="flex flex-col items-center gap-4">
      <button
        class="inline-flex items-center gap-2 px-8 py-4 rounded-lg bg-primary text-primary-foreground font-medium text-lg hover:opacity-90 transition-opacity disabled:opacity-50"
        :disabled="isGenerating"
        @click="download"
      >
        <Icon :name="isGenerating ? 'lucide:loader-2' : 'lucide:download'" class="w-5 h-5" :class="isGenerating ? 'animate-spin' : ''" />
        {{ isGenerating ? 'Generating...' : 'Download ZIP' }}
      </button>
    </div>

    <div class="bg-card border border-border rounded-lg p-6">
      <h3 class="font-semibold mb-4 flex items-center gap-2">
        <Icon name="lucide:book-open" class="w-5 h-5 text-primary" />
        What's Next?
      </h3>
      <ol class="space-y-3 text-sm text-muted-foreground">
        <li class="flex items-start gap-3">
          <span class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold shrink-0">1</span>
          <span>Extract the ZIP into your project root</span>
        </li>
        <li class="flex items-start gap-3">
          <span class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold shrink-0">2</span>
          <span>Open Claude Code and start a session in your project</span>
        </li>
        <li class="flex items-start gap-3">
          <span class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold shrink-0">3</span>
          <span>Reference your agent team: "Ask Maya to run the daily review"</span>
        </li>
        <li class="flex items-start gap-3">
          <span class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold shrink-0">4</span>
          <span>
            Read the
            <NuxtLink to="/guide/getting-started" class="text-primary hover:underline">
              Getting Started guide
            </NuxtLink>
            for detailed setup instructions
          </span>
        </li>
      </ol>
    </div>
  </div>
</template>
