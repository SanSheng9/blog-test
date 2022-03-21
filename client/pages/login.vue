<template>
<!-- Pills content -->
<div class="tab-content">
  <div class="tab-pane fade show active" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <form>

      <!-- Email input -->
      <div class="form-outline mb-4">
        <input v-model="userData.email" type="email" id="loginName" class="form-control" />
        <label class="form-label" for="loginName">Email or username</label>
      </div>

      <!-- Password input -->
      <div class="form-outline mb-4">
        <input v-model="userData.password" type="password" id="loginPassword" class="form-control" />
        <label class="form-label" for="loginPassword">Password</label>
      </div>

      <!-- 2 column grid layout -->
      <div class="row mb-4">
        <div class="col-md-6 d-flex justify-content-center">
          <!-- Checkbox -->
        </div>


      </div>

      <!-- Submit button -->
      <button @click.prevent='logInUser()' type="submit" class="btn btn-primary btn-block mb-4">Sign in</button>

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
    userData: { email: '', password: '', showPassword: false },
  }),
  methods: {
    async logInUser() {
      try {
        await this.$auth.loginWith('local', {
          data: this.userData,
        })
        console.log('notification successful')
      } catch (error) {
        console.log('notification unsuccessful')
      }
    },
  },
}
</script>
