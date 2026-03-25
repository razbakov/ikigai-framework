<script setup lang="ts">
definePageMeta({
  layout: 'guide',
})

const route = useRoute()

useHead({
  title: 'Guide — AI Cabinet',
})
</script>

<template>
  <div class="prose prose-invert max-w-none">
    <ContentDoc :path="`/guide/${(route.params.slug as string[])?.join('/') || 'index'}`">
      <template #not-found>
        <div class="text-center py-10">
          <Icon name="lucide:file-question" class="w-12 h-12 mx-auto mb-4 text-muted-foreground" />
          <h1 class="text-2xl font-bold mb-2">Page Not Found</h1>
          <p class="text-muted-foreground mb-6">This guide page doesn't exist yet.</p>
          <NuxtLink to="/guide" class="text-primary hover:underline">Back to Guide</NuxtLink>
        </div>
      </template>
    </ContentDoc>
  </div>
</template>
