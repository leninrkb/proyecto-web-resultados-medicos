<template lang="es">
    <div class="flex flex-row-reverse">
      <button class="mb-2 px-2 py-1 border-b-2 border-cyan-500 text-gray-300
      animation duration-300 hover:bg-cyan-500 hover:text-gray-100 hover:rounded-md 
      active:bg-cyan-700"
      @click="emitir_evento">Refrescar tabla</button>
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
  </template>
  <script>
  export default {
      name:'Tabla',
      props:{
        datos:{
            type: Object,
            required: true
        }
      },
      data() {
          return {
              registros: undefined,
              titulos: undefined,
          }
      },
      methods: {
          cargar_tabla(){
              try {
                  this.titulos = this.datos.titulos;
                  this.registros = this.datos.registros;
              } catch (error) {
                  this.registros = [];
                  this.titulos = [];
              }
              
          },
          emitir_evento(){
            this.$emit('recargar',true);
          },
          emitir_fila(fila){
            this.$emit('fila',fila);
          }
      },
      beforeMount() {
        this.cargar_tabla();
      }
  }
  </script>