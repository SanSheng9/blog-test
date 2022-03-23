<template>
  <div>
    <Navbar :watch='true' :auth='auth' :content='content'/>
    <nuxt/>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
export default {
  components: {
  Navbar
},
  name: 'layout',
  data() {
    return {
      auth: false,
      content: {}
    }
  },
  mounted() {
    this.$nuxt.$on('auth', auth => {
      this.auth = auth;
    }),
    this.$nuxt.$on('content', content => {
      this.content = content;
    }),
    this.$nuxt.$on('logout', () => {
      this.logout()
    })
  },
  methods: {
    async logout() {
      await fetch('http://localhost:8000/api/logout', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        credentials: 'include',
      });
      await this.$router.push('/login');
    }
  }
}
</script>

<style>

</style>
