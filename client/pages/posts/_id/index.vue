<template>
  <div class="container">
    <div v-if="post.author === getUser.username" class="buttons">
      <nuxt-link :to="`/posts/${post.id}/edit`" class="btn btn-light"
        >Edit the post</nuxt-link
      >
      <a @click="deletePost(post.id)" class="btn btn-light">Delete a post</a>
    </div>

    <div class="col-md-10 blogShort">
      <div class="col-12 text-left my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ post.title }}</h2>
      </div>
      <div class="img">
        <img
          :src="post.photo"
          alt="post img"
          class="pull-left img-responsive postImg img-thumbnail margin10"
        />
      </div>
      <article>
        <p>
          {{ post.description }}
        </p>
      </article>
      <div class="post-end">
        <div class="author">
          Writted by
          <b id="user" @click="getProfileUser(post.author)">{{
            post.author
          }}</b>
        </div>
        <div class="created-at">Created at {{ post.created_at }}</div>
      </div>
    </div>

    <!-- BLOCK COMMENTS -->
    <div
      :style="{ marginBottom: 20 + 'px' }"
      class="row d-flex justify-content-center"
    >
      <div v-if="getLoggedIn || comments.length >= 1" class="col-md-8 col-lg-6">
        <div class="card shadow-0 border" style="background-color: #00808050">
          <div class="card-body p-4">
            <div v-if="getLoggedIn" class="form-outline mb-4">
              <input
                type="text"
                id="addANote"
                class="form-control"
                placeholder="Type comment..."
                v-model="textComment"
              />
              <label
                @click="createComment(post.id)"
                class="btn btn-secondary"
                for="addANote"
                :style="{ marginTop: 10 + 'px' }"
                >Add a comment</label
              >
            </div>
            <transition-group name="comment-list">
              <div
                id="comment"
                v-for="comment in comments"
                :key="comment.id"
                class="card"
              >
                <div class="card-body">
                  <p>{{ comment.body }}</p>

                  <div class="d-flex justify-content-between">
                    <div class="d-flex flex-row align-items-center">
                      <!--        <img
                      :src="comment.avatar"
                      alt="avatar"
                      width="25"
                      height="25"
                    /> -->
                      <p
                        class="small mb-0 ms-2"
                        id="user"
                        @click="getProfileUser(comment.author)"
                      >
                        <b>{{ comment.author }}</b>
                      </p>
                    </div>
                    <div class="d-flex flex-row align-items-center">
                      <p class="small mb-0 ms-2">{{ comment.created_at }}</p>
                    </div>
                  </div>
                  <div
                    v-if="comment.author === getUser.username"
                    class="d-flex flex-row align-items-center"
                  >
                    <p
                      id="delete"
                      @click="deleteComment(comment.id)"
                      class="small text-muted mb-0"
                    >
                      Delete
                    </p>
                  </div>
                </div>
              </div>
            </transition-group>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

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
    user: "",
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
    async getProfileUser(username) {
      await this.$router.push(`/user/${username}`);
    },
    async getComments(id) {
      try {
        this.comments = await this.$axios.$get(`/api/comments/?post=${id}`);
        /*         const profile = await this.$axios.$get(`/api/profile`);
        console.log(profile);
        this.comments.forEach((comment) => {
          const profiles = profile.filter((p) => p.author == comment.author);
          console.log(profiles);
           for (let p of profiles) {
            if ()
          }
        }); */
        /*
         for (let p of profile) {
          let n = 0;
          if (authors[n].author === profile.author)
        }  */
      } catch (e) {
        console.log(e);
      }
    },
    async deleteComment(id) {
      let post = this.post.id;
      try {
        await this.$axios.$delete(`/api/comments/${id}/`); // delete recipe
        this.comments = await this.$axios.$get(`/api/comments/?post=${post}`); // get new list of recipes
        await this.$router.push(`/posts/${post}`);
      } catch (e) {
        console.log(e);
      }
    },
    async createComment(id) {
      try {
        let formComment = {
          body: this.textComment,
          author: this.getUser.username,
          post: id,
        };
        await this.$axios.$post("api/comments/", formComment);
        let newComments = await this.$axios.$get(`/api/comments/?post=${id}`); // get new list of recipes
        this.textComment = "";
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
  computed: { ...mapGetters(["getLoggedIn", "getUser"]) },
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
  margin-top: 20px;
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
#id {
  max-width: 100%;
}
.img {
  max-width: 50vw;
  margin-bottom: 20px;
}
.card {
  margin-top: 30px;
  background-color: #f8f9fa !important;
}
.comment-list-enter-active,
.comment-list-leave-active {
  transition: opacity 0.5s ease;
}

.comment-list-enter-from,
.comment-list-leave-to {
  opacity: 0;
}
</style>
