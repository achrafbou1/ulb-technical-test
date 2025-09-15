import {defineNuxtConfig} from 'nuxt/config'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: '2025-07-15',
    devtools: {enabled: true},
    modules: ['@nuxt/eslint', '@nuxt/ui'],
    css: ['~/assets/css/main.css'],
    nitro: {
        routeRules: {
            '/api/**': {
                proxy: 'https://b0s0kwos00g48ow8cg0skg4w.89.116.111.143.sslip.io/**'
            },
        }
    },
})