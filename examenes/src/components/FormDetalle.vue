<template lang="es">
    <div>
        <!-- <div class="flex flex-wrap gap-2">
            <button class="bg-green-600 rounded-lg p-1 active:bg-green-800" @click="cargar_examen">Cargar examen</button>
            <button class="bg-green-600 rounded-lg p-1 active:bg-green-800" @click="guardar_borrador">Guardar borrador</button>
        </div> -->
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
                        <label for=""><strong>Institucion</strong></label><br>
                        <input disabled="true" class="px-1  rounded-md" type="text" v-model="_institucion.institucion">
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
                <!-- <div class="text-gray-200">
                    <button type="submit" class="bg-cyan-500 rounded-lg p-1 active:bg-cyan-800" @click="guardar_examen">Guardar nuevo examen</button>
                </div>
                <div class="italic">
                    <p><strong>{{mensaje_examen}}</strong></p>
                </div> -->
            </Card>
        <!-- <div v-else class="w-10 h-10 animate-spin p-2 bg-gray-300 rounded-full">
            <img :src="arrows_rotate" alt="arrows rotate">
        </div> -->
        <br>
        <div v-if="mostrar_detalle">
            <div>
                <label for=""><strong>Tipos de examenes</strong></label>
                <Tabla :mostrar="terminado_tipos" :datos="datos_tipos" @recargar="cargar_tipos" @fila="capturar_tipo"></Tabla>
            </div>
            <br>
            <Card class="text-gray-800 font-sans">
                <div class="flex flex-wrap gap-4">
                    <div>
                        <label for=""><strong>Tipo</strong></label><br>
                        <input disabled="true" class="px-1 rounded-md w-96" type="text" v-model="tipo_seleccionado.tipo">
                    </div>
                    <div>
                        <label for=""><strong>Estado</strong></label><br>
                        <Combo llave="estado" :peticion="get_estados" id_prop="1"  @emitido="capturar_evento('_id_estado',$event)"></Combo>
                    </div>
                    <div>
                        <label for=""><strong>Resultado</strong></label><br>
                        <input class="px-1 rounded-md w-96" type="text" v-model="_resultado">
                    </div>
                    <div>
                        <label for=""><strong>Observacion</strong></label><br>
                        <input class="px-1 rounded-md w-96" type="text" v-model="_observacion">
                    </div>
                </div>
                <br>
                <div>
                    <button class="bg-cyan-500 rounded-lg p-1 active:bg-cyan-800" @click="agregar_detalle">Agregar</button>
                    <br>
                    <label class="italic" for=""><strong>{{mensaje_agregar}}</strong></label>
                </div>
            </Card>
            <br>
            <Card class="text-gray-800 font-sans">
                <div>
                    <label for=""><strong>Examenes por hacer</strong></label>
                    <ul  class="list-disc">
                        <li  v-for="(item, index) in _detalle" :key="index">
                            <div class="p-2 rounded-lg mb-2" :class="item.id != 0 ? 'bg-green-400' : 'bg-gray-200'">
                                {{item.tipo}} / {{item.resultado}} / {{item.observacion}}
                            </div>
                        </li>
                    </ul>
                </div>
                <br>
                <div v-if="!guardando_detalle">
                    <button class="bg-cyan-500 rounded-lg p-1 active:bg-cyan-800" @click="guardar_detalle">Guardar detalle</button>
                </div>
                <div v-else class="w-10 h-10 animate-spin p-2 bg-gray-300 rounded-full">
                    <img :src="arrows_rotate" alt="arrows rotate">
                </div>
            </Card>
        </div>
        <div v-else>
            <label for=""><strong>Seleccione un examen para agregar detalles</strong></label>
        </div>
        <br>
    </div>
</template>
<script>
import Card from './ui/Card.vue';
import Combo from './ui/Combo.vue';
import { get_instituciones, get_estados } from '../variables/rutas';
import { examen } from '../variables/examen';
import { ExamenService, TipoExamenService, DetalleExamenService } from '../variables/servicios';
import { arrows_rotate } from '../variables/svg';
import Tabla from '../components/ui/Tabla.vue';

export default {
    name: 'FormDetalle',
    props: {
        datos: {
            type: Object,
            required: true
        }
    },
    components: {
        Combo, Card, Tabla
    },
    data() {
        return {
            examen: examen(),
            arrows_rotate: arrows_rotate,
            get_instituciones,
            get_estados,
            _examen: {},
            _detalle: [],
            _persona: {},
            _institucion: {},
            _id_estado: 0,
            _id_institucion: 0,
            _resultado: 'pendiente',
            _observacion: 'pendiente',
            tipo_seleccionado: { tipo: '' },
            mensaje_examen: '',
            mensaje_agregar: '',
            datos_tipos: {},
            guardando_examen: false,
            guardando_detalle: false,
            terminado_tipos: false,
            mostrar_detalle: false,
        }
    },
    methods: {
        cargar_datos() {
            try {
                this._examen = this.examen.examen ?? { id: '', examen: '', institucion: '', estado: '', motivo: '', observacion: '', fecha_realiza: '' };
                this._detalle = this.examen.detalle ?? [];
                this._institucion = this.examen.institucion ?? { institucion: '' };
                this._persona = this.examen.persona ?? { nombres: '', apellidos: '' };
                this.cargar_tipos();
            } catch (error) { }
        },
        async cargar_tipos() {
            this.terminado_tipos = false;
            this.datos_tipos.titulos = ['tipo', 'referencia', 'descripcion', 'precio'];
            this.datos_tipos.registros = await TipoExamenService.get_tipos();
            this.terminado_tipos = true;
        },
        guardar_borrador() {
            // 
        },
        capturar_evento(tipo, id) {
            this[tipo] = id;
        },
        capturar_tipo(tipo) {
            this.tipo_seleccionado = tipo;
        },
        agregar_detalle() {
            if (this.tipo_seleccionado.id != undefined) {
                let nuevo_detalle = {};
                nuevo_detalle.id = 0;
                nuevo_detalle.id_examen = this._examen.id;
                nuevo_detalle.id_estado = this._id_estado;
                nuevo_detalle.tipo = this.tipo_seleccionado.tipo;
                nuevo_detalle.id_tipo = this.tipo_seleccionado.id;
                nuevo_detalle.resultado = this._resultado;
                nuevo_detalle.observacion = this._observacion;
                let fila = this._detalle.find(p => p.id_tipo == nuevo_detalle.id_tipo);
                if (fila) {
                    this.mensaje_agregar = 'ese tipo de examen ya esta listado';
                } else {
                    this._detalle.push(nuevo_detalle);
                    this.mensaje_agregar = '';
                }
            }
        },
        async guardar_detalle(){
            try {
                this._detalle.forEach(async element => {
                    this.guardando_detalle = true;
                    let {tipo, ...detalle} = element;
                    if(element.id == 0){
                        await DetalleExamenService.create(detalle);
                        element.id = 1;
                    }
                });
            } catch (error) {  }
            this.guardando_detalle = false;
        }
    },
    beforeMount() {
        this.cargar_datos();
        if(this._examen.id == undefined || this._examen.id == ''){
            this.mostrar_detalle = false;
        }else{
            this.mostrar_detalle = true;
        }
    },
}
</script>