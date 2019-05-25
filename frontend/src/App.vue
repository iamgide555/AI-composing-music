<template>
  <div id="app">
      <section>
        <nav>
          <div class="topnav">
            <div class="logo">
              <router-link to="/">
                <img src="./assets/logo.png" width="40" height="40">
                <a>simple music</a>
              </router-link>
            </div>
            <ul class="menu-area">
              <li>
                <router-link to="/signup" v-if="!user">
                  <a>Sign up</a>
                </router-link>
              </li>
              <li>
                <router-link to="/login" v-if="!user">
                  <a>Login</a>
                </router-link>
              </li>
              <li @click="list" v-if="user">
                <a>List</a>
              </li>
              <li v-on:click="logout" v-if="user">
                <a>Logout</a>
              </li>
            </ul>
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
    list() {
      this.$router.push('/list')
    },
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
  background-attachment:fixed;
  background-origin: initial;
  background-repeat:no-repeat;
  background: -webkit-linear-gradient(#24234D 0%,#241428 100%); 
}
.topnav {
  background-color: rgba(4, 4, 39, 0.527);
  overflow: hidden;
}
/* Style the links inside the navigation bar */
.topnav a {
  float: right;
  display: block;
  color: #fff0f0;
  text-align: center;
  padding: 8px 12px;
  font-size: 18px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-transform: uppercase;
}

/* Change the color of links on hover */
.topnav .icon {
  display: none;
}
.logo {
  float: left;
  text-align: left;
  padding-top: 5px;
  padding-left: 20px;
}
nav {
    position: relative;
    width: calc(100% - 60px);
    margin: 0 auto;
    padding: 10px 10px;
    text-align: right;
    padding-right: 2%;
}
.menu-area li {
    display: inline-block;
}
.menu-area a:hover {
    background: rgb(234, 240, 255);
    color: rgb(19, 17, 22);
}

.menu-area a:hover:after {
    transform: translateY(-50%) rotate(-35deg);
}

</style>
