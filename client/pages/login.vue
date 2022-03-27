<template>
  <div class="wrapper">
    <!-- Pills content -->
    <div class="tab-content">
      <div
        class="tab-pane fade show active"
        id="pills-login"
        role="tabpanel"
        aria-labelledby="tab-login"
      >
        <form>
          <!-- Email input -->
          <div class="form-outline mb-4">
            <input
              v-model="email"
              type="email"
              id="loginName"
              class="form-control"
            />
            <label class="form-label" for="loginName">Email</label>
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <input
              v-model="password"
              type="password"
              id="loginPassword"
              class="form-control"
            />
            <label class="form-label" for="loginPassword">Password</label>
          </div>

          <!-- 2 column grid layout -->
          <div class="row mb-4">
            <div class="col-md-6 d-flex justify-content-center">
              <!-- Checkbox -->
            </div>
          </div>

          <!-- Submit button -->
          <button
            @click.prevent="logInUser()"
            type="submit"
            class="btn btn-light btn-block mb-4"
          >
            Sign in
          </button>

          <!-- Register buttons -->
          <div class="text-center">
            <p>
              Not a member? <nuxt-link :to="`/register/`">Register</nuxt-link>
            </p>
          </div>
        </form>
      </div>
    </div>
    <!-- Pills content -->
  </div>
</template>

<script>
export default {
  name: "login",
  head() {
    return {
      title: "Login - BLOG",
    };
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async logInUser() {
      // LOGIN
      try {
        const response = await fetch("http://localhost:8000/api/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          credentials: "include",
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        });
        if (response.status === 200 || response.status === 201) {
          await this.$router.push("/");
        }
      } catch (e) {
        console.log("Логин не удался!", e);
      }
      // AUTH
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
  },
};
</script>
