<template>
  <div class="min-h-screen flex flex-col bg-background text-foreground">
    <CommonAppHeader />
    <div class="flex-1 flex">
      <aside class="hidden md:block w-64 border-r border-border p-6">
        <nav class="space-y-1">
          <h3 class="text-sm font-semibold text-muted-foreground uppercase tracking-wider mb-3">
            Guide
          </h3>
          <NuxtLink
            to="/guide"
            class="block px-3 py-2 rounded-md text-sm hover:bg-muted transition-colors"
            active-class="bg-muted text-primary font-medium"
          >
            Overview
          </NuxtLink>
          <NuxtLink
            to="/guide/getting-started"
            class="block px-3 py-2 rounded-md text-sm hover:bg-muted transition-colors"
            active-class="bg-muted text-primary font-medium"
          >
            Getting Started
          </NuxtLink>
          <NuxtLink
            to="/guide/agents"
            class="block px-3 py-2 rounded-md text-sm hover:bg-muted transition-colors"
            active-class="bg-muted text-primary font-medium"
          >
            Understanding Agents
          </NuxtLink>
          <NuxtLink
            to="/guide/skills"
            class="block px-3 py-2 rounded-md text-sm hover:bg-muted transition-colors"
            active-class="bg-muted text-primary font-medium"
          >
            Skills System
          </NuxtLink>
          <NuxtLink
            to="/guide/s3-governance"
            class="block px-3 py-2 rounded-md text-sm hover:bg-muted transition-colors"
            active-class="bg-muted text-primary font-medium"
          >
            S3 Governance
          </NuxtLink>
          <NuxtLink
            to="/guide/customization"
            class="block px-3 py-2 rounded-md text-sm hover:bg-muted transition-colors"
            active-class="bg-muted text-primary font-medium"
          >
            Customization
          </NuxtLink>
        </nav>
      </aside>
      <main class="flex-1 max-w-4xl mx-auto px-6 py-10">
        <slot />
      </main>
    </div>
    <CommonAppFooter />
  </div>
</template>
