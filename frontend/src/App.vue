<template>
  <div id="app">
      <section>
        <nav>
          <div class="topnav">
            <div class="logo">
              <router-link to="/">
                <a>Simple music</a>
              </router-link>
            </div>
            <router-link to="/signup" v-if="!user">
              <a>Sign up</a>
            </router-link>
            <router-link to="/login" v-if="!user">
              <a>Login</a>
            </router-link>
          </div>
        </nav>
      </section>
    <router-view/>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'App',
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    logout() {
      this.$store.commit('logout', this.$router)
    }
    
  }
}
</script>

<style>
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50; 
}

html,body {
  height: 100%;
  margin: 0;
  padding: 0;
  background-image: linear-gradient(#24234D,#241428);
}
.topnav {
  background-color: rgba(4, 4, 39, 0.527);
  overflow: hidden;
}
/* Style the links inside the navigation bar */
.topnav a {
  float: right;
  color: #fff0f0;
  text-align: center;
  padding: 8px 12px;
  font-size: 18px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}
.logo {
  width: 13%;
  float: left;
  text-transform: uppercase;
  color: #fff;
  font-size: 15px;
  text-align: left;
  padding-left: 0px;
}
</style>
