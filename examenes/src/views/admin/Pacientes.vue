<template lang="es">
    <h3 class="text-gray-200 font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
    <br>
    <Tabla :mostrar="termino_pacientes" :datos="pacientes" @recargar="recargar"></Tabla>
</template>
<script>
import Tabla from '../../components/ui/Tabla.vue';
import axios from 'axios';
import { get_personas } from '../../variables/rutas';
import { GeneroService, PersonaService } from '../../variables/servicios';

export default {
    name: 'Pacientes',
    components: {
        Tabla
    },
    data() {
        return {
            pacientes: { titulos: undefined, registros: undefined },
            termino_pacientes: false,
            generos: undefined
        }
    },
    methods: {
        async cargar_personas() {
            this.termino_pacientes = false;
            try {
                this.generos = await GeneroService.get_generos();
                this.pacientes.titulos = ['id', 'cedula', 'nombres', 'apellidos', 'fecha_nacimiento', 'genero'];
                this.pacientes.registros = await PersonaService.get_personas();
                this.pacientes.registros.forEach(element => {
                    let genero_tmp = this.generos.find(genero => genero.id == element.id_genero);
                    element.genero = genero_tmp.genero;
                });
                this.termino_pacientes = true;
            } catch (error) {
                this.termino_pacientes = true;
            }
        },
        recargar(){
            this.cargar_personas();
        }
    },
    mounted() {
        this.cargar_personas();
    },
}
</script>