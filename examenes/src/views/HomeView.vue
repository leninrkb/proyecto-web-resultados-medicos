<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="mx-5 sm:mx-24">
            <div class="p-3 text-gray-200 text-xl font-sans ">
                {{$route.params.id}}
                <h2 class="text-4xl font-sans">Somos <strong>{{institucion.institucion}}</strong></h2>
                <img class="rounded-lg m-2" :src="institucion.path_img" alt="logo">
                <h3>{{institucion.razon_social}}</h3>
                <br>
                <div class="border-l-4 border-teal-500 pl-2">
                    <h3><strong>Quienes somos ?</strong></h3>
                    <p class="text-justify text-lg">{{institucion.descripcion}}</p>
                    <br>
                    <h3 class=" ">Encuentranos en: {{institucion.ubicacion}}</h3>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Toolbar from '@/components/ui/Toolbar.vue';
import {registro, examenes_disponibles, login} from '../variables/rutas';
import { InstitucionService } from '../variables/servicios';

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
            },
            institucion: {institucion:''}
        }
    },
    methods: {
        async cargar_institucion(){
            this.institucion = await InstitucionService.get_instituciones();
            this.institucion = this.institucion[0];
            this.datos.titulo = this.institucion.institucion;
            console.log(this.institucion);
        }
    },
    mounted() {
        this.cargar_institucion();
    },
}
</script>