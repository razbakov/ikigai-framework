<script setup lang="ts">
definePageMeta({
  layout: 'guide',
})

useHead({
  title: 'Guide — Ikigai Team',
  meta: [
    { name: 'description', content: 'Learn how to set up and use your Ikigai Team — from understanding agents to deploying skills.' },
  ],
})

const sections = [
  {
    title: 'Getting Started',
    description: 'Set up your Ikigai Team configuration and deploy your first agents.',
    icon: 'lucide:rocket',
    to: '/guide/getting-started',
  },
  {
    title: 'Understanding Agents',
    description: 'Learn how AI agents work, their roles, personalities, and decision-making framework.',
    icon: 'lucide:users',
    to: '/guide/agents',
  },
  {
    title: 'Skills System',
    description: 'Discover how skills work — reusable workflows your agents can execute on demand.',
    icon: 'lucide:zap',
    to: '/guide/skills',
  },
  {
    title: 'S3 Governance',
    description: 'Sociocracy 3.0 patterns for agent domains, drivers, constraints, and decision authority.',
    icon: 'lucide:layers',
    to: '/guide/s3-governance',
  },
  {
    title: 'Customization',
    description: 'Advanced customization: create custom agents, write your own skills, and extend the system.',
    icon: 'lucide:settings',
    to: '/guide/customization',
  },
]
</script>

<template>
  <div>
    <h1 class="text-3xl font-bold mb-3">Ikigai Team Guide</h1>
    <p class="text-lg text-muted-foreground mb-10">
      Everything you need to know about setting up and using your AI executive team.
    </p>

    <div class="grid gap-4">
      <NuxtLink
        v-for="section in sections"
        :key="section.to"
        :to="section.to"
        class="flex items-start gap-4 p-5 bg-card border border-border rounded-lg hover:shadow-md hover:-translate-y-0.5 transition-all"
      >
        <div class="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center shrink-0">
          <Icon :name="section.icon" class="w-5 h-5 text-primary" />
        </div>
        <div>
          <h2 class="font-semibold mb-1">{{ section.title }}</h2>
          <p class="text-sm text-muted-foreground">{{ section.description }}</p>
        </div>
        <Icon name="lucide:chevron-right" class="w-5 h-5 text-muted-foreground ml-auto shrink-0 mt-2.5" />
      </NuxtLink>
    </div>
  </div>
</template>
