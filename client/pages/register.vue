<template>
<!-- Pills content -->
<div class="tab-content">
  <div class="tab-pane fade" id="pills-register" role="tabpanel" aria-labelledby="tab-register">
    <form>

      <!-- Username input -->
      <div class="form-outline mb-4">
        <input v-model='register.username' type="text" id="registerUsername" class="form-control" />
        <label class="form-label" for="registerUsername">Username</label>
      </div>

      <!-- Email input -->
      <div class="form-outline mb-4">
        <input v-model='register.email' type="email" id="registerEmail" class="form-control" />
        <label class="form-label" for="registerEmail">Email</label>
      </div>

      <!-- Password input -->
      <div class="form-outline mb-4">
        <input v-model="register.password" type="password" id="registerPassword" class="form-control" />
        <label class="form-label" for="registerPassword">Password</label>
      </div>

      <!-- Repeat Password input -->
      <div class="form-outline mb-4">
        <input type="password" id="registerRepeatPassword" class="form-control" />
        <label class="form-label" for="registerRepeatPassword">Repeat password</label>
      </div>


      <!-- Submit button -->
      <button @click.prevent='registerUser()' type="submit" class="btn btn-primary btn-block mb-3">Sign in</button>
    </form>
  </div>
</div>
<!-- Pills content -->
</template>

<script>
export default {
  layout: 'form',
  data: () => ({
    register: {
      password: '',
      last_login: null,
      username: '',
      first_name: '',
      last_name: '',
      email: '',
      is_staff: false,
      is_active: true,
      groups: [1],
      user_permissions: []
    }
  }),
  methods: {
  async registerUser() {
    this.loading = true;
    let data = this.register;
    try {
      await this.$axios.post('/users/', data);
      this.$router.push('/login');
      this.loading = false;

    } catch (error) {
      this.loading = false;
    }
  }
}
}
</script>

<style>
.tab-content > .tab-pane {
    display: block;
}
.fade:not(.show) {
    opacity: 100%;
}
</style>
