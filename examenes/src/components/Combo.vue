<template lang="es">
    <select class="rounded-md" v-if="terminado" @change="emitir" v-model="id_seleccionado">
        <option :value="item.id" v-for="(item, index) in lista" :key="index" :selected="item.id === id_seleccionado">{{item.valor}}</option>
    </select>
    <div v-else class="w-6 h-6 animate-spin">
        <img :src="arrows_rotate" alt="arrows rotate">
    </div>
</template>
<script>
import axios from 'axios';
import { arrows_rotate } from "../variables/svg";
export default {
    name:'Combo',
    props:{
        id_prop:{
            type: Number,
            required: false
        },
        peticion:{
            type: String,
            required: true
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
            lista:[],
            id_seleccionado: 1
        }
    },
    methods: {
        cargar_datos(){
            try {
                if(this.id_prop !== undefined){
                    this.id_seleccionado = this.id_prop ?? 1;
                }
                this.cargar_combo();
            } catch (error) { }
        },
        cargar_combo(){
            this.terminado = false;
            axios.get(this.peticion)
            .then(resp => {
                let keys = Object.keys(resp.data.result[0]);
                resp.data.result.forEach(element => {
                    this.lista.push({
                        id: element.id,
                        valor: element[keys[0]]
                    });
                });
                this.terminado = true;
            })
            .catch(error => {
                //code
            });
        },
        emitir(){
            this.$emit('emitido',this.id_seleccionado);
        }
    },
}
</script>