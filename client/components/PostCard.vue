<template>
  <div id="card">
    <div class="post-card">
      <div class="card bg-dark text-white">
        <img :src="image" class="card-img" alt="..." />
        <div class="card-img-overlay">
          <h5 class="card-title">{{ title }}</h5>
          <nuxt-link :to="`/posts/${id}/`" class="btn btn-light"
            >Open post</nuxt-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "post-card",
  props: ["title", "image", "description", "id"],
};
</script>

<style>
#card {
  max-width: 400px;
  min-width: 400px;
  min-height: 300px;
}
.post-card h5,
.post-card .btn {
  z-index: 3;
}
#card img {
  z-index: 1;
}
.card-img-overlay {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
