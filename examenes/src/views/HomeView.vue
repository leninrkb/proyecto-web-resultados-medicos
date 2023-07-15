<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="mx-5 sm:mx-24">
        <div class="p-3 text-gray-400">
            HOME
            - portada de bienvenida
        </div>
    </div>
    </div>
</template>
<script>
import Toolbar from '@/components/ui/Toolbar.vue';
import {registro, examenes_disponibles, login} from '../variables/rutas';
export default {
    name: 'HomeView',
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
                        titulo:'Iniciar Sesion',
                        ruta: login
                    }
                ]
            }
        }
    }
}
</script>