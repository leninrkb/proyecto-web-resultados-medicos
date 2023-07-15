<template lang="es">
    <h3 class="text-gray-200 font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
    <br>
    <Tabla :mostrar="terminado_examenes" :datos="tabla_examenes" @recargar="recargar" @fila="capturar_fila"></Tabla>
    <DetalleExamen :mostrar="mostrar_detalle" :fila="fila"></DetalleExamen>
</template>
<script>
import Tabla from '@/components/ui/Tabla.vue';
import DetalleExamen from '../../components/DetalleExamen.vue';
import axios from 'axios';
import { get_examenes, get_personas, get_instituciones, get_estados } from '../../variables/rutas';
import { InstitucionService, EstadoService, PersonaService, ExamenService } from '../../variables/servicios';

export default {
    name: 'ExamenesPacientes',
    components: {
        Tabla, DetalleExamen
    },
    data() {
        return {
            tabla_examenes: { titulos: undefined, registros: undefined },
            terminado_examenes: false,
            personas: undefined,
            instituciones: undefined,
            estados: undefined,
            mostrar_detalle: false,
            fila: {}
        }
    },
    methods: {
        async cargar_examenes() {
            this.terminado_examenes = false;
            try {
                this.personas = await PersonaService.get_personas();
                this.instituciones = await InstitucionService.get_instituciones();
                this.estados = await EstadoService.get_estados();
                this.tabla_examenes.titulos = ['id', 'institucion', 'nombres', 'apellidos', 'estado', 'examen', 'motivo', 'fecha_realiza', 'observacion']
                this.tabla_examenes.registros = await ExamenService.get_examenes();
                this.tabla_examenes.registros.forEach(element => {
                    let temp = this.personas.find(p => p.id == element.id_persona);
                    element.nombres = temp.nombres;
                    element.apellidos = temp.apellidos;
                    temp = this.instituciones.find(p => p.id == element.id_institucion);
                    element.institucion = temp.institucion;
                    temp = this.estados.find(p => p.id == element.id_estado);
                    element.estado = temp.estado;
                });
            } catch (error) {  }
            this.terminado_examenes = true;
        },
        recargar() {
            this.cargar_examenes();
        },
        capturar_fila(fila) {
            this.mostrar_detalle = false;
            this.fila = fila;
            this.mostrar_detalle = true;
        }
    },
    mounted() {
        this.cargar_examenes();
    },
}
</script>