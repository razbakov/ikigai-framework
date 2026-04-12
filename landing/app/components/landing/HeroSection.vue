<script setup lang="ts">
const { t } = useI18n()
const starterPrompt = 'Set up my Ikigai Team using https://github.com/razbakov/ikigai-team'
const copied = ref(false)

type Harness = {
  id: string
  name: string
  launchLabel: string
  logoKind: 'icon' | 'monogram'
  logo?: string
  monogram?: string
}

const harnesses: Harness[] = [
  {
    id: 'claude-code',
    name: 'Claude Code',
    launchLabel: 'Open Claude Code',
    logoKind: 'icon',
    logo: 'simple-icons:claude',
  },
  {
    id: 'cursor',
    name: 'Cursor',
    launchLabel: 'Open Cursor Chat or Agent',
    logoKind: 'icon',
    logo: 'simple-icons:cursor',
  },
  {
    id: 'codex',
    name: 'Codex',
    launchLabel: 'Open Codex',
    logoKind: 'icon',
    logo: 'simple-icons:openai',
  },
  {
    id: 'antigravity',
    name: 'AntiGravity',
    launchLabel: 'Open AntiGravity',
    logoKind: 'monogram',
    monogram: 'AG',
  },
  {
    id: 'chatgpt',
    name: 'ChatGPT',
    launchLabel: 'Open ChatGPT',
    logoKind: 'icon',
    logo: 'simple-icons:openai',
  },
  {
    id: 'cline',
    name: 'Cline',
    launchLabel: 'Open Cline',
    logoKind: 'icon',
    logo: 'simple-icons:cline',
  },
  {
    id: 'windsurf',
    name: 'Windsurf',
    launchLabel: 'Open Windsurf',
    logoKind: 'icon',
    logo: 'simple-icons:windsurf',
  },
  {
    id: 'continue',
    name: 'Continue',
    launchLabel: 'Open Continue',
    logoKind: 'monogram',
    monogram: 'Co',
  },
  {
    id: 'aider',
    name: 'Aider',
    launchLabel: 'Open Aider',
    logoKind: 'monogram',
    monogram: 'Ai',
  },
  {
    id: 'gemini-cli',
    name: 'Gemini CLI',
    launchLabel: 'Open Gemini CLI',
    logoKind: 'icon',
    logo: 'simple-icons:googlegemini',
  },
  {
    id: 'opencode',
    name: 'OpenCode',
    launchLabel: 'Open OpenCode',
    logoKind: 'monogram',
    monogram: 'Op',
  },
]

const selectedHarnessId = ref(harnesses[0]!.id)
const selectedHarness = computed(
  () => harnesses.find(h => h.id === selectedHarnessId.value) ?? harnesses[0]!,
)

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
          {{ t('hero.title') }}
          <span class="text-primary">{{ t('hero.titleHighlight') }}</span>
        </h1>
        <p class="mt-6 text-lg text-muted-foreground max-w-2xl mx-auto">
          {{ t('hero.subtitle') }}
        </p>

        <div class="mt-8 max-w-4xl mx-auto text-left">
          <div class="relative">
            <div class="pointer-events-none absolute inset-y-0 left-0 w-8 bg-gradient-to-r from-background via-background/85 to-transparent z-10" />
            <div class="pointer-events-none absolute inset-y-0 right-0 w-8 bg-gradient-to-l from-background via-background/85 to-transparent z-10" />
            <div
              class="overflow-x-auto px-6 pb-2 [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden"
              :aria-label="t('hero.ariaTools')"
            >
              <div class="flex min-w-max flex-nowrap justify-start gap-2">
                <button
                  v-for="harness in harnesses"
                  :key="harness.id"
                  type="button"
                  class="inline-flex shrink-0 items-center gap-2 whitespace-nowrap rounded-full border px-3 py-2 text-sm font-medium transition-colors"
                  :class="selectedHarnessId === harness.id
                    ? 'border-primary bg-primary text-primary-foreground'
                    : 'border-border bg-card/80 text-foreground hover:border-primary/50'"
                  @click="selectedHarnessId = harness.id"
                >
                  <Icon
                    v-if="harness.logoKind === 'icon' && harness.logo"
                    :name="harness.logo"
                    class="h-4 w-4 shrink-0"
                  />
                  <span
                    v-else
                    class="inline-flex h-5 min-w-5 items-center justify-center rounded-full border border-current/25 px-1 text-[10px] font-bold uppercase leading-none"
                  >
                    {{ harness.monogram }}
                  </span>
                  {{ harness.name }}
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-8 max-w-2xl mx-auto rounded-2xl border border-border bg-background/80 text-left shadow-lg backdrop-blur">
          <div class="flex items-center justify-between gap-4 border-b border-border px-4 py-3">
            <div>
              <p class="text-sm font-medium">1. {{ selectedHarness.launchLabel }}</p>
              <p class="text-sm text-muted-foreground">{{ t('hero.step2') }}</p>
            </div>
            <button
              type="button"
              class="inline-flex items-center gap-2 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:opacity-90 transition-opacity"
              @click="copyPrompt"
            >
              <Icon :name="copied ? 'lucide:check' : 'lucide:copy'" class="h-4 w-4" />
              {{ copied ? t('hero.copied') : t('hero.copyPrompt') }}
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
          :alt="t('hero.heroAlt')"
          class="rounded-xl shadow-2xl border border-border"
        />
      </div>
    </div>
  </section>
</template>
