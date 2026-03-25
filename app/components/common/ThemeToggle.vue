<script setup lang="ts">
const colorMode = useColorMode()

function toggleTheme() {
  colorMode.preference = colorMode.value === 'dark' ? 'light' : 'dark'
}
</script>

<template>
  <button
    class="p-2 rounded-md hover:bg-muted transition-colors"
    aria-label="Toggle theme"
    @click="toggleTheme"
  >
    <Icon
      :name="colorMode.value === 'dark' ? 'lucide:sun' : 'lucide:moon'"
      class="w-5 h-5"
    />
  </button>
</template>
