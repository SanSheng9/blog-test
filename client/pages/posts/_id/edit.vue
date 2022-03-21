<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ post.title }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img v-if="!preview" class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="post.photo">
        <img v-else class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="preview">
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitPost">
          <div class="form-group">
            <label for>Post tilte</label>
            <input type="text" class="form-control" v-model="post.title" >
          </div>
          <div class="form-group">
            <label for>Post picture</label>
            <input type="file" @change="onFileChange">
          </div>
          <div class="form-group mb-3">
            <label for>Description</label>
            <textarea v-model="post.description" class="form-control" rows="8"></textarea>
          </div>
          <button type="submit" class="btn btn-success">Save</button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head(){
      return {
        title: "Edit Recipe"
      }
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
      },
      preview: ""
    };
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.post.picture = files[0]
      this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitPost() {
      let editedPost = this.post
      if (editedPost.photo.indexOf("http://") != -1){
        delete editedPost["photo"]
      }
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in editedPost) {
        formData.append(data, editedPost[data]);
      }
      try {
        let response = await this.$axios.$patch(`/api/posts/${editedPost.id}/`, formData, config);
        this.$router.push("/");
        console.log('formData: ', formData);
        console.log('response: ', response)
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
<style>
</style>
