<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="mx-5 sm:mx-24">
            <div class="p-3 text-gray-400">
                resumen
                - portada de bienvenida
            </div>
        </div>
    </div>
</template>
<script>
import Toolbar from '@/components/ui/Toolbar.vue';
import {registro, login} from '../variables/rutas';

export default {
    name:'ResumenView',
    components:{
        Toolbar
    },
    data() {
        return {
            datos:{
                titulo:'Biolab',
                enlaces:[ ],
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
            },
            hash: undefined
        }
    },
    methods: {
        
    },
    mounted() {
        this.hash = this.$route.params.id;
        
    },
}
</script>