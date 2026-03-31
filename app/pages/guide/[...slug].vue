<script setup lang="ts">
definePageMeta({
  layout: 'guide',
})

const route = useRoute()
const slug = computed(() => {
  const parts = route.params.slug as string[]
  return parts?.length ? parts.join('/') : 'index'
})

const { data: page } = await useAsyncData(
  `guide-${slug.value}`,
  () => queryCollection('guide').path(`/guide/${slug.value}`).first()
)

if (page.value) {
  useHead({
    title: `${page.value.title} — AI Cabinet Guide`,
  })
}
</script>

<template>
  <div>
    <div v-if="page" class="guide-content">
      <h1 class="text-3xl font-bold mb-2">{{ page.title }}</h1>
      <p v-if="page.description" class="text-lg text-muted-foreground mb-8">{{ page.description }}</p>
      <div class="prose-custom">
        <ContentRenderer :value="page" />
      </div>
    </div>
    <div v-else class="text-center py-10">
      <h1 class="text-2xl font-bold mb-2">Page Not Found</h1>
      <p class="text-muted-foreground mb-6">This guide page doesn't exist yet.</p>
      <NuxtLink to="/guide" class="text-primary hover:underline">Back to Guide</NuxtLink>
    </div>
  </div>
</template>
