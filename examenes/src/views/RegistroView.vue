<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="p-3 text-gray-400">
            Registro
            - form de registro
        </div>
    </div>
</template>
<script>
import Toolbar from '@/components/ui/Toolbar.vue';
import {home} from '../variables/rutas';
export default {
    name:'RegistroView',
    components:{
        Toolbar
    },
    data() {
        return {
            datos:{
                titulo:'Biolab',
                enlaces:[
                    'Examenes disponibles','Precios'
                ],
                primarios:[
                    {
                        titulo:'Regresar',
                        ruta: home
                    }
                ]
            }
        }
    },
}
</script>