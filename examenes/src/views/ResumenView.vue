<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="mx-5 sm:mx-24">
            <DetalleExamen :id_examen="id_examen"></DetalleExamen>
            este es el resumen
        </div>
    </div>
</template>
<script>
import DetalleExamen from '../components/DetalleExamen.vue';
import Toolbar from '@/components/ui/Toolbar.vue';
import {registro, login} from '../variables/rutas';
import { descifrar } from '../variables/funciones';
 
export default {
    name:'ResumenView',
    components:{
        Toolbar, DetalleExamen
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
            id_examen: 0
        }
    },
    methods: {
        capturar_cifrado(){
            let cifrado = this.$route.params.id;
            let descifrado = descifrar(cifrado, 'examenes');
            // this.id_examen = JSON.parse(descifrado);
            this.id_examen = descifrado;
            console.log(this.id_examen);
        }
    },
    beforeMount() {
        this.capturar_cifrado();
    },
}
</script>