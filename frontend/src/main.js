import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import store from './store'
import VueCookies from 'vue-cookies'
import GAuth from 'vue-google-oauth2'

Vue.use(VueCookies)
Vue.config.productionTip = false

Vue.prototype.$axios = axios

Vue.use(GAuth, {clientId : '600891788689-357gibaduvtcm85asibhg985p7ck0oko.apps.googleusercontent.com',
  scope: 'profile email'})

window.Kakao.init("f33eb90cf5b5db7c0cf945cacf7cb652");


new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
