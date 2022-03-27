<template>
  <div class="container">
    <div class="buttons">
      <nuxt-link
        v-if="post.author === user.login"
        :to="`/posts/${post.id}/edit`"
        class="btn btn-light"
        >Редактировать пост</nuxt-link
      >
      <a
        v-if="post.author === user.login"
        @click="deletePost(post.id)"
        class="btn btn-light"
        >Удалить пост</a
      >
    </div>
    <b-card-group deck>
      <b-card :img-src="post.photo" img-alt="Card image" img-left class="mb-3">
        <h1 class="mb-3 display-4 text-uppercase">{{ post.title }}</h1>
        <b-card-text>
          {{ post.description }}
          <br />
          <div class="post-end">
            <div class="author">
              Writted by
              <b id="user" @click="getProfileUser(post.author)">{{
                post.author
              }}</b>
            </div>
            <div class="created-at">Created at {{ post.created_at }}</div>
          </div>
        </b-card-text>
      </b-card>
    </b-card-group>
    <!-- BLOCK COMMENTS -->
    <div
      :style="{ marginBottom: 20 + 'px' }"
      class="row d-flex justify-content-center"
    >
      <div v-if="loggedIn || comments.length >= 1" class="col-md-8 col-lg-6">
        <div class="card shadow-0 border" style="background-color: #00808050">
          <div class="card-body p-4">
            <div v-if="loggedIn" class="form-outline mb-4">
              <input
                type="text"
                id="addANote"
                class="form-control"
                placeholder="Type comment..."
                v-model="textComment"
              />
              <label
                @click="createComment(post.id)"
                class="btn btn-light"
                for="addANote"
                :style="{ marginTop: 10 + 'px' }"
                >+ Add a comment</label
              >
            </div>

            <div v-for="comment in comments" :key="comment.id" class="card">
              <div class="card-body">
                <p>{{ comment.body }}</p>

                <div class="d-flex justify-content-between">
                  <div class="d-flex flex-row align-items-center">
                    <img
                      :src="comment.avatar"
                      alt="avatar"
                      width="25"
                      height="25"
                    />
                    <p class="small mb-0 ms-2">{{ comment.author }}</p>
                  </div>
                  <div class="d-flex flex-row align-items-center">
                    <p class="small mb-0 ms-2">{{ comment.created_at }}</p>
                  </div>
                  <div
                    v-if="comment.author === user.login"
                    class="d-flex flex-row align-items-center"
                  >
                    <a
                      id="delete"
                      @click="deleteComment(comment.id)"
                      class="small text-muted mb-0"
                      >Delete?</a
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: "View-blog",
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
  data: () => ({
    post: {},
    comments: {},
    textComment: "",
  }),
  methods: {
    async deletePost(id) {
      try {
        await this.$axios.$delete(`/api/posts/${id}/`); // delete recipe
        let newPost = await this.$axios.$get("/api/posts/"); // get new list of recipes
        this.post = newPost; // update list of recipes
        this.$router.push("/");
      } catch (e) {
        console.log(e);
      }
    },
    async getProfileUser(login) {
      await this.$router.push(`/user/${login}`);
    },
    async getComments(id) {
      try {
        this.comments = await this.$axios.$get(`/api/comments/?post=${id}`);
        this.comments.forEach((comment) => {
          if (comment.author == this.user.login) {
            comment.avatar = this.user.avatar;
          }
        });
      } catch (e) {
        console.log(e);
      }
    },
    async deleteComment(id) {
      try {
        await this.$axios.$delete(`/api/comments/${id}/`); // delete recipe
        let newComments = await this.$axios.$get(`/api/comments/?post=${id}`); // get new list of recipes
        this.comments = newComments; // update list of recipes
        this.$router.push(`/posts/${id}`);
      } catch (e) {
        console.log(e);
      }
    },
    async createComment(id) {
      try {
        let formComment = {
          body: this.textComment,
          author: this.user.login,
          post: id,
        };
        await this.$axios.$post("api/comments/", formComment);
        let newComments = await this.$axios.$get(`/api/comments/?post=${id}`); // get new list of recipes
        this.comments = newComments; // update list of recipes
        this.$router.push(`/posts/${id}`);
      } catch (e) {
        console.log(e);
      }
    },
  },
  mounted() {
    this.getComments(this.post.id);
  },
  computed: {
    user({ $store }) {
      return $store.getters["getUser"];
    },
    loggedIn({ $store }) {
      return $store.getters["getLoggedIn"];
    },
  },
};
</script>

<style scoped>
.container {
  margin-top: 20px;
  max-width: 90%;
}
.buttons {
  display: flex;
  margin-bottom: 30px;
  justify-content: space-between;
}
#delete {
  cursor: pointer;
}
.post-end {
  margin-top: 30px;
  color: gray;
  display: flex;
  justify-content: space-between;
}
#user {
  cursor: pointer;
}
</style>
