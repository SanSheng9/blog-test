<template>
<div>
  <Navbar :watch='false' />
<div class="wrapper">
    <!-- Pills navs -->
<ul class="nav nav-pills nav-justified mb-3" id="ex1" role="tablist">
  <li class="nav-item" role="presentation">
    <nuxt-link active-class="active" :to="`/login/`"
      class="nav-link"
      id="tab-login"
      data-mdb-toggle="pill"
      role="tab"
      aria-controls="pills-login"
      aria-selected="true"
      >Login</nuxt-link>
  </li>
  <li class="nav-item" role="presentation">
    <nuxt-link active-class="active" :to="`/register/`"
      class="nav-link"
      id="tab-register"
      data-mdb-toggle="pill"
      href="#pills-register"
      role="tab"
      aria-controls="pills-register"
      aria-selected="false"
      >Register</nuxt-link
    >
  </li>
</ul>
<nuxt/>
  </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
export default {
components: {
  Navbar
},
}
</script>

<style>
.wrapper{
  max-width: 40%;
  margin: 0 auto;
  margin-top: 200px;
}
.nav-pills .nav-link.active, .nav-pills .show > .nav-link {
    color: #212529;
    background-color: #f8f9fa;
    border-color: #f8f9fa;
}
a {
    color: #808080;
    text-decoration: none;
    background-color: transparent;
}
</style>
