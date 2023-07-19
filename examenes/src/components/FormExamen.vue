<template lang="es">
    <div>
        <div class="flex flex-wrap gap-2">
            <button class="bg-green-600 rounded-lg p-1 active:bg-green-800" @click="cargar_examen">Cargar examen</button>
            <button class="bg-green-600 rounded-lg p-1 active:bg-green-800" @click="guardar_borrador">Guardar borrador</button>
        </div>
            <Card class="text-gray-800 font-sans">
                <label class="text-green-600" for=""><strong>Datos de la persona</strong></label>
                <div class="flex flex-wrap gap-4">
                    <div>
                        <label for=""><strong>ID</strong></label><br>
                        <input disabled="true" class="px-1 w-10 rounded-md" type="text" v-model="_persona.id">
                    </div>
                    <div>
                        <label for=""><strong>Cedula</strong></label><br>
                        <input disabled="true" class="px-1  rounded-md" type="text" v-model="_persona.cedula">
                    </div>
                    <div>
                        <label for=""><strong>Nombres</strong></label><br>
                        <input disabled="true" class="px-1  rounded-md" type="text" v-model="_persona.nombres">
                    </div>
                    <div>
                        <label for=""><strong>Apellidos</strong></label><br>
                        <input disabled="true" class="px-1  rounded-md" type="text" v-model="_persona.apellidos">
                    </div>
                </div>

                <br>
                <label class="text-green-600" for=""><strong>Sobre el examen</strong></label>
                <div class="flex flex-wrap gap-4">
                    <div>
                        <label for=""><strong>Institucion</strong></label><br>
                        <Combo llave="institucion" :peticion="get_instituciones" id_prop="1"  @emitido="capturar_evento('_id_institucion',$event)"></Combo>
                    </div>
                    <div>
                        <label for=""><strong>Estado del examen</strong></label><br>
                        <Combo llave="estado" :peticion="get_estados" id_prop="1"  @emitido="capturar_evento('_id_estado',$event)"></Combo>
                    </div>
                    <div>
                        <label for=""><strong>Titulo</strong></label><br>
                        <input class="px-1 rounded-md" type="text" v-model="_examen.examen" required="true" maxlength="200">
                    </div>
                    <div>
                        <label for=""><strong>Motivo</strong></label><br>
                        <textarea class="px-1 rounded-md sm:w-80" v-model="_examen.motivo" rows="3" maxlength="500"></textarea>
                    </div>
                    <div>
                        <label for=""><strong>Fecha de ingreso</strong></label><br>
                        <input class="px-1 rounded-md" type="date" required="true"  v-model="_examen.fecha_realiza">
                    </div>
                    <div>
                        <label for=""><strong>Observacion</strong></label><br>
                        <textarea class="px-1 rounded-md sm:w-80"  v-model="_examen.observacion" rows="3" maxlength="500"></textarea>
                    </div>
                </div>
                <br>
                <div v-if="!guardando_examen" class="text-gray-200">
                    <button type="submit" class="bg-cyan-500 rounded-lg p-1 active:bg-cyan-800" @click="guardar_examen">Guardar nuevo examen</button>
                </div>
                <div v-else class="w-9 h-9 animate-spin p-2 bg-gray-300 rounded-full">
                    <img :src="arrows_rotate" alt="arrows rotate">
                </div>
                <br>
                <div class="italic">
                    <p><strong>{{mensaje_examen}}</strong></p>
                </div>
            </Card>
    </div>
</template>
<script>
import Card from './ui/Card.vue';
import Combo from './ui/Combo.vue';
import { get_instituciones, get_estados } from '../variables/rutas';
import { examen } from '../variables/examen';
import { ExamenService } from '../variables/servicios';
import { arrows_rotate } from '../variables/svg';
export default {
    name:'FormExamen',
    props:{
        datos:{
            type: Object,
            required: true
        }
    },
    components:{
        Combo, Card
    },
    data() {
        return {
            arrows_rotate: arrows_rotate,
            get_instituciones,
            get_estados,
            _examen: { },
            _detalle: [],
            _persona: { },
            examen: examen(),
            guardando_examen: false,
            mensaje_examen: '',
            _id_estado: 0,
            _id_institucion: 0
        }
    },
    methods: {
        cargar_datos(){
            try {
                this._examen = {examen: '', motivo: '', observacion: '', fecha_realiza:''};
                this._persona = this.examen.persona ?? { id: -1, cedula: 'ninguno', nombres: 'ninguno', apellidos: 'ninguno'};
            } catch (error) { }
        },
        cargar_examen(){
            try {
                this._examen = this.examen.examen ?? {examen: '', motivo: '', observacion: '', fecha_realiza:''};
                this._detalle = this.examen.detalle;
            } catch (error) { }
        },
        guardar_borrador(){
            console.log(this._examen);
            this.examen.setExamen(this._examen);
            this.examen.setDetalle(this._detalle);
        },
        async guardar_examen(){
            try {
                this.mensaje_examen = '';
                if(this._persona.id != -1){
                    if(this.validar_campos()){
                        this.guardando_examen = true;
                        let nuevo = {};
                        nuevo.id = 0;
                        nuevo.id_institucion = this._id_institucion;
                        nuevo.id_estado = this._id_estado;
                        nuevo.id_persona = this._persona.id;
                        nuevo.examen = this._examen.examen;
                        nuevo.motivo = this._examen.motivo ?? '-';
                        nuevo.fecha_realiza = this._examen.fecha_realiza;
                        nuevo.observacion = this._examen.observacion ?? '-';
                        await ExamenService.create_examen(nuevo).then(resp => {
                            this.mensaje_examen = 'examen guardado!';
                            this.examen.setExamen(resp);
                        }).catch(error => {
                            this.mensaje_examen = error;
                        });
                        this.guardando_examen = false;
                    }
                }else{
                    this.mensaje_examen = 'seleccione una paciente';
                }
            } catch (error) {
                console.log(error);
             }
        },
        validar_campos(){
            let regex = /^(.+)$/;
            if(!regex.test(this._examen.examen)){
                this.mensaje_examen += 'Ingrese un titulo. '
                return false;
            }
            if(!regex.test(this._examen.fecha_realiza)){
                this.mensaje_examen += 'Indique la fecha. '
                return false;
            }
            return true;
        },
        capturar_evento(tipo, id){
            this[tipo] = id;
        },
    },
    beforeMount() {
        this.cargar_datos();
    },
}
</script>