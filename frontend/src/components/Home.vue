<template>
  <div>
    <br><br>
    <h1>Hello User</h1>
    <img src="../assets/logo.png" width="300" height="300">
    <h2>Welcome to Simple Music!!!</h2> <h2 v-if="username != null">Mr.{{username}}</h2>
     <br>

  </div>
</template>
<script>
/* eslint-disable */
export default {
  data() {
    return {
      username: this.$store.state.user.username
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    },
  },
}
</script>
<style>
h1 {
  color: White;
  font-style: oblique;
  font-size: 30px;
}
h2 {
  color: white;
  font-size: 20px;
}
</style>
