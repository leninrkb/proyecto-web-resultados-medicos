<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos="datos_toolbar"></Toolbar>
        <div class="flex flex-row-reverse px-3 mt-2 gap-2 text-gray-400">
            <button class="animation ease-in-out duration-300 ring-teal-600 hover:ring
            hover:bg-teal-900 hover:text-gray-200
             p-1 rounded-md"
             @click="terminar_sesion"> Terminar sesion </button>
            <div class="flex-grow"></div>
            <h3 class="p-1 text-teal-200"><strong>Bienvenido {{sesion.usuario}}</strong></h3>
        </div>
        <br>
        <div class="mx-5 sm:mx-24">
            <router-view></router-view>
        </div>
    </div>
</template>
<script>
import { sesion } from '../../variables/sesion';
import { home} from '../../variables/rutas';
import Toolbar from '@/components/ui/Toolbar.vue';

export default {
    name:'InicioView',
    components:{
        Toolbar
    },
    data() {
        return {
            sesion: sesion(),
            datos_toolbar: datos_toolbar
        }
    },
    methods: {
        verificar_sesion(){
            if(this.sesion.usuario == undefined){
            this.$router.push(home);
            }
            if(this.sesion.id_rol != 1){
                this.$router.push(home);
            }
        },
        terminar_sesion(){
            this.sesion.terminarSesion();
            this.verificar_sesion();
        },
        
    },
    beforeMount() {
        this.verificar_sesion();
    },
    
    
}
import { examenes_pacientes, administrar, pacientes } from '../../variables/rutas';
const datos_toolbar = {
    titulo: 'biolab',
    enlaces: [
        {
            titulo: 'Examenes de pacientes',
            ruta: examenes_pacientes
        },
        {
            titulo: 'Examenes',
            ruta: administrar
        },
        {
            titulo: 'Pacientes',
            ruta: pacientes
        },
    ],
    primarios: [ ]
}
</script>