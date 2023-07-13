<template lang="es">
    <h3 class="text-gray-200 font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
    <br>
    <Tabla :mostrar="terminado_examenes" :datos="tabla_examenes" @recargar="recargar" @fila="capturar_fila"></Tabla>
</template>
<script>
import Tabla from '@/components/ui/Tabla.vue';
import axios from 'axios';
import { get_examenes} from '../../variables/rutas';

export default {
    name: 'ExamenesPacientes',
    components:{
        Tabla
    },
    data() {
        return {
            tabla_examenes:{titulos:undefined, registros:undefined},
            terminado_examenes: false
        }
    },
    methods: {
        async traer_examenes() {
            this.terminado_examenes = false;
            try {
                this.tabla_examenes.titulos = ['id', 'id_institucion', 'id_persona', 'id_estado', 'examen', 'motivo', 'fecha_realiza', 'observacion']
                await axios.get(get_examenes).then(resp => {
                    this.tabla_examenes.registros = resp.data.result;
                    this.terminado_examenes = true;
                }).catch(error => {
                    this.terminado_examenes = true;
                });
            } catch (error) {
                this.terminado_examenes = true;
            }
        },
        recargar(){
            this.traer_examenes();
        },
        capturar_fila(fila){
            console.log(fila);
        }
    },
    mounted() {
        this.traer_examenes();
    },
}
</script>