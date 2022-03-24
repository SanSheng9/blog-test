<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">BLOG</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarText">
    <ul class="navbar-nav mr-auto">
    <nuxt-link exact active-class="active" :to="`/`" class="nav-link">Home</nuxt-link>
    <nuxt-link v-if="$store.getters.loggedIn" active-class="active" :to="`/add/`" class="nav-link">New post</nuxt-link>
    </ul>

    <span v-if="$store.getters.loggedIn" class="navbar-text" >
      <nuxt-link :to="`/user/`">{{$store.getters.loggedIn}}</nuxt-link>
         / <a class="logout" @click="logout()">Log out</a>
    </span>

    <span class="navbar-text" v-if="!$store.getters.loggedIn">
          <ul class="navbar-nav mr-auto">
      <nuxt-link active-class="active" :to="`/login/`" class="nav-link">Login</nuxt-link>
      <nuxt-link active-class="active" :to="`/register/`" class="nav-link">Register</nuxt-link>
          </ul>
    </span>
  </div>
</nav>
    <nuxt/>
  </div>
</template>

<script>

export default {
  name: 'layout',
  data() {
    return {
      content: {}
    }
  },
  fetch(){
    this.$store.dispatch("fetchUsers")
  },
  mounted() {
    this.$nuxt.$on('logout', () => {
      this.logout()
    })
  },
  methods: {
    async logout() {
      await this.$auth.logout();
      await fetch('http://localhost:8000/api/logout', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        credentials: 'include',
      });
      this.$router.push('/login');
    }
  },
  computed: {
    getUser() {
      return this.$store.getters['getUser']
    },
        getLoggedIn() {
      return this.$store.getters['getLoggedIn']
    }
  }
}
</script>

<style>
#slash{
}
.logout:hover{
  cursor: pointer;
}
</style>
