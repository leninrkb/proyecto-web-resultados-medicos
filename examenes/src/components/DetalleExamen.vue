<template lang="es">
    <div v-if="mostrar">
      <h3 class="text-gray-200 font-sans text-xl capitalize">Detalle del examen</h3>
        <hr>
        <div class="text-gray-200 text-xl mb-20">
            <h3 class="flex flex-row-reverse font-bold">{{institucion.institucion}}</h3>
            <h3 class="flex flex-row-reverse font-bold">{{institucion.ubicacion}}</h3>
            <br>
            <img class="w-32 rounded-md ring-1 ring-sky-500" :src="institucion.path_img" alt="logo laboratorio">
            <h4 class="text-sky-500 font-semibold">Examen No. {{examen.id}}</h4>
            <h4 class="text-gray-200 font-semibold uppercase">{{fila.nombres}} {{fila.apellidos}}</h4>
            <div class="border-l-4 pl-2 border-sky-500 text-sm">
                <h5><strong>Identificacion: </strong> {{persona.cedula}} </h5>
                <h5><strong>Fecha de nacimiento: </strong> {{persona.fecha_nacimiento}} </h5>
                <h5><strong>Edad: </strong> {{persona.edad}} </h5>
                <h5><strong>Genero: </strong> {{genero.genero}} </h5>
                <div class="flex flex-row-reverse">
                    <h5><strong>Fecha de ingreso: </strong>{{fila.fecha_realiza}}</h5>
                </div>
            </div>
            <br>
            <div>
                <h4 class="mx-auto w-fit font-semibold">Informe de resultados</h4>
            </div>
            <br>
            <div class="text-sm border-l-4 border-green-500 pl-2">
                <h5 class="uppercase font-semibold text-gray-300">{{examen.examen}}</h5>
                <h4><strong>Razon del examen</strong></h4>
                <p class="text-justify text-gray-400">
                    {{examen.motivo}}
                </p>
            </div>
            <br>
            <div class="overflow-x-auto text-sm rounded-lg bg-stone-700 p-2">
                <table class="table-auto divide-y-2 divide-stone-400">
                    <thead>
                        <tr>
                            <th class="px-2">Tipo de Examen</th>
                            <th class="px-2">Estado</th>
                            <th class="px-2">V. Referencia</th>
                            <th class="px-2">Resultados</th>
                            <th class="px-2">Observaciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, index) in detalle" :key="index">
                            <td  class="p-2">{{item.tipo}}</td>
                            <td  class="p-2">{{item.estado}}</td>
                            <td  class="p-2">{{item.referencia}}</td>
                            <td  class="p-2">{{item.resultado}}</td>
                            <td  class="p-2">{{item.observacion}}</td>
                        </tr>
                    </tbody>
                </table> 
            </div>
            <br>
            <div class="text-sm border-l-4 border-green-500 pl-2">
                <h4><strong>Observaciones</strong></h4>
                <p class="text-justify text-gray-400">
                    {{examen.observacion}}
                </p>
            </div>
            <button @click="crearQR">generar qr</button>
            <div id="container">
                <canvas id="canvas"></canvas>
            </div>
        </div>  
        <hr>
    </div>
    <div v-else class="w-10 h-10 p-2 mx-auto animate-spin bg-gray-300 rounded-full">
        <img :src="arrows_rotate" alt="arrows rotate">
    </div>
    
</template>
<script>
import { arrows_rotate } from '../variables/svg';
import {
    InstitucionService, ExamenService,
    PersonaService, GeneroService,
    TipoExamenService, DetalleExamenService,
    EstadoService
} from '../variables/servicios';
import { calcularEdad } from '../variables/funciones';
import qrcode from 'qrcode';

export default {
    name: 'DetalleExamen',
    props: {
        fila: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            mostrar: false,
            arrows_rotate,
            institucion: {},
            examen: {},
            persona: {},
            genero: {},
            tipo_examen: {},
            detalle: []
        }
    },
    methods: {
        reestablecer() {
            this.institucion = {},
                this.examen = {},
                this.persona = {},
                this.genero = {},
                this.tipo_examen = {},
                this.detalle = []
        },
        crearQR() {
            let canvas = document.getElementById('container');
            qrcode.toCanvas('hola soy joao', { errorCorrectionLevel: 'H' }, function (err, canvas) {
                if (err) throw err
                var container = document.getElementById('container');
                container.appendChild(canvas)
            });
        },
        async cargar_datos() {
            this.mostrar = false;
            try {
                // this.crearQR();
                this.reestablecer();
                this.institucion = await InstitucionService.get_instituciones_id(this.fila.id_institucion);
                this.examen = await ExamenService.get_examen_id(this.fila.id);
                this.persona = await PersonaService.get_persona_id(this.fila.id_persona);
                this.persona.edad = calcularEdad(this.persona.fecha_nacimiento);
                this.genero = await GeneroService.get_genero_id(this.persona.id_genero);
                let tipos_examenes = await TipoExamenService.get_tipos();
                let estados_examenes = await EstadoService.get_estados();
                let resp = await DetalleExamenService.get_detalle();
                resp.forEach(element => {
                    if (element.id_examen == this.examen.id) {
                        let tipo = tipos_examenes.find(p => p.id == element.id_tipo);
                        element.tipo = tipo.tipo;
                        element.referencia = tipo.referencia;
                        let estado = estados_examenes.find(p => p.id == element.id_estado);
                        element.estado = estado.estado;
                        this.detalle.push(element);
                    }
                });

            } catch (error) {
                console.log(error);
             }
            this.mostrar = true;

        }
    },
    beforeMount() {
        this.cargar_datos();
    },
    watch: {
        fila() {
            console.log(this.fila);
            this.cargar_datos();
        }
    }
}
</script>