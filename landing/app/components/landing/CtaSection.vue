<template>
  <section class="py-20 bg-gradient-to-b from-transparent to-primary/5">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <Icon name="lucide:compass" class="w-12 h-12 text-primary mx-auto mb-6" />
      <h2 class="text-3xl sm:text-4xl font-bold mb-4">
        Ready to Meet Your Team?
      </h2>
      <p class="text-lg text-muted-foreground mb-8 max-w-xl mx-auto">
        One command sets up 6 agents with GTD, OKRs, coaching, and governance.
        You walk away with a working system, not a blank canvas.
      </p>
      <div class="flex flex-wrap gap-4 justify-center">
        <NuxtLink
          to="/guide/getting-started"
          class="inline-flex items-center gap-2 px-8 py-4 rounded-lg bg-primary text-primary-foreground font-medium text-lg hover:opacity-90 transition-opacity"
        >
          <Icon name="lucide:rocket" class="w-5 h-5" />
          Get Started
        </NuxtLink>
        <NuxtLink
          to="/skills"
          class="inline-flex items-center gap-2 px-8 py-4 rounded-lg border border-border hover:bg-muted transition-colors text-lg"
        >
          Browse Skills
        </NuxtLink>
      </div>
    </div>
  </section>
</template>
