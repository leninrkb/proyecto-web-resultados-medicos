<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos="datos_toolbar"></Toolbar>
        <div class="flex flex-row-reverse px-3 mt-2 gap-2 text-gray-400">
            <button class="animation ease-in-out duration-300 ring-teal-600 hover:ring
            hover:bg-teal-900 hover:text-gray-200
             p-1 rounded-md"
             @click="terminar_sesion"> Terminar sesion </button>
            <div class="flex-grow"></div>
            <h3 class="p-1 text-teal-200"><strong>Bienvenido {{sesion.usuario}}</strong></h3>
        </div>
        <br>
        <div class="mx-5 sm:mx-24">


            <div class="text-gray-200 font-sans">
                <h3 class="font-sans text-xl capitalize">Todos mis examenes</h3>
                <!-- <br> -->
                <!-- <h3><strong>Seleccionado: </strong> {{examen.examen == undefined ? 'ninguno' : 'Examen ID ' + examen.examen.id}}</h3> -->
            </div>
            <Tabla :mostrar="terminado_examenes" :datos="tabla_examenes" @recargar="recargar" @fila="capturar_fila"></Tabla>
            <br>
            <div v-if="mostrar_detalle" class="flex flex-row-reverse">
                <button class="rounded-md bg-red-600 p-1 text-gray-100 hover:bg-red-700" @click="mostrar_detalle = !mostrar_detalle">Cerrar</button>
            </div>
            <DetalleExamen v-if="mostrar_detalle" :id_examen="fila.id" @detalle="capturar_detalle"></DetalleExamen>
        </div>
    </div>
</template>
<script>
import { sesion } from '../../variables/sesion';
import { examen } from '../../variables/examen';
import { home} from '../../variables/rutas';
import Toolbar from '@/components/ui/Toolbar.vue';
import Tabla from '@/components/ui/Tabla.vue';
import DetalleExamen from '../../components/DetalleExamen.vue';
import { InstitucionService, EstadoService, PersonaService, ExamenService, UsuarioService } from '../../variables/servicios';


export default {
    name:'InicioPacienteView',
    components:{
        Toolbar, Tabla, DetalleExamen
    },
    data() {
        return {
            examen: examen(),
            sesion: sesion(),
            datos_toolbar: datos_toolbar,
            mostrar_detalle: false,
            terminado_examenes: false,
            tabla_examenes: { titulos: undefined, registros: [] },
            personas: undefined,
            instituciones: undefined,
            estados: undefined,
            fila: {},
            id_persona: 0

        }
    },
    methods: {
        verificar_sesion(){
            if(this.sesion.usuario == undefined){
            this.$router.push(home);
            }
            if(this.sesion.id_rol != 2){
                this.$router.push(home);
            }
        },
        terminar_sesion(){
            this.sesion.terminarSesion();
            this.verificar_sesion();
        },
        async cargar_examenes() {
            this.terminado_examenes = false;
            try {
                this.tabla_examenes.registros = [];
                this.personas = await PersonaService.get_personas();
                this.instituciones = await InstitucionService.get_instituciones();
                this.estados = await EstadoService.get_estados();
                this.tabla_examenes.titulos = ['id', 'institucion', 'nombres', 'apellidos', 'estado', 'examen', 'motivo', 'fecha_realiza', 'observacion']
                let resp = await ExamenService.get_examenes();
                resp.forEach(element => {
                    if(element.id_persona == this.id_persona){
                        this.tabla_examenes.registros.push(element);
                    }
                });
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
            this.mostrar_detalle = true;
            this.fila = fila;
        },
        capturar_detalle(detalle){
            detalle = JSON.parse(detalle);
            this.examen.setExamen(detalle.examen);
            this.examen.setDetalle(detalle.detalle);
            this.examen.setPersona(detalle.persona);
            this.examen.setInstitucion(detalle.institucion);
            // console.log(detalle);
        }
        
    },
    beforeMount() {
        this.verificar_sesion();
    },
    mounted() {
        this.id_persona = this.sesion.id_persona;
        this.cargar_examenes();
    },
    
    
}
import { examenes_pacientes, administrar, pacientes } from '../../variables/rutas';
const datos_toolbar = {
    titulo: 'biolab',
    enlaces: [ ],
    primarios: [ ]
}
</script>