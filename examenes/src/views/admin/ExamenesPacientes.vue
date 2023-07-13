<template lang="es">
    <h3 class="text-gray-200 font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
    <br>
    <!--I  -->
    <Tabla v-if="terminado" :datos="tabla_examenes" @emitido="emitido_tabla"></Tabla>
    <div v-else class="w-10 h-10 p-2 mx-auto animate-spin bg-gray-300 rounded-full">
        <img :src="arrows_rotate" alt="arrows rotate">
    </div>
    <!--F  -->

</template>
<script>
import Tabla from '@/components/ui/Tabla.vue';
import axios from 'axios';
import { get_examenes} from '../../variables/rutas';
import { arrows_rotate } from "../../variables/svg";


export default {
    name: 'ExamenesPacientes',
    components:{
        Tabla
    },
    data() {
        return {
            tabla_examenes:{titulos:undefined, registros:undefined},
            arrows_rotate: arrows_rotate,
            terminado: false
        }
    },
    methods: {
        traer_examenes() {
            this.terminado = false;
            try {
                this.tabla_examenes.titulos = ['id', 'id_institucion', 'id_persona', 'id_estado', 'examen', 'motivo', 'fecha_realiza', 'observacion']
                axios.get(get_examenes).then(resp => {
                    this.tabla_examenes.registros = resp.data.result;
                    this.terminado = true;
                }).catch(error => {
                    this.terminado = true;
                });
            } catch (error) {
                this.terminado = true;
            }
        },
        emitido_tabla(){
            this.traer_examenes();
        }
    },
    mounted() {
        this.traer_examenes();
    },
}
</script>