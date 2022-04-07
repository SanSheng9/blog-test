<template>
  <div class="home-page">
    <nav
      id="navbar-left"
      class="block-one navbar fixed-left navbar-light bg-light"
    >
      <div class="my-container">
        <form class="form-inline my-2 my-lg-0">
          <label for="search">Search</label>
          <input
            id="search"
            class="form-control mr-sm-2"
            type="search"
            placeholder="..."
            v-model="searchQuery"
          />
          <button
            id="btn-search"
            class="btn btn-light my-2 my-sm-0"
            type="submit"
            @click.prevent="searchQuery = ''"
          >
            Clear
          </button>
        </form>
      </div>
    </nav>

    <div class="block-two posts-list">
      <transition-group name="t-post-list">
        <post-card
          class="post-card"
          v-for="post in searchedProducts"
          :key="post.id"
          :title="post.title"
          :description="post.description"
          :image="post.photo"
          :id="post.id"
        >
        </post-card
      ></transition-group>
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
      title: "BLOG",
    };
  },
  async asyncData({ $axios }) {
    let response = await $axios.get("/api/posts");
    return { posts: response.data };
  },
  data: () => ({
    posts: {},
    searchQuery: "",
  }),
  computed: {
    searchedProducts() {
      return this.posts.filter((post) =>
        post.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
};
</script>

<style scoped>
.home-page {
  display: flex;
  margin-top: 0.7vh;
}

.block-one {
  flex: 0 1 20%;
  min-height: 92vh;
}
#navbar-left {
  display: block;
}
.my-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
#btn-search {
  margin-top: 5px !important;
}
.block-two {
  flex: 1 1 79%;
}
.posts-list {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
.post-card {
  margin: 10px;
}
@media (max-width: 690px) {
  .home-page {
    flex-direction: column;
  }
  .block-one {
    min-height: 1vh;
  }
}
.t-post-list-enter-active,
.t-post-list-leave-active {
  transition: opacity 0.5s ease;
}

.t-post-list-enter-from,
.t-post-list-leave-to {
  opacity: 0;
}
</style>
