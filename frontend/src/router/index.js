import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Signup from '@/components/Signup'
import Test from '@/components/Test'
import Test2 from '@/components/Test2'
import Generate from '@/components/Generate'
import Song from '@/components/Song'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/signup',
      name: 'Singup',
      component: Signup
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    },
    {
      path: '/test2',
      name: 'Test2',
      component: Test2
    },
    {
      path: '/Generate',
      name: 'Generate',
      component: Generate
    },
    {
      path: '/Song',
      name: 'Song',
      component: Song
    }
  ]
})
