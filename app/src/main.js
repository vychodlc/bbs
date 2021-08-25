import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueScroller  from 'vue-scroller'

Vue.config.productionTip = false

Vue.use(VueScroller)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
