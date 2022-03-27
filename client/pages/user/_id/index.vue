<template>
  <div>
    <div class="page-content page-container" id="page-content">
      <div class="padding">
        <div id="container" class="row container d-flex justify-content-center">
          <div class="col-md-5">
            <div class="card">
              <!-- USER PROFILE STATIC -->
              <div class="card-body text-center">
                <img
                  id="avatar"
                  :src="profile[0].avatar"
                  class="img-lg mb-4"
                  alt="profile image"
                />
                <h4>{{ profile[0].username }}</h4>
                <p class="mt-2 card-text">
                  {{ profile[0].about_me }}
                </p>
              </div>
              <nuxt-link
                v-if="user.username === profile[0].username"
                :to="`/user/${user.username}/edit`"
                class="btn btn-light"
                >Change my profile!</nuxt-link
              >
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
    profile: { avatar: "", about_me: "" },
  }),
  async asyncData({ params, $axios }) {
    let profile = await $axios.$get(`/api/profile/?username=${params.id}`);
    return { profile };
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
