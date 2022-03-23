<template>
<div>
      <p>message:</p> {{ message }}
      <p>content: </p> {{content}}
</div>
</template>

<script>
export default {
    layout: 'default',
data() {
    return {
      message: '',
      content: '',
    }
  },
  async mounted() {
    try {
      const response = await fetch('http://localhost:8000/api/user', {
        headers: {'Content-Type': 'application/json'},
        credentials: 'include',
      })
      const content = await response.json();
      this.message = 'Hi ' + content.name;
      this.content = content
      this.$nuxt.$emit('auth', true);
      this.$nuxt.$emit('content', this.content);
    } catch (e) {
      this.message = 'You are not logged in';
      this.$nuxt.$emit('auth', false);
    }
  }
}
</script>

<style>

</style>
