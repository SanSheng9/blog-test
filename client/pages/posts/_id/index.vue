<template>
<div class="container">
  <div class="buttons">
    <nuxt-link :to="`/posts/${post.id}/edit`" class="btn btn-light">Редактировать пост</nuxt-link>
    <a @click="deletePost(post.id)" class="btn btn-light">Удалить пост</a>
  </div>
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
      let post = await $axios.$get(`/api/posts/${params.id}`);
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
  },
  methods: {
    async deletePost(id) {
      try {
        await this.$axios.$delete(`/api/posts/${id}/`); // delete recipe
        let newRecipes = await this.$axios.$get("/api/posts/"); // get new list of recipes
        this.recipes = newRecipes; // update list of recipes
        this.$router.push("/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
.container{
  margin-top: 20px;
  max-width: 90%;
}
.buttons{
  display: flex;
  margin-bottom: 30px;
  justify-content: space-between;
}
</style>
