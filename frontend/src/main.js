import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import store from './store'
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)
Vue.config.productionTip = false

Vue.prototype.$axios = axios

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
