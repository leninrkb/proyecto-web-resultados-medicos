import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegistroView from '../views/RegistroView.vue'
import ExamenesView from '../views/ExamenesView.vue'
import LoginView from '../views/LoginView.vue'
import InicioView from '../views/admin/InicioView.vue'
import ExamenesPacientes from '../views/admin/ExamenesPacientes.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/registro',
    name: 'registro',
    component: RegistroView
  },
  {
    path: '/examenes_disponibles',
    name: 'examenes_disponibles',
    component: ExamenesView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/inicio',
    name: 'inicio',
    component: InicioView,
    children:[
      {
        path:'examenes',
        name:'examenes',
        component: ExamenesPacientes
      },
    ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
