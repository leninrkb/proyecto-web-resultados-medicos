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
            <h4 class="text-gray-200 font-semibold uppercase">{{persona.nombres}} {{persona.apellidos}}</h4>
            <div class="border-l-4 pl-2 border-sky-500 text-sm">
                <h5><strong>Identificacion: </strong> {{persona.cedula}} </h5>
                <h5><strong>Fecha de nacimiento: </strong> {{persona.fecha_nacimiento}} </h5>
                <h5><strong>Edad: </strong> {{persona.edad}} </h5>
                <h5><strong>Genero: </strong> {{genero.genero}} </h5>
                <div class="flex flex-row-reverse">
                    <h5><strong>Fecha de ingreso: </strong>{{examen.fecha_realiza}}</h5>
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
            <br>
            <img class="rounded-lg" :src="qr_url" alt="qr">
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
import { cifrar } from '../variables/funciones';
import { resumen } from '../variables/rutas';

export default {
    name: 'DetalleExamen',
    props: {
        id_examen: {
            type: Number,
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
            detalle: [],
            qr_url: ''

        }
    },
    methods: {
        reestablecer() {
            this.institucion = {},
                this.examen = {},
                this.persona = {},
                this.genero = {},
                this.tipo_examen = {},
                this.detalle = [],
                this.qr_url = ''
        },
        crearQR(datos) {
            let ctx = this;
            datos = JSON.stringify(datos);
            datos = cifrar(datos, 'examenes');
            let url_componente = resumen + datos;
            console.log( url_componente);
            qrcode.toDataURL(url_componente, function (err, url) {
                ctx.qr_url = url;
            });
            
        },
        async cargar_datos() {
            this.mostrar = false;
            try {
                this.reestablecer();
                this.examen = await ExamenService.get_examen_id(this.id_examen);
                this.institucion = await InstitucionService.get_instituciones_id(this.examen.id_institucion);
                this.persona = await PersonaService.get_persona_id(this.examen.id_persona);
                this.persona.edad = calcularEdad(this.persona.fecha_nacimiento);
                this.genero = await GeneroService.get_genero_id(this.persona.id_genero);
                let tipos_examenes = await TipoExamenService.get_tipos();
                let estados_examenes = await EstadoService.get_estados();
                let detalle_examen = await DetalleExamenService.get_detalle();
                detalle_examen.forEach(element => {
                    if (element.id_examen == this.examen.id) {
                        let tipo = tipos_examenes.find(p => p.id == element.id_tipo);
                        element.tipo = tipo.tipo;
                        element.referencia = tipo.referencia;
                        let estado = estados_examenes.find(p => p.id == element.id_estado);
                        element.estado = estado.estado;
                        this.detalle.push(element);
                    }
                });
                this.crearQR(this.id_examen);
            } catch (error) {
                console.log(error);
            }
            this.mostrar = true;

        }
    },
    mounted() {
        this.cargar_datos();
    },
    watch: {
        id_examen() {
            this.cargar_datos();
        }
    }
}
</script>