<template lang="es">
  <div class="flex flex-row-reverse">
    <button class="mb-2 px-2 py-1 border-b-2 border-cyan-500 text-gray-300
    animation duration-300 hover:bg-cyan-500 hover:text-gray-100 hover:rounded-md 
    active:bg-cyan-700"
    @click="cargar_tabla">Refrescar tabla</button>
  </div>
  <div class="overflow-x-auto rounded-lg border border-gray-700">
    <table class="min-w-full divide-y-2 divide-gray-700 bg-gray-200 text-sm">
      <thead class="ltr:text-left rtl:text-right">
        <tr>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
            Examen
          </th>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
            Motivo
          </th>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
            Observacion
          </th>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
            Fecha
          </th>
        </tr>
      </thead>

      <tbody class="divide-y divide-gray-700">
        <tr class="animation duration-200 hover:bg-gray-400 bg-gray-100 hover:cursor-pointer"
        v-for="(item, index) in registros" :key="index">
          <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">{{item.examen}}</td>
          <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{item.motivo}}</td>
          <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{item.observacion}}</td>
          <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{item.fecha_realiza}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios';
import { get_examenes } from '../../variables/rutas';
export default {
    name:'TablaExamenesPacientes',
    data() {
        return {
            registros: undefined
        }
    },
    methods: {
        cargar_tabla(){
            try {
                axios.get(get_examenes).then(resp => {
                console.log(resp.data);
                this.registros = resp.data.result;
                }).catch(error => {
                    // error
                });
            } catch (error) {
                this.registros = [];
            }
            
        }
    },
    mounted() {
        this.cargar_tabla();
    },
}
</script>