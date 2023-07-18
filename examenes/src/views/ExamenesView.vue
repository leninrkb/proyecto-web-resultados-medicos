<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="mx-5 sm:mx-24">
            <div class=" text-gray-200">
                <h2 class="text-xl">Examenes disponibles</h2>
            </div>
            <div class="text-gray-200">
                <label for=""><strong>Tipos de examenes</strong></label>
                <Tabla :mostrar="terminado_tipos" :datos="datos_tipos" @recargar="cargar_tipos"></Tabla>
            </div>
        </div>
    </div>
</template>
<script>
import Toolbar from '@/components/ui/Toolbar.vue';
import { registro, login } from '../variables/rutas';
import { TipoExamenService } from '../variables/servicios';
import Tabla from '../components/ui/Tabla.vue';


export default {
    name: 'ExamenesView',
    components: {
        Toolbar, Tabla
    },
    data() {
        return {
            datos: {
                titulo: 'Biolab',
                enlaces: [  ],
                primarios: [
                    {
                        titulo: 'Registrarse',
                        ruta: registro
                    },
                    {
                        titulo: 'Iniciar Sesion',
                        ruta: login
                    },
                ]
            },
            datos_tipos: {},
            terminado_tipos : false,
        }
    },
    methods: {
        async cargar_tipos() {
            this.terminado_tipos = false;
            this.datos_tipos.titulos = ['tipo', 'referencia', 'descripcion', 'precio'];
            this.datos_tipos.registros = await TipoExamenService.get_tipos();
            this.terminado_tipos = true;
        },
    },
    mounted() {
        this.cargar_tipos();
    },
}
</script>