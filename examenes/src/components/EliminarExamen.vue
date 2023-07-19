<template lang="es">
    <div>
        <Card class="text-gray-800 font-sans">
            <label class="text-green-600" for=""><strong>Datos de la persona</strong></label>
            <div class="flex flex-wrap gap-4">
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
                    <label for=""><strong>ID</strong></label><br>
                    <input disabled="true" class="px-1  rounded-md" type="text" v-model="_examen.id">
                </div>
                <div>
                    <label for=""><strong>Estado del examen</strong></label><br>
                    <input disabled="true" class="px-1  rounded-md" type="text" v-model="_examen.estado">
                </div>
                <div>
                    <label for=""><strong>Titulo</strong></label><br>
                    <input disabled="true" class="px-1 rounded-md" type="text" v-model="_examen.examen" required="true" maxlength="200">
                </div>
                <div>
                    <label for=""><strong>Motivo</strong></label><br>
                    <textarea disabled="true" class="px-1 rounded-md sm:w-80" v-model="_examen.motivo" rows="2" maxlength="500"></textarea>
                </div>
                <div>
                    <label for=""><strong>Fecha de ingreso</strong></label><br>
                    <input disabled="true" class="px-1 rounded-md" type="date" v-model="_examen.fecha_realiza">
                </div>
                <div>
                    <label for=""><strong>Observacion</strong></label><br>
                    <textarea disabled="true" class="px-1 rounded-md sm:w-80" placeholder="pendiente" v-model="_examen.observacion" rows="2" maxlength="500"></textarea>
                </div>
            </div>
        </Card>
        <br>
        <div v-if="eliminando" class="flex bg-gray-300 rounded-lg gap-2 text-gray-800 w-fit p-2">
            <label class="italic" for=""><strong>Eliminando examen...</strong></label>
            <img class="w-6 h-6 animate-spin" :src="arrows_rotate" alt="arrows rotate">
        </div>
        <br>
        <div v-if="mostrar_eliminar">
            <button class="bg-red-600 p-2 rounded-lg active:bg-red-800" @click="eliminar">Eliminar Examen</button>
        </div>
        <div v-if="!mostrar_eliminar">
            <label class="italic" for=""><strong>Seleccione un examen para poder eliminarlo</strong></label>
        </div>
        <br>
    </div>
</template>
<script>
import { examen } from '../variables/examen';
import { ExamenService } from '../variables/servicios';
import Card from '../components/ui/Card.vue';
import { arrows_rotate } from '../variables/svg';

export default {
    name:'EliminarExamen',
    components:{
        Card
    },
    data() {
        return {
            examen: examen(),
            arrows_rotate,
            _examen: {},
            _persona: {},
            mostrar_eliminar: false,
            eliminando: false,
        }
    },
    methods: {
        cargar_datos() {
            try {
                this._examen = this.examen.examen ?? { id: '', examen: '', institucion: '', estado: '', motivo: '', observacion: '', fecha_realiza: '' };
                this._persona = this.examen.persona ?? { nombres:'', apellidos:'' };
            } catch (error) { }
            if(this._examen.id == undefined || this._examen.id == ''){
                this.mostrar_eliminar = false;
            }else{
                this.mostrar_eliminar = true;
            }
        },
        async eliminar(){
            this.eliminando = true;
            await ExamenService.delete(this._examen.id);
            this.examen.eliminarExamen();
            this.cargar_datos();
            this.eliminando = false;
        }
    },
    mounted() {
        this.cargar_datos();
    },
}
</script>