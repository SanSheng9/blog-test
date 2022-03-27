<template>
  <div>
    <div class="page-content page-container" id="page-content">
      <div class="padding">
        <div id="container" class="row container d-flex justify-content-center">
          <div class="col-md-5">
            <div class="card">
              <!-- USER PROFILE CHANGE -->
              <div
                v-if="user.login === profile[0].login"
                class="card-body text-center"
              >
                <!-- avatar -->
                <img
                  v-if="!preview"
                  id="avatar"
                  :src="profile[0].avatar"
                  class="img-lg rounded-circle mb-4"
                  alt="profile image"
                />
                <img
                  v-else
                  id="avatar"
                  class="img-lg rounded-circle mb-4"
                  :src="preview"
                />
                <div class="form-group">
                  <input type="file" @change="onFileChange" />
                </div>
                <!-- login no changed -->
                <h4>{{ profile[0].login }}</h4>
                <!-- about -->
                <div class="form-group mb-3">
                  <input
                    v-model="profile[0].about_me"
                    id="input-about"
                    type="text"
                    class="form-control"
                  />
                </div>
              </div>

              <!-- END -->
              <a @click="submitProfile()" class="btn btn-light">
                Save changes!
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  layout: "default",
  data: () => ({
    preview: "",
    formData: {},
  }),
  async asyncData({ params, $axios }) {
    let profile = await $axios.$get(`/api/profile/?login=${params.id}`);
    return { profile };
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.profile[0].avatar = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = (e) => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitProfile() {
      let editedProfile = this.profile[0];
      //      if (editedPost.photo.indexOf("http://") != -1){
      //        delete editedPost["photo"]
      //      }
      let formData = new FormData();
      formData.append("login", editedProfile.login);
      formData.append("about_me", editedProfile.about_me);
      formData.append("avatar", editedProfile.avatar);
      console.log(formData);
      try {
        await fetch("http://localhost:8000/api/user", {
          method: "PATCH",
          credentials: "include",
          body: formData,
        });
        this.$router.push(`/user/${this.profile[0].login}`);
      } catch (e) {
        console.log(e);
      }
    },
  },
  computed: {
    user({ $store }) {
      return $store.getters["getUser"];
    },
  },
};
</script>

<style scoped>
#page-content {
  margin-top: 10vh;
}
#container {
  margin: 0 auto;
}
#avatar {
  max-height: 100px;
}
#input-about {
  text-align: center;
}
img {
  max-width: 100%;
}
</style>
