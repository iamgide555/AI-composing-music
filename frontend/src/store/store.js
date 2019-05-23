import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
/* eslint-disable */
const state = {
  user: null,
  file_name: null,
  path: null,
  duration: null
}

const mutations = {
  login(state, user) {
    state.user = user
  },
  logout(state, router) {
    state.user = null
    router.push('/')
  },
  getFilename(state, file) {
    state.path = file[0]
    state.duration = file[3]
    state.file_name = file[2]
  }
}

export default new Vuex.Store({
    state,
    mutations
})