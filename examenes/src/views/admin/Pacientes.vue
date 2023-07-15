<template lang="es">
    <h3 class="text-gray-200 font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
    <br>
    <Tabla :mostrar="termino_pacientes" :datos="pacientes"></Tabla>
</template>
<script>
import Tabla from '../../components/ui/Tabla.vue';
import axios from 'axios';
import { get_personas, get_generos } from '../../variables/rutas';
export default {
    name:'Pacientes',
    components:{
        Tabla
    },
    data() {
        return {
            pacientes:{titulos:undefined, registros:undefined},
            termino_pacientes: false,
            generos: undefined
        }
    },
    methods: {
        cargar_personas(){
            this.termino_pacientes = false;
            try {
                this.cargar_generos();
                axios.get(get_personas).then(resp => {
                    this.pacientes.titulos = ['id','cedula','nombres','apellidos','fecha_nacimiento','genero'];
                    this.pacientes.registros = resp.data.result;
                    this.pacientes.registros.forEach(element => {
                        let genero_tmp = this.generos.find(genero => genero.id == element.id_genero);
                        element.genero = genero_tmp.genero;
                    });
                    this.termino_pacientes = true;
                }).catch(error => {
                    this.termino_pacientes = true;
                });
            } catch (error) {
                this.termino_pacientes = true;
            }
        },
        cargar_generos(){
            try {
                axios.get(get_generos).then(resp => {
                    this.generos = resp.data.result;
                }).catch(error => { });
            } catch (error) {
                
            }
        }
    },
    mounted() {
        this.cargar_personas();
    },
}
</script>