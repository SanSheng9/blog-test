<template>
<div>
  <h1>Приветствую, {{ $auth.user.name }}</h1>
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
}
</script>

<style>

</style>
