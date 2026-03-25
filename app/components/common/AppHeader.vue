<script setup lang="ts">
const mobileMenuOpen = ref(false)
</script>

<template>
  <header class="border-b border-border bg-background/80 backdrop-blur-sm sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <NuxtLink to="/" class="flex items-center gap-2">
          <Icon name="lucide:brain-circuit" class="w-7 h-7 text-primary" />
          <span class="text-lg font-bold">AI Cabinet</span>
        </NuxtLink>

        <nav class="hidden md:flex items-center gap-6">
          <NuxtLink
            to="/"
            class="text-sm text-muted-foreground hover:text-foreground transition-colors"
            active-class="text-foreground font-medium"
          >
            Home
          </NuxtLink>
          <NuxtLink
            to="/guide"
            class="text-sm text-muted-foreground hover:text-foreground transition-colors"
            active-class="text-foreground font-medium"
          >
            Guide
          </NuxtLink>
          <NuxtLink
            to="/skills"
            class="text-sm text-muted-foreground hover:text-foreground transition-colors"
            active-class="text-foreground font-medium"
          >
            Skills
          </NuxtLink>
          <CommonThemeToggle />
          <NuxtLink
            to="/onboard"
            class="inline-flex items-center gap-2 px-4 py-2 rounded-md bg-primary text-primary-foreground text-sm font-medium hover:opacity-90 transition-opacity"
          >
            <Icon name="lucide:rocket" class="w-4 h-4" />
            Get Started
          </NuxtLink>
        </nav>

        <button
          class="md:hidden p-2"
          @click="mobileMenuOpen = !mobileMenuOpen"
        >
          <Icon :name="mobileMenuOpen ? 'lucide:x' : 'lucide:menu'" class="w-6 h-6" />
        </button>
      </div>

      <div v-if="mobileMenuOpen" class="md:hidden pb-4 space-y-2">
        <NuxtLink
          to="/"
          class="block px-3 py-2 text-sm hover:bg-muted rounded-md"
          @click="mobileMenuOpen = false"
        >
          Home
        </NuxtLink>
        <NuxtLink
          to="/guide"
          class="block px-3 py-2 text-sm hover:bg-muted rounded-md"
          @click="mobileMenuOpen = false"
        >
          Guide
        </NuxtLink>
        <NuxtLink
          to="/skills"
          class="block px-3 py-2 text-sm hover:bg-muted rounded-md"
          @click="mobileMenuOpen = false"
        >
          Skills
        </NuxtLink>
        <div class="flex items-center gap-3 px-3 py-2">
          <CommonThemeToggle />
          <NuxtLink
            to="/onboard"
            class="inline-flex items-center gap-2 px-4 py-2 rounded-md bg-primary text-primary-foreground text-sm font-medium"
            @click="mobileMenuOpen = false"
          >
            Get Started
          </NuxtLink>
        </div>
      </div>
    </div>
  </header>
</template>
