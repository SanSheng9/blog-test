<template>
  <div>
    <div class="posts-list">
      <post-card
        class="post-card"
        v-for="post in posts"
        :key="post.id"
        :title="post.title"
        :description="post.description"
        :image="post.photo"
        :id="post.id"
      >
      </post-card>
    </div>
  </div>
</template>

<script>
import PostCard from "~/components/PostCard.vue";
export default {
  components: {
    PostCard,
  },
  head() {
    return {
      title: "Blog",
    };
  },
  async asyncData({ $axios }) {
    let response = await $axios.get("/api/posts");
    return { posts: response.data };
  },
  data: () => ({
    posts: {},
  }),
  methods: {},
};
</script>

<style scoped>
.posts-list {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
.post-card {
  margin: 10px;
}
</style>
