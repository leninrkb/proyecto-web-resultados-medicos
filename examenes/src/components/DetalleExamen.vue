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
                <h4 class="mx-auto w-fit">Informe de resultados</h4>
            </div>
            <br>
            <div class="text-sm">
                <table class="table-fixed">
                    <thead>
                        <tr>
                        <th>Examen</th>
                        <th>Tipo</th>
                        <th>Resultado</th>
                        <th>V. Referencia</th>
                        <th>Estado</th>
                        <th>Observacion</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, index) in detalle" :key="index">
                        <td>{{item.resultado}}</td>
                        <td>Malcolm Lockyer</td>
                        <td>1961</td>
                        </tr>
                    </tbody>
                </table> 
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
    TipoExamenService, DetalleExamenService
} from '../variables/servicios';
import { calcularEdad } from '../variables/funciones';

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
        async cargar_datos(){
            this.mostrar = false;
            try {
                this.institucion = await InstitucionService.get_instituciones_id(this.fila.id_institucion);
                this.examen = await ExamenService.get_examen_id(this.fila.id);
                this.persona = await PersonaService.get_persona_id(this.fila.id_persona);
                this.persona.edad = calcularEdad(this.persona.fecha_nacimiento);
                this.genero = await GeneroService.get_genero_id(this.persona.id_genero);
                this.detalle = await DetalleExamenService.get_detalle(this.examen.id);

            } catch (error) { }
            this.mostrar = true;

        }
    },
    beforeMount(){
        this.cargar_datos();
    },
    watch:{
        fila(){
            console.log(this.fila);
            this.cargar_datos();
        }
    }
}
</script>