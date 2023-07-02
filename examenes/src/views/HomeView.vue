<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
    </div>
</template>
<script>
import Toolbar from '@/components/ui/Toolbar.vue'
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
                    'Examenes disponibles','Precios'
                ],
                primarios:[
                    'Ingresar','Registrarse'
                ]
            }
        }
    }
}
</script>