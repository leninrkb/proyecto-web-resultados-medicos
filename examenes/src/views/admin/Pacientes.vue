<template lang="es">
    <h3 class="text-gray-200 font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
    <br>
    <Tabla :mostrar="termino_pacientes" :datos="pacientes"></Tabla>
</template>
<script>
import Tabla from '../../components/ui/Tabla.vue';
import axios from 'axios';
import { get_pacientes } from '../../variables/rutas';
export default {
    name:'Pacientes',
    components:{
        Tabla
    },
    data() {
        return {
            pacientes:{titulos:undefined, registros:undefined},
            termino_pacientes: false
        }
    },
    methods: {
        cargar_pacientes(){
            this.termino_pacientes = false;
            try {
                axios.get(get_pacientes).then(resp => {
                    this.pacientes.titulos = ['id','cedula','nombres','apellidos','fecha_nacimiento','id_genero'];
                    this.pacientes.registros = resp.data.result;
                    this.termino_pacientes = true;
                }).catch(error => {
                    this.termino_pacientes = true;
                 });
            } catch (error) {
                this.termino_pacientes = true;
            }
        }
    },
    mounted() {
        this.cargar_pacientes();
    },
}
</script>
