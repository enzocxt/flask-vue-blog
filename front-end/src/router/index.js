import Vue from 'vue'
import Router from 'vue-router'
import Tic from '@/components/Tic'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Tic',
      component: Tic
    }
  ]
})
