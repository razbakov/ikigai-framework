<script setup lang="ts">
const systems = [
  {
    name: 'Ikigai',
    description: 'Find your purpose. Delegate everything else. The team exists so you can focus on what only you can do.',
    icon: 'lucide:compass',
    color: 'text-purple-500',
  },
  {
    name: 'GTD',
    description: 'Inbox processing, next actions, weekly reviews. Maya runs Getting Things Done so nothing slips through.',
    icon: 'lucide:inbox',
    color: 'text-cyan-500',
  },
  {
    name: 'OKRs',
    description: 'Quarterly objectives cascade to every agent. Marco tracks progress and challenges anything that does not move the needle.',
    icon: 'lucide:target',
    color: 'text-yellow-500',
  },
  {
    name: 'Level 10 Life',
    description: 'Score 10 life areas, track trends, catch burnout early. Sage runs assessments so you stay sustainable.',
    icon: 'lucide:heart-pulse',
    color: 'text-green-500',
  },
  {
    name: 'Sociocracy 3.0',
    description: 'Clear domains, consent-based decisions, decision authority matrix. Every agent knows their boundaries and who to hand off to.',
    icon: 'lucide:git-branch',
    color: 'text-blue-500',
  },
  {
    name: 'CRM',
    description: 'Meet someone, send a screenshot. Kai researches them, enriches the profile, and tracks follow-ups automatically.',
    icon: 'lucide:users',
    color: 'text-orange-500',
  },
]
</script>

<template>
  <section class="py-20 bg-muted/30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold">Not Just Agents. A System.</h2>
        <p class="mt-3 text-lg text-muted-foreground max-w-2xl mx-auto">
          Every methodology is already wired in. You do not have to learn it, configure it,
          or stitch tools together. Just use it.
        </p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="system in systems"
          :key="system.name"
          class="bg-card border border-border rounded-xl p-6 hover:border-primary/30 transition-colors"
        >
          <div class="flex items-center gap-3 mb-3">
            <Icon :name="system.icon" class="w-6 h-6" :class="system.color" />
            <h3 class="text-lg font-semibold">{{ system.name }}</h3>
          </div>
          <p class="text-sm text-muted-foreground">{{ system.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
