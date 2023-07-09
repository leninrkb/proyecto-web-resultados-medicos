<template lang="es">
    <div class="grid grid-flow-dense grid-cols-3 grid-rows-10 gap-y-2">
        <label class="col-span-1 font-semibold" for="cedula">Cedula</label>
        <input class="col-span-2 px-2 rounded-md" type="text" id="cedula" v-model="cedula" @input="emitir_info">

        <label class="col-span-1 font-semibold" for="nombres">Nombres</label>
        <input class="col-span-2 px-2 rounded-md" type="text" id="nombres" v-model="nombres" @input="emitir_info">

        <label class="col-span-1 font-semibold" for="apellidos">Apellidos</label>
        <input class="col-span-2 px-2 rounded-md" type="text" id="apellidos" v-model="apellidos" @input="emitir_info">
 
        <label class="col-span-1 font-semibold" for="fecha">Fecha de nacimiento</label>
        <input class="col-span-2 px-2 rounded-md" type="date" id="fecha" v-model="fecha_nacimiento" @input="emitir_info">

        <label class="col-span-1 font-semibold" for="genero">genero</label>
        <Combo :peticion="get_generos" :id_prop="id_genero"  @emitido="capturar_evento"></Combo>
    </div>
    <div v-if="mostrar_errores" class="w-60 mx-auto my-3 text-red-700 font-semibold">
        <p class="break-before-all">{{errores}}</p>
    </div>
</template>
<script>
import Combo from './Combo.vue';
import { get_generos } from "../variables/rutas";

export default {
    name: 'FormPersona',
    props:{
        datos:{
            type: Object,
            required: false
        }
    },
    beforeMount() {
        this.cargar_datos();
    },
    components:{
        Combo
    },
    data() {
        return {
            id: 0,
            cedula: '',
            nombres: '',
            apellidos: '',
            fecha_nacimiento: '',
            id_genero: 1,
            mostrar_errores: false,
            errores: '',
            get_generos: get_generos
        }
    },
    methods: {
        cargar_datos(){
            if(this.datos !== undefined){
                try {
                    this.id = this.datos.id ?? 0;
                    this.cedula = this.datos.cedula ?? '';
                    this.nombres = this.datos.nombres ?? '';
                    this.apellidos = this.datos.apellidos ?? '';
                    this.fecha_nacimiento = this.datos.fecha_nacimiento ?? '';
                    this.id_genero = this.datos.id_genero ?? 1;
                    this.emitir_info();
                }catch{ }
            }
        },
        capturar_evento(valor){
            this.id_genero = valor;
            this.emitir_info();
        },
        emitir_info(){
            let validado = this.valores_validos();
            if(validado === true){
                this.mostrar_errores = false;
                this.errores = '';
                let persona = {
                    id: this.id,
                    cedula: this.cedula,
                    nombres: this.nombres,
                    apellidos: this.apellidos,
                    fecha_nacimiento: this.fecha_nacimiento,
                    id_genero: this.id_genero
                }
                this.$emit('emitido',persona);

            }else{
                this.mostrar_errores = true;
                this.errores = validado;
            }
        },
        valores_validos(){
            let mensaje = '';
            let regex_nombres = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$/;
            let regex_cedula = /^\d{10}$/;
            let regex_fecha = /^\d{4}-(0[1-9]|1[0-2])-([0-2][1-9]|3[01])$/;
            // const regexFecha = /^(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[01])-\d{4}$/;

            
            this.cedula = this.cedula.replace(/\s/g, '');
            if(!regex_cedula.test(this.cedula)){
                mensaje += 'Campo -cedula- no valido. '
            }
            if(!regex_nombres.test(this.nombres)){
                mensaje += 'Campo -nombres- no valido. '
            }
            if(!regex_nombres.test(this.apellidos)){
                mensaje += 'Campo -apellidos- no valido. '
            }
            if(!regex_fecha.test(this.fecha_nacimiento)){
                mensaje += 'Campo -fecha- no valido. '
            }
            if(mensaje === ''){
                return true;
            }
            return mensaje;
        }
    },
}
</script>