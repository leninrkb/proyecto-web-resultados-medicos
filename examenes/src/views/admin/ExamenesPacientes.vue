<template lang="es">
    <div class="text-gray-200 font-sans">
        <h3 class="font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
        <br>
        <h3><strong>Seleccionado: </strong> {{examen.examen == undefined ? 'ninguno' : 'Examen ID ' + examen.examen.id}}</h3>
    </div>
    <Tabla :mostrar="terminado_examenes" :datos="tabla_examenes" @recargar="recargar" @fila="capturar_fila"></Tabla>
    <br>
    <div v-if="mostrar_detalle" class="flex flex-row-reverse">
        <button class="rounded-md bg-red-600 p-1 text-gray-100 hover:bg-red-700" @click="mostrar_detalle = !mostrar_detalle">Cerrar</button>
    </div>
    <DetalleExamen v-if="mostrar_detalle" :id_examen="fila.id" @detalle="capturar_detalle"></DetalleExamen>
    <div v-if="mostrar_detalle" class="text-gray-200">
        <Card class="text-gray-800">
            <form  ref="form" @submit.prevent="sendEmail" >
                <div class="flex flex-wrap gap-2">
                    <div>
                        <label><strong>Desde</strong></label><br>
                        <input  class="rounded-md px-2" type="text" name="from_name" v-model="institucion.institucion">
                    </div>
                    <div>
                        <label><strong>Para</strong></label><br>
                        <input  class="rounded-md px-2" type="email" name="to_email" v-model="persona.correo">
                    </div>
                    <div>
                        <label><strong>URL</strong></label><br>
                        <input  class="rounded-md px-2" name="message" v-model="url">
                    </div>
                </div>
                <br>
                <input v-if="!enviando" class="rounded-md bg-blue-600 p-1 text-gray-100 active:bg-blue-800"  type="submit" value="Enviar">
                <div v-else class="w-8 h-8 p-2 animate-spin bg-gray-300 rounded-full">
                    <img :src="arrows_rotate" alt="arrows rotate">
                </div>
                <p class="italic">
                    <strong>{{mensaje_enviado}}</strong>
                </p>
            </form>
        </Card>
    </div>
    

</template>
<script>
import Tabla from '@/components/ui/Tabla.vue';
import DetalleExamen from '../../components/DetalleExamen.vue';
import { InstitucionService, EstadoService, PersonaService, ExamenService } from '../../variables/servicios';
import { examen } from '../../variables/examen';
import emailjs from '@emailjs/browser';
import Card from '../../components/ui/Card.vue';
import { arrows_rotate} from '../../variables/svg';
export default {
    name: 'ExamenesPacientes',
    components: {
        Tabla, DetalleExamen, Card
    },
    data() {
        return {
            arrows_rotate,
            tabla_examenes: { titulos: undefined, registros: undefined },
            terminado_examenes: false,
            personas: undefined,
            instituciones: undefined,
            estados: undefined,
            fila: {},
            mostrar_detalle: false,
            examen: examen(),
            url: '',
            institucion: { institucion: '' },
            persona: { correo: '' },
            enviando: false,
            mensaje_enviado: ''
        }
    },
    methods: {
        sendEmail() {
            this.mensaje_enviado = ''
            this.enviando = true;
            emailjs.sendForm('service_2gt20zb', 'template_654ouel', this.$refs.form, '2JAqEz9uTrOlanGrJ')
                .then((result) => {
                    console.log('SUCCESS!', result.text);
                    this.mensaje_enviado = 'Correo Enviado!'
                    this.enviando = false;

                }, (error) => {
                    console.log('FAILED...', error.text);
                    this.mensaje_enviado = 'Fallo al enviar'
                    this.enviando = false;
                });
        },
        async cargar_examenes() {
            this.terminado_examenes = false;
            try {
                this.personas = await PersonaService.get_personas();
                console.log(this.personas);
                this.instituciones = await InstitucionService.get_instituciones();
                this.estados = await EstadoService.get_estados();
                this.tabla_examenes.titulos = ['id', 'institucion', 'nombres', 'apellidos', 'correo', 'estado', 'examen', 'motivo', 'fecha_realiza', 'observacion']
                this.tabla_examenes.registros = await ExamenService.get_examenes();
                this.tabla_examenes.registros.forEach(element => {
                    let temp = this.personas.find(p => p.id == element.id_persona);
                    element.nombres = temp.nombres;
                    element.apellidos = temp.apellidos;
                    element.correo = temp.correo;
                    temp = this.instituciones.find(p => p.id == element.id_institucion);
                    element.institucion = temp.institucion;
                    temp = this.estados.find(p => p.id == element.id_estado);
                    element.estado = temp.estado;
                });
            } catch (error) { }
            this.terminado_examenes = true;
        },
        recargar() {
            this.cargar_examenes();
        },
        capturar_fila(fila) {
            this.mostrar_detalle = true;
            this.fila = fila;
        },
        capturar_detalle(detalle) {
            detalle = JSON.parse(detalle);
            this.examen.setExamen(detalle.examen);
            this.examen.setDetalle(detalle.detalle);
            this.examen.setPersona(detalle.persona);
            this.examen.setInstitucion(detalle.institucion);
            this.institucion = detalle.institucion;
            this.persona = detalle.persona;
            this.url = detalle.url;
            // console.log(detalle);
        }
    },
    mounted() {
        this.cargar_examenes();
    },
}
</script>