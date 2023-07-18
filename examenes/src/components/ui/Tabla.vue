<template lang="es">
    <div v-if="mostrar">
      <br>
      <div class="flex flex-wrap flex-row-reverse gap-2">
        <button class="mb-2 px-2 py-1 border-b-2 border-cyan-500 text-gray-300
        animation duration-300 hover:bg-cyan-500 hover:text-gray-100 hover:rounded-md 
        active:bg-cyan-700"
        @click="emitir_evento">Refrescar tabla</button>
        <div class="flex-grow"></div>
        <div class="flex flex-wrap gap-2 m-1">
          <button @click="filtrar()" class="p-1 rounded-lg bg-teal-500 active:bg-teal-800">Buscar</button>
          <input class="p-1 rounded-md px-2" type="text" v-model="filtro">
          <button @click="quitar_filtro" class="p-1 underline underline-offset-2 text-gray-200 active:text-gray-500">Limpiar</button>
        </div>
      </div>
      <div class="overflow-x-auto rounded-lg border border-gray-700">
        <table class="min-w-full divide-y-2 divide-gray-700 bg-gray-200 text-sm">
          <thead class="ltr:text-left rtl:text-right">
            <tr>
              <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 uppercase"
              v-for="(titulo, index) in titulos" :key="index">
                {{titulo}}
              </th>
            </tr>
          </thead>
    
          <tbody class="divide-y divide-gray-700">
            <tr class="animation duration-200 hover:bg-gray-400 bg-gray-100 hover:cursor-pointer"
            v-for="(item, index) in registros" :key="index">
              <td @click="emitir_fila(item)" class="whitespace-nowrap px-4 py-2 font-medium text-gray-900"
              v-for="(llave, index) in titulos" :key="index">{{item[llave]}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else class="w-10 h-10 p-2 mx-auto animate-spin bg-gray-300 rounded-full">
        <img :src="arrows_rotate" alt="arrows rotate">
    </div>
  </template>
<script>
import { arrows_rotate } from "../../variables/svg";

export default {
  name: 'Tabla',
  props: {
    datos: {
      type: Object,
      required: true
    },
    mostrar: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      registros: undefined,
      titulos: undefined,
      arrows_rotate: arrows_rotate,
      filtro: ''
    }
  },
  methods: {
    cargar_tabla() {
      try {
        this.titulos = this.datos.titulos;
        this.registros = this.datos.registros;
      } catch (error) {
        this.registros = [];
        this.titulos = [];
      }

    },
    filtrar(){
      let filtrados = [];
      this.registros.forEach(p => {
        Object.keys(p).forEach(k => {
          if(p[k] == this.filtro){
            filtrados.push(p);
          }
        });
      });
      this.registros = filtrados;
    },
    quitar_filtro(){
      this.cargar_tabla();
    },
    emitir_evento() {
      this.$emit('recargar', true);
    },
    emitir_fila(fila) {
      this.$emit('fila', fila);
    }
  },
  mounted() {
    this.cargar_tabla();
  },
  watch:{
    mostrar(){
      this.cargar_tabla();
    }
  }
}
</script>