export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'client-blog',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    'bootstrap-vue/nuxt',
    '@nuxtjs/axios',
    '@nuxtjs/auth',
  ],

  axios: {
    baseURL: "http://localhost:8000/"
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },
  auth: {
    strategies: {
      local: {
  //      token: {
  //        property: 'token',
   //       global: true,
          // required: true,
          // type: 'Bearer'
   //     },
        endpoints: {
          login: { url: '/users/login/', method: 'post', propertyName: 'data.token'},
          logout: { url: '/users/logout/', method: 'post' },
          user: { url: '/users', method: 'get', propertyName: 'data'}
        }
      }
    }
  }
}
