import BootstrapVue from 'bootstrap-vue'
import '@/../bootstrap/css/bootstrap.css'
import 'bootstrap'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
