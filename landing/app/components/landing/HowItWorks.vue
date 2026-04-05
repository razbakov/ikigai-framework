<script setup lang="ts">
const steps = [
  {
    number: '01',
    title: 'Install the Skill',
    description: 'One command installs the setup wizard. No dependencies, no build step.',
    icon: 'lucide:download',
  },
  {
    number: '02',
    title: 'Answer 10 Questions',
    description: 'Name, projects, OKRs, integrations. The wizard generates your full team with all systems wired in.',
    icon: 'lucide:message-circle',
  },
  {
    number: '03',
    title: 'Start Delegating',
    description: 'Talk to Maya. She dispatches to the right agent. GTD, OKRs, reviews, and coaching run automatically.',
    icon: 'lucide:rocket',
  },
]
</script>

<template>
  <section class="py-20 bg-muted/30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold">How It Works</h2>
        <p class="mt-3 text-lg text-muted-foreground">
          Three steps to your AI-powered executive team.
        </p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div
          v-for="(step, index) in steps"
          :key="step.number"
          class="relative text-center"
        >
          <div v-if="index < steps.length - 1" class="hidden md:block absolute top-12 left-[60%] w-[80%] h-px bg-border" />
          <div class="w-24 h-24 mx-auto rounded-2xl bg-primary/10 flex items-center justify-center mb-6">
            <Icon :name="step.icon" class="w-10 h-10 text-primary" />
          </div>
          <span class="text-xs font-mono text-muted-foreground">STEP {{ step.number }}</span>
          <h3 class="text-xl font-semibold mt-2 mb-3">{{ step.title }}</h3>
          <p class="text-sm text-muted-foreground max-w-xs mx-auto">{{ step.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
