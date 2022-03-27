<template>
  <div class="wrapper">
    <!-- Pills content -->
    <div class="tab-content">
      <div
        class="tab-pane fade"
        id="pills-register"
        role="tabpanel"
        aria-labelledby="tab-register"
      >
        <form>
          <!-- Name input -->
          <div class="form-outline mb-4">
            <input
              v-model="login"
              type="username"
              id="registerName"
              class="form-control"
            />
            <label class="form-label" for="registerName">Login</label>
          </div>

          <!-- Email input -->
          <div class="form-outline mb-4">
            <input
              v-model="email"
              type="email"
              id="registerEmail"
              class="form-control"
            />
            <label class="form-label" for="registerEmail">Email</label>
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <input
              v-model="password"
              type="password"
              id="registerPassword"
              class="form-control"
            />
            <label class="form-label" for="registerPassword">Password</label>
          </div>

          <!-- Repeat Password input -->
          <div class="form-outline mb-4">
            <input
              type="password"
              id="registerRepeatPassword"
              class="form-control"
            />
            <label class="form-label" for="registerRepeatPassword"
              >Repeat password</label
            >
          </div>

          <!-- Submit button -->
          <button
            @click.prevent="registerUser()"
            type="submit"
            class="btn btn-light btn-block mb-3"
          >
            Sign in
          </button>
        </form>
      </div>
    </div>
  </div>
  <!-- Pills content -->
</template>

<script>
export default {
  name: "register",
  head() {
    return {
      title: "Register - BLOG",
    };
  },
  data() {
    return {
      login: "",
      email: "",
      password: "",
    };
  },
  methods: {
    async registerUser() {
      await fetch("http://localhost:8000/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          login: this.login,
          email: this.email,
          password: this.password,
        }),
      });
      await this.$router.push("/login");
    },
  },
};
</script>

<style>
.wrapper {
  margin: 0 auto;
  margin-top: 150px;
  max-width: 30%;
}
.tab-content > .tab-pane {
  display: block;
}
.fade:not(.show) {
  opacity: 100%;
}
</style>
