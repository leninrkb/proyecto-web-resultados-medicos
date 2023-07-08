<template lang="es">
    <select class="rounded-md" v-if="terminado" @change="emitir" v-model="id_genero">
        <option :value="item.id" v-for="(item, index) in generos" :key="index" :selected="item.id === id_genero">{{item.genero}}</option>
    </select>
    <div v-else class="w-6 h-6 animate-spin">
        <img :src="arrows_rotate" alt="arrows rotate">
    </div>
</template>
<script>
import axios from 'axios';
import { get_generos } from "../variables/rutas";
import { arrows_rotate } from "../variables/svg";
export default {
    name:'ComboGenero',
    props:{
        id_genero_prop:{
            type: Number,
            required: false
        }
    },
    mounted() {
        this.cargar_datos();
        this.emitir();
    },
    data() {
        return {
            terminado: false,
            arrows_rotate: arrows_rotate,
            generos:[],
            id_genero: 1
        }
    },
    methods: {
        cargar_datos(){
            try {
                if(this.id_genero_prop !== undefined){
                    this.id_genero = this.id_genero_prop ?? 1;
                }
                this.cargar_combo();
            } catch (error) { }
        },
        cargar_combo(){
            this.terminado = false;
            axios.get(get_generos)
            .then(resp => {
                resp.data.result.forEach(element => {
                    this.generos.push(element);
                });
                this.terminado = true;
            })
            .catch(error => {
                //code
            });
        },
        emitir(){
            this.$emit('id_genero',this.id_genero);
        }
    },
}
</script>