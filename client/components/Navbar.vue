<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">BLOG</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
    <nuxt-link exact active-class="active" :to="`/`" class="nav-link">Home</nuxt-link>
    <nuxt-link active-class="active" :to="`/add/`" class="nav-link">New post</nuxt-link>
    <nuxt-link active-class="active" :to="`/login/`" class="nav-link">Login</nuxt-link>
    <nuxt-link active-class="active" :to="`/register/`" class="nav-link">Register</nuxt-link>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style>

</style>
