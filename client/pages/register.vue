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
            <label class="form-label" for="registerName">Login</label>
            <input
              v-model="username"
              type="username"
              id="registerName"
              class="form-control"
              required
            />
          </div>

          <!-- Email input -->
          <div class="form-outline mb-4">
            <label class="form-label" for="registerEmail">Email</label>
            <input
              v-model="email"
              type="email"
              id="registerEmail"
              class="form-control"
              required
            />
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <label class="form-label" for="registerPassword">Password</label>
            <input
              v-model="password"
              type="password"
              id="registerPassword"
              class="form-control"
              pattern="[0-9a-fA-F]{4,8}"
              required
            />
          </div>

          <!-- Repeat Password input -->
          <div class="form-outline mb-4">
            <label class="form-label" for="registerRepeatPassword"
              >Repeat password</label
            ><input
              type="password"
              id="registerRepeatPassword"
              class="form-control"
              pattern="[0-9a-fA-F]{4,8}"
              required
              v-model="repeatPassword"
            />
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
      username: "",
      email: "",
      password: "",
      repeatPassword: "",
    };
  },
  methods: {
    async registerUser() {
      if (this.password === this.repeatPassword) {
        try {
          const response = await fetch("http://localhost:8000/api/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              username: this.username,
              email: this.email,
              password: this.password,
            }),
          });
          if (response.status === 200 || response.status === 201) {
            await this.$router.push("/login");
            this.$notify({
              title: "Register successful!",
            });
          }
          if (response.status === 400) {
            this.$notify({
              title:
                "Error registration! Maybe, you must fill in all the registration fields!",
              type: "warn",
            });
          }
        } catch (e) {
          console.log(e);
        }
      } else {
        this.$notify({
          title: "The passwords are different!",
          type: "warn",
        });
      }
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
