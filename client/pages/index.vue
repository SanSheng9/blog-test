<template>
<div>
  <div class="posts-list">
  <post-card
  class="post-card"
  v-for="post in posts" :key="post.id"
  :title='post.title'
  :description='post.description'
  :image='post.photo'
  :id='post.id'
  >
</post-card>
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
    let response = await $axios.get("/api/posts")
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

<style scoped>

.posts-list{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
.post-card{
  margin: 15px;
}
</style>
