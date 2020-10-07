import Vue from 'vue'
// import Vuex from 'vuex'
import Router from 'vue-router'


import Join from '../page/user/Join.vue'
import Login from '../page/user/Login.vue'
import Home from '../page/Home.vue'
import Favorites from '../page/user/Favorites.vue'
import Recommend from '../page/post/Recommend.vue'
import List from '../page/post/List.vue'
import TonicDetail from '../page/post/TonicDetail.vue'
Vue.use(Router)
// Vue.use(Vuex)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/user/join',
      name: 'Join',
      component: Join
    },
    {
      path: '/user/favorites',
      name: 'favorites',
      component: Favorites
    },
    {
      path: '/user/login',
      // name: constants.URL_TYPE.USER.JOIN,
      name: 'login',
      component: Login
    },
    {
      path: '/list',
      name: 'List',
      component: List
    },
    {
      path: `/list/:tonic_pk`,
      name: 'TonicDetail',
      component: TonicDetail
    },
    {
      path: '/recommend',
      name: 'Recommend',
      component: Recommend
    },
  ]
})


