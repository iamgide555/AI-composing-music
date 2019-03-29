<template>
  <div id="app">
      <section class="hero is-primary">
        <nav class="navbar" role="navigation" aria-label="main navigation">
          <router-link to="/">
            <div class="navbar-brand">
              <a class="navbar-item" href="https://bulma.io">
                <img src="http://pluspng.com/img-png/music-png-transparent-image-2400.png">
                <H1 class="title">AI</H1>
              </a>

              <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
              </a>
            </div>
          </router-link>

          <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-end">
              <div class="navbar-item">
                <div class="buttons">
                  <router-link to="/signup">
                    <a class="button">
                      <strong>Sign up</strong>
                    </a>
                  </router-link>
                  <router-link to="/login">
                    <a class="button is-primary">
                      Log in
                    </a>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </nav>
      </section>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
