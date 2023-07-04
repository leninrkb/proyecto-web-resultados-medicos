<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="p-3 text-gray-400">
            Login
            - login
        </div>
    </div>
</template>
<script>
import Toolbar from '@/components/ui/Toolbar.vue';
import {registro, examenes_disponibles, home} from '../variables/rutas';
export default {
    name: 'LoginView',
    components:{
        Toolbar
    },
    data(){
        return{
            datos:{
                titulo:'Biolab',
                enlaces:[
                    {
                        titulo: 'Examenes',
                        ruta: examenes_disponibles
                    }
                ],
                primarios:[
                    {
                        titulo:'Registrarse',
                        ruta: registro
                    },
                    {
                        titulo:'Regresar',
                        ruta: home
                    }
                ]
            }
        }
    }
}
</script>