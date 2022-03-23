<template>
<!-- Pills content -->
<div class="tab-content">
  <div class="tab-pane fade" id="pills-register" role="tabpanel" aria-labelledby="tab-register">
    <form>

      <!-- Name input -->
      <div class="form-outline mb-4">
        <input v-model='name' type="username" id="registerName" class="form-control" />
        <label class="form-label" for="registerName">Name</label>
      </div>

      <!-- Email input -->
      <div class="form-outline mb-4">
        <input v-model='email' type="email" id="registerEmail" class="form-control" />
        <label class="form-label" for="registerEmail">Email</label>
      </div>

      <!-- Password input -->
      <div class="form-outline mb-4">
        <input v-model="password" type="password" id="registerPassword" class="form-control" />
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
   name: "register",
  data() {
    return {
      name: '',
      email: '',
      password: ''
    }
  },
  methods: {
    async registerUser() {
      await fetch('http://localhost:8000/api/register', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          name: this.name,
          email: this.email,
          password: this.password
        })
      });
      await this.$router.push('/login');
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
.btn-primary {
    color: #212529;
    background-color: #f8f9fa;
    border-color: #f8f9fa;
}
.btn-primary:hover,
.btn-primary:active {
    color: #f8f9fa;
    background-color: #212529;
    border-color: #212529;
}
</style>
