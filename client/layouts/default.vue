<template>
  <div>
    <Navbar :watch='true'/>
    <nuxt/>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
export default {
components: {
  Navbar
}
}
</script>

<style>

</style>
