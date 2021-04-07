import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
import App from './App'
import axios from 'axios'
import VueAxios from 'vue-axios'
import all from './js/all.js'
import store from './store'
Vue.use(VueAxios, axios, all, Vuex)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')