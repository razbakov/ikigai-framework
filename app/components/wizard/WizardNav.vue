<script setup lang="ts">
const props = defineProps<{
  step: number
  totalSteps: number
  canProceed: boolean
}>()

const emit = defineEmits<{
  back: []
  next: []
}>()
</script>

<template>
  <div class="flex items-center justify-between mt-10 pt-6 border-t border-border">
    <button
      v-if="props.step > 1"
      class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg border border-border hover:bg-muted transition-colors text-sm"
      @click="emit('back')"
    >
      <Icon name="lucide:arrow-left" class="w-4 h-4" />
      Back
    </button>
    <div v-else />

    <button
      v-if="props.step < props.totalSteps"
      class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-sm font-medium transition-all"
      :class="props.canProceed
        ? 'bg-primary text-primary-foreground hover:opacity-90'
        : 'bg-muted text-muted-foreground cursor-not-allowed'"
      :disabled="!props.canProceed"
      @click="props.canProceed && emit('next')"
    >
      Next
      <Icon name="lucide:arrow-right" class="w-4 h-4" />
    </button>
  </div>
</template>
