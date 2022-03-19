<template>

<div>
  <div class="post-card">
<div class="card bg-dark text-white">
  <img :src='image' class="card-img" alt="...">
  <div class="card-img-overlay">
    <h5 class="card-title">{{ title }}</h5>
    <nuxt-link :to="`/posts/${id}/`" class="btn btn-light">Открыть пост</nuxt-link>
    <nuxt-link :to="`/posts/${id}/edit`" class="btn btn-light">Редактировать пост</nuxt-link>
  </div>
</div>
</div></div>
</template>

<script>
export default {
  name: 'post-card',
  props: [
    'title', 'image', 'description', 'id',
  ]
}
</script>

<style>
.post-card{
max-width: 400px;
}
</style>
