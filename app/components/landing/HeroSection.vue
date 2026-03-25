<script setup lang="ts">
const terminalLines = [
  { agent: 'Maya', color: 'text-[var(--color-maya)]', text: 'Good morning. 3 items in inbox, 2 meetings today. Your top priority is the product launch.' },
  { agent: 'Viktor', color: 'text-[var(--color-viktor)]', text: 'PR #47 passed all checks. Deploying to staging now.' },
  { agent: 'Luna', color: 'text-[var(--color-luna)]', text: 'Blog post draft ready for review. SEO score: 92/100.' },
  { agent: 'Marco', color: 'text-[var(--color-marco)]', text: 'Q2 OKR progress: 67%. Revenue target needs attention.' },
]

const visibleLines = ref(0)
let interval: ReturnType<typeof setInterval>

onMounted(() => {
  interval = setInterval(() => {
    if (visibleLines.value < terminalLines.length) {
      visibleLines.value++
    } else {
      clearInterval(interval)
    }
  }, 800)
})

onUnmounted(() => {
  clearInterval(interval)
})
</script>

<template>
  <section class="relative overflow-hidden py-20 sm:py-32">
    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent" />
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <div>
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight">
            Your AI
            <span class="text-primary">Executive Team</span>
          </h1>
          <p class="mt-6 text-lg text-muted-foreground max-w-xl">
            Build a team of specialized AI agents that handle operations, engineering,
            content, strategy, personal coaching, and community — so you can focus on
            what matters most.
          </p>
          <div class="mt-8 flex flex-wrap gap-4">
            <NuxtLink
              to="/onboard"
              class="inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-primary text-primary-foreground font-medium hover:opacity-90 transition-opacity"
            >
              <Icon name="lucide:rocket" class="w-5 h-5" />
              Build Your Team
            </NuxtLink>
            <NuxtLink
              to="/guide"
              class="inline-flex items-center gap-2 px-6 py-3 rounded-lg border border-border hover:bg-muted transition-colors"
            >
              <Icon name="lucide:book-open" class="w-5 h-5" />
              Read the Guide
            </NuxtLink>
          </div>
        </div>

        <div class="bg-card border border-border rounded-xl overflow-hidden shadow-2xl">
          <div class="flex items-center gap-2 px-4 py-3 border-b border-border bg-muted/50">
            <div class="w-3 h-3 rounded-full bg-red-500/70" />
            <div class="w-3 h-3 rounded-full bg-yellow-500/70" />
            <div class="w-3 h-3 rounded-full bg-green-500/70" />
            <span class="text-xs text-muted-foreground ml-2 font-mono">ai-cabinet</span>
          </div>
          <div class="p-4 font-mono text-sm space-y-3 min-h-[200px]">
            <div
              v-for="(line, i) in terminalLines"
              :key="i"
              class="transition-all duration-500"
              :class="i < visibleLines ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-2'"
            >
              <span :class="line.color" class="font-bold">{{ line.agent }}:</span>
              <span class="text-foreground/80 ml-2">{{ line.text }}</span>
            </div>
            <div v-if="visibleLines >= terminalLines.length" class="flex items-center gap-1 text-muted-foreground">
              <span class="animate-pulse">_</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
