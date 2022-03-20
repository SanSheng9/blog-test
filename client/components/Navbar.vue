<template>
<div>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">BLOG</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
    <nuxt-link exact active-class="active" :to="`/`" class="nav-link">Home</nuxt-link>
    <nuxt-link active-class="active" :to="`/add/`" class="nav-link">New post</nuxt-link>
    <nuxt-link active-class="active" :to="`/login/`" class="nav-link">Login</nuxt-link>
    <nuxt-link active-class="active" :to="`/register/`" class="nav-link">Register</nuxt-link>
    </ul>
  </div>
</nav>
</div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style>

</style>
