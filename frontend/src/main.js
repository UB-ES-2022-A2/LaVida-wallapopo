import BootstrapVue from 'bootstrap-vue'
import '@/../bootstrap/css/bootstrap.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { library } from '@fortawesome/fontawesome-svg-core'

import {
  faUserSecret,
  faHeart,
  faUserCircle,
  faMagnifyingGlass,
  faEnvelope,
  faCirclePlus,
  faTruckFast,
  faCar,
  faMotorcycle,
  faHelmetSafety,
  faShirt,
  faTv,
  faMobile,
  faComputer,
  faVolleyball,
  faBicycle,
  faGamepad,
  faHouse,
  faFireBurner,
  faFilm,
  faBook,
  faBaby,
  faCoins,
  faTrowelBricks,
  faSeedling,
  faEllipsis
} from '@fortawesome/free-solid-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(
  faUserSecret,
  faHeart,
  faUserCircle,
  faMagnifyingGlass,
  faEnvelope,
  faCirclePlus,
  faTruckFast,
  faCar,
  faMotorcycle,
  faHelmetSafety,
  faShirt,
  faTv,
  faMobile,
  faComputer,
  faVolleyball,
  faBicycle,
  faGamepad,
  faHouse,
  faFireBurner,
  faFilm,
  faBook,
  faBaby,
  faCoins,
  faTrowelBricks,
  faSeedling,
  faEllipsis
)

Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.component('font-awesome-icon', FontAwesomeIcon)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
