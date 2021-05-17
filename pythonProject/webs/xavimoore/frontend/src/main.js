import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
import App from './App'
import axios from 'axios'
import VueAxios from 'vue-axios'
import all from './js/all.js'
import store from './store'
import GeneralHeader from './layout/GeneralHeader'
import GeneralFooter from './layout/GeneralFooter'
Vue.component('GeneralHeader', GeneralHeader)
Vue.component('GeneralFooter', GeneralFooter)
import AdminHeader from './layout/BackendHeader'
import AdminFooter from './layout/GeneralFooter'
Vue.component('AdminHeader',AdminHeader)
Vue.component('AdminFooter', AdminFooter)
import PanelHeader from './layout/GeneralHeader'
import PanelFooter from './layout/GeneralFooter'
Vue.component('PanelHeader',PanelHeader)
Vue.component('PanelFooter', PanelFooter)
Vue.use(VueAxios, axios, all, Vuex)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')