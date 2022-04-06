<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light" id="navbar">
      <nuxt-link :to="`/`" class="navbar-brand">BLOG</nuxt-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarText"
        aria-controls="navbarText"
        aria-expanded="true"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <nuxt-link
            v-if="getLoggedIn"
            active-class="active"
            :to="`/add/`"
            class="nav-link"
            >+ Add a post</nuxt-link
          >
        </ul>

        <span v-if="getLoggedIn" class="navbar-text">
          <nuxt-link :to="`/user/${getUser.username}`">{{
            getUser.email
          }}</nuxt-link>
          / <a class="logout" @click="logout()">Log out</a>
        </span>

        <span class="navbar-text" v-if="!getLoggedIn">
          <ul class="navbar-nav mr-auto">
            <nuxt-link active-class="active" :to="`/login/`" class="nav-link"
              >Login</nuxt-link
            >
            <nuxt-link active-class="active" :to="`/register/`" class="nav-link"
              >Register</nuxt-link
            >
          </ul>
        </span>
      </div>
    </nav>
    <nuxt />
    <notifications position="bottom right" width="30%" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "layout",
  data() {
    return {};
  },
  async mounted() {
    try {
      const response = await fetch("http://localhost:8000/api/user", {
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });
      const content = await response.json();
      if (content.username) {
        this.$store.commit("setUser", content);
        this.$store.commit("setLoggedIn", true);
      }
    } catch (e) {
      (this.message = "You are not logged in"), e;
    }
  },
  methods: {
    async logout() {
      await fetch("http://localhost:8000/api/logout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });
      this.$store.commit("setUser", "");
      this.$store.commit("setLoggedIn", false);
      this.$router.push("/login");
    },
  },
  computed: {
    ...mapGetters(["getLoggedIn", "getUser"]),
  },
};
</script>

<style>
#slash {
}
.logout:hover {
  cursor: pointer;
}
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
textarea:-webkit-autofill,
textarea:-webkit-autofill:hover,
textarea:-webkit-autofill:focus,
select:-webkit-autofill,
select:-webkit-autofill:hover,
select:-webkit-autofill:focus {
  border: 1px solid teal;
  -webkit-text-fill-color: #008080;
  -webkit-box-shadow: 0 0 0px 1000px rgba(0, 128, 128, 0.157) inset;
  transition: background-color 5000s ease-in-out 0s;
}
</style>
