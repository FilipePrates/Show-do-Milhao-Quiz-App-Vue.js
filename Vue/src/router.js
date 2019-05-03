import Vue from 'vue'
import Router from 'vue-router'
import Cabecario from './components/Cabecario.vue'
import Pergunta from './components/Pergunta.vue'
import Ajudas from './components/Ajudas.vue'
import Respostas from './components/Respostas.vue'
import Quiz from './components/Quiz.vue'
import BottomNav from './components/BottomNav'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { path: '/', name: 'App', component: App },
    { path: '/info', name: 'Info', component: Cabecario},
    { path: '*', redirect: '/' }
  ]
})
