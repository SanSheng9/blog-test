<template>
  <div>
    <div class="page-content page-container" id="page-content">
      <div class="padding">
        <div id="container" class="row container d-flex justify-content-center">
          <div class="col-md-5">
            <div class="card">
              <div class="card-body text-center">
                <div>
                  <img
                    id="avatar"
                    :src="'http://127.0.0.1:8000' + user.avatar"
                    class="img-lg rounded-circle mb-4"
                    alt="profile image"
                  />
                  <h4>{{ user.name }}</h4>
                </div>
                <p class="mt-2 card-text">
                  {{ user.about_me }}
                </p>
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
  layout: "default",
  data() {
    return {
      message: "",
      content: "",
    };
  },
  computed: {
    user({ $store }) {
      return $store.getters["getUser"];
    },
  },
};
</script>

<style scoprf>
#page-content {
  margin-top: 10vh;
}
#container {
  margin: 0 auto;
}
#avatar {
  max-width: 80px;
}
</style>
