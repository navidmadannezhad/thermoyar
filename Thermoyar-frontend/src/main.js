import Vue from 'vue'
import router from './router'
import App from './App.vue';
import RingLoader from 'vue-spinner/src/RingLoader.vue';
import axios from 'axios'
import VueAxios from 'vue-axios'
import store from '../store/index.js';

Vue.component('ring-loader', RingLoader);

Vue.use(VueAxios, axios);

Vue.config.productionTip = false

let appExists = document.querySelector('#app') != undefined;
if(appExists){
  new Vue({
    router,
    store,
    render: h => h(App),
  }).$mount('#app')
}

