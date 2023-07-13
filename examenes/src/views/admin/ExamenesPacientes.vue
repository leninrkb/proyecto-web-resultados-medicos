<template lang="es">
    <h3 class="text-gray-200 font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
    <br>
    <Tabla :mostrar="terminado_examenes" :datos="tabla_examenes" @recargar="recargar" @fila="capturar_fila"></Tabla>
</template>
<script>
import Tabla from '@/components/ui/Tabla.vue';
import axios from 'axios';
import { get_examenes, get_personas, get_instituciones, get_estados} from '../../variables/rutas';

export default {
    name: 'ExamenesPacientes',
    components:{
        Tabla
    },
    data() {
        return {
            tabla_examenes:{titulos:undefined, registros:undefined},
            terminado_examenes: false,
            personas: undefined,
            instituciones: undefined,
            estados: undefined,
        }
    },
    methods: {
        cargar_examenes() {
            this.terminado_examenes = false;
            try {
                this.cargar_personas();
                this.cargar_instituciones();
                this.cargar_estados();
                axios.get(get_examenes).then(resp => {
                    this.tabla_examenes.titulos = ['id', 'institucion', 'nombres','apellidos', 'estado', 'examen', 'motivo', 'fecha_realiza', 'observacion']
                    this.tabla_examenes.registros = resp.data.result;
                    this.tabla_examenes.registros.forEach(element => {
                        let temp = this.personas.find(p => p.id == element.id_persona);
                        element.nombres = temp.nombres;
                        element.apellidos = temp.apellidos;
                        temp = this.instituciones.find(p => p.id == element.id_institucion);
                        element.institucion = temp.institucion;
                        temp = this.estados.find(p => p.id == element.id_estado);
                        element.estado = temp.estado;
                    });
                    this.terminado_examenes = true;
                }).catch(error => {
                    this.terminado_examenes = true;
                });
            } catch (error) {
                this.terminado_examenes = true;
            }
        },
        cargar_personas(){
            try {
                axios.get(get_personas).then(resp => {
                    this.personas = resp.data.result;
                }).catch(error => {

                });
            } catch (error) {
                
            }
        },
        cargar_instituciones(){
            try {
                axios.get(get_instituciones).then(resp => {
                    this.instituciones = resp.data.result;
                }).catch(error => {

                });
            } catch (error) {
                
            }
        },
        cargar_estados(){
            try {
                axios.get(get_estados).then(resp => {
                    this.estados = resp.data.result;
                }).catch(error => {

                });
            } catch (error) {
                
            }
        },
        recargar(){
            this.cargar_examenes();
        },
        capturar_fila(fila){
            console.log(fila);
        }
    },
    mounted() {
        this.cargar_examenes();
    },
}
</script>