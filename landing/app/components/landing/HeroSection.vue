<script setup lang="ts">
const starterPrompt = 'Set up my Ikigai Team using https://github.com/razbakov/ikigai-team'
const copied = ref(false)

async function copyPrompt() {
  await navigator.clipboard.writeText(starterPrompt)
  copied.value = true

  setTimeout(() => {
    copied.value = false
  }, 2000)
}
</script>

<template>
  <section class="relative overflow-hidden py-20 sm:py-32">
    <div class="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent" />
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight">
          Your AI
          <span class="text-primary">Dream Team</span>
        </h1>
        <p class="mt-6 text-lg text-muted-foreground max-w-2xl mx-auto">
          Open Claude Code on Desktop, paste this message, and start. No setup wizard,
          no docs detour, no extra decisions.
        </p>

        <div class="mt-8 max-w-2xl mx-auto rounded-2xl border border-border bg-background/80 text-left shadow-lg backdrop-blur">
          <div class="flex items-center justify-between gap-4 border-b border-border px-4 py-3">
            <div>
              <p class="text-sm font-medium">1. Open Claude Code on Desktop</p>
              <p class="text-sm text-muted-foreground">2. Paste this prompt</p>
            </div>
            <button
              type="button"
              class="inline-flex items-center gap-2 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:opacity-90 transition-opacity"
              @click="copyPrompt"
            >
              <Icon :name="copied ? 'lucide:check' : 'lucide:copy'" class="h-4 w-4" />
              {{ copied ? 'Copied' : 'Copy prompt' }}
            </button>
          </div>

          <div class="px-4 py-4">
            <pre class="whitespace-pre-wrap break-words text-sm sm:text-base leading-7 text-foreground font-mono">{{ starterPrompt }}</pre>
          </div>
        </div>
      </div>

      <div class="max-w-4xl mx-auto">
        <img
          src="/hero-team.png"
          alt="Meet the Ikigai Team — Maya, Viktor, Luna, Alex, Marco, Sage, and Kai"
          class="rounded-xl shadow-2xl border border-border"
        />
      </div>
    </div>
  </section>
</template>
