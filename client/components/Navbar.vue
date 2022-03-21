<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">BLOG</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarText">
    <ul class="navbar-nav mr-auto">
    <nuxt-link exact active-class="active" :to="`/`" class="nav-link">Home</nuxt-link>
    <nuxt-link v-if="$auth.loggedIn" active-class="active" :to="`/add/`" class="nav-link">New post</nuxt-link>
    </ul>

    <span class="navbar-text" v-if="$auth.loggedIn">
    {{ $auth.user.email }}
         / <a class="logout" @click="logOut()">Log out</a>
    </span>

    <span class="navbar-text" v-if="!$auth.loggedIn && watch">
          <ul class="navbar-nav mr-auto">
      <nuxt-link active-class="active" :to="`/login/`" class="nav-link">Login</nuxt-link>
      <nuxt-link active-class="active" :to="`/register/`" class="nav-link">Register</nuxt-link>
          </ul>

    </span>
  </div>
</nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: ['watch'],
  methods: {
    logOut(){
    this.$auth.logout()
    this.$router.push('/login/')
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
