<script setup lang="ts">
import { useWizardStore } from '~/stores/wizard'

const store = useWizardStore()
</script>

<template>
  <div class="space-y-8">
    <div>
      <h2 class="text-2xl font-bold mb-2">Define Your Mission & Vision</h2>
      <p class="text-muted-foreground">
        What drives you? Your mission and vision help your agents understand your goals and
        make aligned decisions.
      </p>
    </div>

    <div class="space-y-6">
      <div>
        <label class="block text-sm font-medium mb-2" for="mission">
          Mission
          <span class="text-muted-foreground font-normal ml-1">
            (What you are building and why)
          </span>
        </label>
        <textarea
          id="mission"
          :value="store.mission"
          class="w-full min-h-[120px] px-4 py-3 rounded-lg bg-muted border border-input text-foreground placeholder:text-muted-foreground/50 focus:ring-2 focus:ring-ring focus:border-transparent outline-none resize-y"
          placeholder="e.g., Create tools and knowledge that help indie founders build sustainable businesses — products people pay for, lessons people learn from."
          @input="store.setMission(($event.target as HTMLTextAreaElement).value)"
        />
        <p class="mt-1 text-xs text-muted-foreground">
          {{ store.mission.length }} characters
          <span v-if="store.mission.length > 0 && store.mission.length < 11" class="text-destructive">
            (minimum 11 characters)
          </span>
        </p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-2" for="vision">
          Vision
          <span class="text-muted-foreground font-normal ml-1">
            (Where you want to be in 3-5 years)
          </span>
        </label>
        <textarea
          id="vision"
          :value="store.vision"
          class="w-full min-h-[120px] px-4 py-3 rounded-lg bg-muted border border-input text-foreground placeholder:text-muted-foreground/50 focus:ring-2 focus:ring-ring focus:border-transparent outline-none resize-y"
          placeholder="e.g., Financially independent through my own products, free to choose what to work on, where to be, and what legacy to leave."
          @input="store.setVision(($event.target as HTMLTextAreaElement).value)"
        />
      </div>
    </div>
  </div>
</template>
