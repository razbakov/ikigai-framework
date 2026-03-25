<script setup lang="ts">
import { AGENTS } from '~/types/agent'
</script>

<template>
  <section class="py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold">Meet Your Team</h2>
        <p class="mt-3 text-lg text-muted-foreground max-w-2xl mx-auto">
          Six specialized agents, each with their own expertise and personality. Pick the ones you need.
        </p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <LandingAgentCard
          v-for="agent in AGENTS"
          :key="agent.id"
          :agent="agent"
        />
      </div>
    </div>
  </section>
</template>
