<template lang="es">
    <h2 class="font-bold">Registro</h2>
    <div class="grid grid-flow-dense grid-cols-3 grid-rows-10 gap-y-2">
        <label class="col-span-1 font-semibold" for="cedula">Cedula</label>
        <input class="col-span-2 px-2 rounded-md" type="text" id="cedula" v-model="cedula">

        <label class="col-span-1 font-semibold" for="nombres">Nombres</label>
        <input class="col-span-2 px-2 rounded-md" type="text" id="nombres" v-model="nombres">

        <label class="col-span-1 font-semibold" for="apellidos">Apellidos</label>
        <input class="col-span-2 px-2 rounded-md" type="text" id="apellidos" v-model="apellidos">
 
        <label class="col-span-1 font-semibold" for="fecha">Fecha de nacimiento</label>
        <input class="col-span-2 px-2 rounded-md" type="date" id="fecha" v-model="fecha_nacimiento">

        <label class="col-span-1 font-semibold" for="genero">genero</label>
        <ComboGenero id="genero"  @id_genero="capturar_evento"></ComboGenero>
    </div>
    
    <div class="flex flex-row-reverse gap-3">
        <button class=" active:translate-x-3 animation ease-in-out duration-200 hover:bg-green-500 hover:text-gray-800  rounded-md p-2 bg-emerald-600 text-gray-200" @click="emitir_info">Siguiente</button>
    </div>
    <div v-if="mostrar_errores" class="w-60 mx-auto my-3 text-red-700 font-semibold">
        <p class="break-before-all">{{errores}}</p>
    </div>
</template>
<script>
import ComboGenero from './ComboGenero.vue';
export default {
    name: 'FormPersona',
    components:{
        ComboGenero
    },
    data() {
        return {
            cedula:'',
            nombres:'',
            apellidos:'',
            fecha_nacimiento:'',
            id_genero:3,
            mostrar_errores:false,
            errores:''
        }
    },
    methods: {
        capturar_evento(valor){
            this.id_genero = valor;
        },
        emitir_info(){
            let validado = this.valores_validos();
            if(validado === true){
                this.mostrar_errores = false;
                this.errores = '';
                let persona = {
                    cedula: this.cedula,
                    nombres: this.nombres,
                    apellidos: this.apellidos,
                    fecha_nacimiento: this.fecha_nacimiento,
                    id_genero: this.id_genero
                }
                this.$emit('persona',persona);

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