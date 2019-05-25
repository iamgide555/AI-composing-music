import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Signup from '@/components/Signup'
import Test from '@/components/Test'
import Test2 from '@/components/Test2'
import Generate from '@/components/Generate'
import Example from '@/components/Example'
import testTee from '@/components/testTee'
import PlaySound from '@/components/PlaySound'
import List from '@/components/List'

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
      path: '/example',
      name: 'Example',
      component: Example
    },
    {
      path: '/testTee',
      name: 'testtt',
      component: testTee
    },
    {
      path: '/PlaySound',
      name: 'PlaySound',
      component: PlaySound
    },
    {
      path: '/List',
      name: 'List',
      component: List
    }
  ]
})
