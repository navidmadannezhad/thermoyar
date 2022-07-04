import Vue from 'vue'
import VueRouter from 'vue-router'
import saturated from '../components/saturated.vue'
import superHeat from '../components/superHeat.vue'
import compressed from '../components/compressed.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/saturated',
    name: 'saturated',
    component: saturated,
    props: true
  },
  {
    path: '/super-heat',
    name: 'superHeat',
    component: superHeat,
    props: true
  },
  {
    path: '/compressed',
    name: 'compressed',
    component: compressed,
    props: true
  },
]

const router = new VueRouter({
  routes
})

export default router
