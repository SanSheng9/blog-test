<
<template>
  <div class="container">
    <main class="container my-5">
      <div class="row">
        <div class="col-12 text-center my-3">
          <h2 class="mb-3 display-4 text-uppercase">{{ post.title }}</h2>
        </div>
        <div class="col-md-6 mb-4">
          <img
            v-if="preview"
            class="img-fluid"
            style="
              width: 400px;
              border-radius: 10px;
              box-shadow: 0 1rem 1rem rgba(0, 0, 0, 0.7);
            "
            :src="preview"
            alt
          />
          <img
            v-else
            class="img-fluid"
            style="
              width: 400px;
              border-radius: 10px;
              box-shadow: 0 1rem 1rem rgba(0, 0, 0, 0.7);
              opacity: 70%;
            "
            src="@/static/2.jpg"
          />
        </div>
        <div class="col-md-4">
          <form @submit.prevent="submitPost">
            <div class="form-group">
              <label for>Title</label>
              <input type="text" class="form-control" v-model="post.title" />
            </div>
            <div class="form-group">
              <label for>Picture</label>
              <input type="file" name="file" @change="onFileChange" />
            </div>
            <div class="form-group mb-3">
              <label for>Text</label>
              <textarea
                v-model="post.description"
                class="form-control"
                rows="8"
              ></textarea>
            </div>
            <button type="submit" class="btn btn-light">Submit</button>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  head() {
    return {
      title: "Add Post",
    };
  },
  data: () => ({
    post: {
      title: "",
      photo: "",
      description: "",
      author: "",
    },
    preview: "",
  }),
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.post.photo = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      // let image = new Image();
      let reader = new FileReader();
      let vm = this;
      reader.onload = (e) => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitPost() {
      const config = {
        headers: { "content-type": "multipart/form-data" },
      };
      this.post.author = this.getUser.username;

      let formData = new FormData();
      for (let data in this.post) {
        formData.append(data, this.post[data]);
      }
      if (this.post.photo !== null || this.post.photo != "") {
        try {
          let response = await this.$axios.$post(
            "api/posts/",
            formData,
            config
          );
          await this.$router.push("/");
        } catch (e) {
          console.log(e);
        }
      }
    },
  },
  computed: { ...mapGetters(["getLoggedIn", "getUser"]) },
};
</script>
<style scoped></style>
