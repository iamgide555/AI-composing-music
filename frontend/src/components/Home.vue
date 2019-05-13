<template>
  <div>
    Home Page
    <br><br>
    <router-link to="/generate">
      <a v-if="user">Generate</a>
    </router-link>
     <br>

  </div>
</template>
<script>
/* eslint-disable */
export default {
  computed: {
    user() {
      return this.$store.state.user
    },
  },
}
</script>
<style>

</style>
