import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
/* eslint-disable */
const state = {
  user: null,
  fileName: null,
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
    state.fileName = file[0]
    state.duration = file[1]
  }
}

export default new Vuex.Store({
    state,
    mutations
})