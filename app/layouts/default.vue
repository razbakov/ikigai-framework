<template>
  <div class="min-h-screen flex flex-col bg-background text-foreground">
    <CommonAppHeader />
    <main class="flex-1">
      <slot />
    </main>
    <CommonAppFooter />
  </div>
</template>
