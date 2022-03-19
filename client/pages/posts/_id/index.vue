<template>
<div class="container">
      <b-card-group deck>
      <b-card :img-src="post.photo" img-alt="Card image" img-left class="mb-3">
        <b-card-text>
          {{post.description}}
        </b-card-text>
      </b-card>
      </b-card-group>
</div>
</template>


<script>
export default {
  head() {
    return {
      title: 'View-blog'
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let post = await $axios.$get(`/posts/${params.id}`);
      return { post };
    } catch (e) {
      return { post: [] };
    }
  },
  data() {
    return {
      post: {
        title: "",
        photo: "",
        description: ""
      }
    };
  }
};
</script>

<style scoped>
.container{
  margin-top: 20px;
  max-width: 90%;
}
</style>
