import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
/* eslint-disable */
const state = {
  user: null
}

const mutations = {
  login(state, user) {
    state.user = user
  },
  logout(state, router) {
    state.user = null
    router.push('/')
  }
}

export default new Vuex.Store({
    state,
    mutations
})