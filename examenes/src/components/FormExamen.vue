<template lang="es">
    <div>
        <div class="flex flex-wrap gap-2">
            <button class="bg-green-600 rounded-lg p-1 active:bg-green-800" @click="cargar_examen">Cargar examen</button>
            <button class="bg-green-600 rounded-lg p-1 active:bg-green-800" @click="guardar_borrador">Guardar borrador</button>
        </div>
        <form action="">
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
                        <Combo llave="institucion" :peticion="get_instituciones" id_prop="1"  @emitido="capturar_evento('institucion',$event)"></Combo>
                    </div>
                    <div>
                        <label for=""><strong>Estado del examen</strong></label><br>
                        <Combo llave="estado" :peticion="get_estados" id_prop="3"  @emitido="capturar_evento('institucion',$event)"></Combo>
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
                        <input class="px-1 rounded-md" type="date" v-model="_examen.fecha_realiza">
                    </div>
                    <div>
                        <label for=""><strong>Observacion</strong></label><br>
                        <textarea class="px-1 rounded-md sm:w-80" placeholder="pendiente" v-model="_examen.observacion" rows="3" maxlength="500"></textarea>
                    </div>
                </div>
                <br>
                <div class="text-gray-200">
                    <button type="submit" class="bg-cyan-500 rounded-lg p-1 active:bg-cyan-800" @click="guardar_examen">Guardar nuevo examen</button>
                </div>
            </Card>
        </form>
    </div>
</template>
<script>
import Card from './ui/Card.vue';
import Combo from './ui/Combo.vue';
import { get_instituciones, get_estados } from '../variables/rutas';
import { examen } from '../variables/examen';
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
            get_instituciones,
            get_estados,
            _examen: {},
            _detalle: [],
            _persona: { },
            examen: examen()
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
        guardar_examen(){
            let nuevo = {};
            nuevo.id_institucion = this._examen.id_institucion;
            nuevo.id_estado = this._examen.id_estado;
            nuevo.id_persona = this._persona.id;
            nuevo.examen = this._examen.examen;
            nuevo.motivo = this._examen.motivo;
            nuevo.fecha_realiza = this._examen.fecha_realiza;
            nuevo.observacion = this._examen.observacion;


            console.log(nuevo);
        },
        capturar_evento(tipo, evento){
            console.log(tipo);
            console.log(evento);
        },
    },
    beforeMount() {
        this.cargar_datos();
    },
}
</script>