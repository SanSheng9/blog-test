<template>
<!-- Pills content -->
<div class="tab-content">
  <div class="tab-pane fade show active" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <form>

      <!-- Email input -->
      <div class="form-outline mb-4">
        <input v-model="username" type="email" id="loginName" class="form-control" />
        <label class="form-label" for="loginName">Email or username</label>
      </div>

      <!-- Password input -->
      <div class="form-outline mb-4">
        <input v-model="password" type="password" id="loginPassword" class="form-control" />
        <label class="form-label" for="loginPassword">Password</label>
      </div>

      <!-- 2 column grid layout -->
      <div class="row mb-4">
        <div class="col-md-6 d-flex justify-content-center">
          <!-- Checkbox -->
        </div>


      </div>

      <!-- Submit button -->
      <button @click.prevent='logIn()' type="submit" class="btn btn-primary btn-block mb-4">Sign in</button>

      <!-- Register buttons -->
      <div class="text-center">
        <p>Not a member?     <nuxt-link :to="`/register/`">Register</nuxt-link></p>
      </div>
    </form>
  </div>
</div>
<!-- Pills content -->
</template>

<script>
export default {
  layout: 'form',
    data: () => ({
      username: '',
      password: '',
  }),
methods: {
  async logIn() {
    let data = this.login;
    this.loading = true;
    try {
      let res = await this.$auth.loginWith('local', {
        username: this.username,
        password: this.password
      });
      this.loading = false;
      let user = res.data.data.user;
      this.$auth.setUser(user);
      console.log('Succes!!!!');

    } catch (error) {
      this.loading = false;
      console.log(error);
    }
  }
}}
</script>

<style>
.form{
  max-width: 30%;
  margin: 0 auto;
  margin-top: 300px;
}
</style>
