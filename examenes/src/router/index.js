import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegistroView from '../views/RegistroView.vue'
import ExamenesView from '../views/ExamenesView.vue'
import LoginView from '../views/LoginView.vue'
import InicioView from '../views/admin/InicioView.vue'
import ExamenesPacientes from '../views/admin/ExamenesPacientes.vue'
import AdministrarExamenes from '../views/admin/AdministrarExamenes.vue'
import Pacientes from '../views/admin/Pacientes.vue'
import ResumenView from '../views/ResumenView.vue'
import FormExamen from '../components/FormExamen.vue'
import FormDetalle from '../components/FormDetalle.vue'
import EliminarExamen from '../components/EliminarExamen.vue'
import InicioPaciente from '../views/paciente/InicioPaciente.vue'

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
    path: '/resumen',
    name: 'resumen',
    component: ResumenView
  },
  {
    path: '/resumen/:id',
    name: 'resumen',
    component: ResumenView
  },
  {
    path: '/inicio_paciente',
    name: 'inicio_paciente',
    component: InicioPaciente
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
      {
        path:'administrar',
        name:'administrar',
        component: AdministrarExamenes,
        children:[
          {
            path:'nuevo_examen',
            name:'nuevo_examen',
            component: FormExamen
          },
          {
            path:'nuevo_detalle',
            name:'nuevo_detalle',
            component: FormDetalle
          },
          {
            path:'eliminar_examen',
            name:'eliminar_examen',
            component: EliminarExamen
          },
        ]
      },
      {
        path:'pacientes',
        name:'pacientes',
        component: Pacientes
      },
    ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
