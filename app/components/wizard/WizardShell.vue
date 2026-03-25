<script setup lang="ts">
import { useWizardStore } from '~/stores/wizard'

const store = useWizardStore()
const route = useRoute()
const router = useRouter()

const totalSteps = 7

const stepParam = computed(() => {
  const s = Number(route.query.step) || 1
  return Math.max(1, Math.min(totalSteps, s))
})

watch(stepParam, (val) => {
  store.setStep(val)
}, { immediate: true })

function goToStep(step: number) {
  router.push({ path: '/onboard', query: { step: String(step) } })
}

const stepLabels = [
  'Mission & Vision',
  'Projects',
  'Pain Points',
  'Recommendations',
  'Customize',
  'Skills',
  'Generate',
]

const progressPercentage = computed(() => (stepParam.value / totalSteps) * 100)
</script>

<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
    <div class="mb-8">
      <div class="flex items-center justify-between mb-2">
        <span class="text-sm text-muted-foreground">
          Step {{ stepParam }} of {{ totalSteps }}:
          <span class="text-foreground font-medium">{{ stepLabels[stepParam - 1] }}</span>
        </span>
        <span class="text-sm text-muted-foreground">
          {{ Math.round(progressPercentage) }}%
        </span>
      </div>
      <div class="w-full h-2 bg-muted rounded-full overflow-hidden">
        <div
          class="h-full bg-primary rounded-full transition-all duration-500 ease-out"
          :style="{ width: `${progressPercentage}%` }"
        />
      </div>
      <div class="flex justify-between mt-2">
        <button
          v-for="(label, i) in stepLabels"
          :key="i"
          class="text-xs hidden sm:block transition-colors"
          :class="i + 1 <= stepParam ? 'text-primary' : 'text-muted-foreground/50'"
          @click="i + 1 <= stepParam ? goToStep(i + 1) : null"
        >
          {{ label }}
        </button>
      </div>
    </div>

    <WizardStepMission v-if="stepParam === 1" />
    <WizardStepProjects v-else-if="stepParam === 2" />
    <WizardStepPainPoints v-else-if="stepParam === 3" />
    <WizardStepRecommendation v-else-if="stepParam === 4" />
    <WizardStepCustomize v-else-if="stepParam === 5" />
    <WizardStepSkills v-else-if="stepParam === 6" />
    <WizardStepGenerate v-else-if="stepParam === 7" />

    <WizardWizardNav
      :step="stepParam"
      :total-steps="totalSteps"
      :can-proceed="store.isStepValid(stepParam)"
      @back="goToStep(stepParam - 1)"
      @next="goToStep(stepParam + 1)"
    />
  </div>
</template>
