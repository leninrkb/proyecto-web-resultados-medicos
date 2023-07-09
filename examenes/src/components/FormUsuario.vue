<template lang="es">
    <div class="grid grid-flow-dense grid-cols-3 grid-rows-10 gap-y-2">
        <label class="col-span-1 font-semibold" for="usuario">usuario</label>
        <input class="col-span-2 px-2 rounded-md" type="text" id="usuario" v-model="usuario" @input="emitir_datos">

        <label class="col-span-1 font-semibold" for="contrasena">contrasena</label>
        <input class="col-span-2 px-2 rounded-md" type="password" id="contrasena" v-model="contrasena" @input="emitir_datos">

        <label class="col-span-1 font-semibold" for="rol">rol</label>
        <Combo disabled="true" id_prop="2" @emitido="capturar_valor" :peticion="get_roles_usuarios"></Combo>
    </div>
    <div v-if="mostrar_errores" class="w-80 mx-auto my-3 text-red-700 font-semibold">
        <p class="break-before-all">{{errores}}</p>
    </div>
</template>
<script>
import { get_roles_usuarios } from '../variables/rutas';
import Combo from '../components/Combo.vue';
export default {
    name: 'FormUsuario',
    props:{
        datos:{
            type: Object,
            requred: true
        }
    },
    components: {
        Combo
    },
    beforeMount() {
        this.cargar_datos();
    },
    data() {
        return {
            get_roles_usuarios: get_roles_usuarios,
            id: 0,
            id_persona: 0,
            usuario: '',
            contrasena: '',
            id_rol: 0,
            mostrar_errores: false,
            errores: '',
        }
    },
    methods: {
        cargar_datos(){
            try {
                this.id = this.datos.id ?? 0;
                this.id_persona = this.datos.id_persona ?? 0;
                this.id_rol = this.datos.id_rol ?? 0;
                this.usuario = this.datos.usuario ?? '';
                this.contrasena = this.datos.contrasena ?? '';
                this.emitir_datos();
            } catch (error) {
                
            }
        },
        capturar_valor(id) {
            this.id_rol = id;
        },
        emitir_datos(){
            let validado = this.valores_validos();
            if(validado === true){
                this.mostrar_errores = false;
                this.errores = '';
                let usuario = {
                    id: this.id,
                    id_persona: this.id_persona,
                    id_rol: this.id_rol,
                    usuario: this.usuario,
                    contrasena: this.contrasena
                };
                this.$emit('emitido',usuario);
            }else{
                this.mostrar_errores = true;
                this.errores = validado;
                this.$emit('emitido',false);
            }
            
        },
        valores_validos(){
            let mensaje = '';
            let regex_contrasena = /^.{8}$/;
            let regex_usuario = /^.{5,}$/;
            this.usuario = this.usuario.replace(/\s/g, '');
            this.contrasena = this.contrasena.replace(/\s/g, '');
            if(!regex_usuario.test(this.usuario)){
                mensaje += 'Usuario debe tener al menos 5 caracteres. '
            }
            if(!regex_contrasena.test(this.contrasena)){
                mensaje += 'Su contrasena debe tener 8 caracteres. '
            }
            if(mensaje === ''){
                return true;
            }
            return mensaje;
        }
    },
}
</script>