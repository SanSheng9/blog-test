<template>
  <div>
    <div class="page-content page-container" id="page-content">
      <div class="padding">
        <div id="container" class="row container d-flex justify-content-center">
          <div class="col-md-5">
            <div class="card">
              <!-- USER PROFILE CHANGE -->
              <div
                v-if="getUser.username === profile[0].username"
                class="card-body text-center"
              >
                <!-- avatar -->
                <img
                  v-if="!preview"
                  id="avatar"
                  :src="profile[0].avatar"
                  class="img-lg mb-4"
                  alt="profile image"
                />
                <img v-else id="avatar" class="img-lg mb-4" :src="preview" />
                <div class="form-group">
                  <input type="file" @change="onFileChange" />
                </div>
                <!-- login no changed -->
                <h4>{{ profile[0].username }}</h4>
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
import { mapGetters } from "vuex";

export default {
  layout: "default",
  data() {
    return {
      upProfile: {},
      preview: null,
    };
  },
  async asyncData({ params, $axios }) {
    let profile = await $axios.$get(`/api/profile/?username=${params.id}`);
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
      reader.onload = (e) => {
        this.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitProfile() {
      let editedProfile = this.profile[0];
      this.upProfile = this.profile[0];

      /* if (
        editedProfile.avatar.indexOf("http://") != -1 ||
        editedProfile.avatar == "" ||
        editedProfile.avatar == null
      ) {
        delete editedProfile["avatar"];
      } */
      if (this.preview !== null) {
        let formData = new FormData();
        formData.append("username", editedProfile.username);
        formData.append("about_me", editedProfile.about_me);
        formData.append("avatar", editedProfile.avatar);

        console.log(formData);
        try {
          const response = await fetch("http://localhost:8000/api/user", {
            method: "PATCH",
            credentials: "include",
            body: formData,
          });
          if (response.status === 200 || response.status === 201) {
            this.$router.push(`/user/${this.profile[0].username}`);
          }
        } catch (e) {
          console.log(e);
        }
      } else {
        this.upProfile = {
          about_me: this.profile[0].about_me,
          avatar: this.getUser.avatar.substr(6),
          username: this.getUser.username,
        };

        console.log(this.upProfile);
        try {
          const response = await fetch("http://localhost:8000/api/user", {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },

            credentials: "include",
            body: JSON.stringify(this.upProfile),
          });
          if (response.status === 200 || response.status === 201) {
            this.$router.push(`/user/${this.profile[0].username}`);
          }
          console.log("JSON type");
        } catch (e) {}
      }
    },
  },
  computed: { ...mapGetters(["getLoggedIn", "getUser"]) },
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
