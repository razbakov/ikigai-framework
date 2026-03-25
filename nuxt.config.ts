export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',

  devtools: { enabled: true },

  ssr: false,

  modules: [
    '@pinia/nuxt',
    'shadcn-nuxt',
    '@nuxtjs/color-mode',
    '@nuxt/content',
    '@nuxt/icon',
    '@nuxtjs/sitemap',
    '@nuxtjs/robots',
  ],

  postcss: {
    plugins: {
      '@tailwindcss/postcss': {},
    },
  },

  css: ['~/assets/css/main.css'],

  colorMode: {
    preference: 'dark',
    fallback: 'dark',
    classSuffix: '',
  },

  shadcn: {
    prefix: '',
    componentDir: './app/components/ui',
  },

  site: {
    url: 'https://ai-cabinet.netlify.app',
  },

  nitro: {
    preset: 'static',
  },

  routeRules: {
    '/': { prerender: true },
    '/onboard': { prerender: true },
    '/skills': { prerender: true },
    '/guide': { prerender: true },
    '/guide/**': { prerender: true },
    '/skills/**': { prerender: true },
  },
})
