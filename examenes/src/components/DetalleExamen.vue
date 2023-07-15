<template lang="es">
    <div v-if="mostrar">
      <h3 class="text-gray-200 font-sans text-xl capitalize">Detalle del examen</h3>
        <br>  
    </div>
    <div v-else class="w-10 h-10 p-2 mx-auto animate-spin bg-gray-300 rounded-full">
        <img :src="arrows_rotate" alt="arrows rotate">
    </div>
    
</template>
<script>
import { arrows_rotate } from '../variables/svg';
import { get_instituciones } from '../variables/rutas';

export default {
    name:'DetalleExamen',
    props:{
        mostrar: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {
            arrows_rotate,
            institucion: undefined
        }
    },
    methods: {
        cargar_instituciones(){
            try {
                
            } catch (error) {
                
            }
        }
    },
    mounted() {
        
    },
    watch:{
    mostrar(){
      
    }
  }
}
</script>