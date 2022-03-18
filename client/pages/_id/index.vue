<template>
<div>
  <div class="post">
    <div class="image">
      <img :src='posts.image' alt="">
    </div>
    <div class="text">
      {{posts.description}}
    </div>
  </div>
</div>
</template>


<script>
import PostCard from "~/components/PostCard.vue";
export default {
  head() {
    return {
      title: 'Test-blog'
    };
  },
  components: {
    PostCard
  },
  async asyncData({ $axios, params }) {
    try {
    let response = await $axios.get("/posts")
    let posts = response.data
    return { posts };
    } catch (e) {
      return { posts: [] };
    }
  },
  data() {
    return {
      posts: []
      };
  },
  methods: {

  }
};
</script>

<style>

</style>
