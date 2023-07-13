<template lang="es">
    <div class="grid grid-flow-dense grid-cols-3 grid-rows-10 gap-y-2">
        <label class="col-span-1 font-semibold" for="usuario">usuario</label>
        <input class="col-span-2 px-2 rounded-md" type="text" id="usuario" v-model="usuario" @input="emitir_datos">

        <label class="col-span-1 font-semibold" for="contrasena">contrasena</label>
        <input class="col-span-2 px-2 rounded-md" type="password" id="contrasena" v-model="contrasena" @input="emitir_datos">

        <label v-if="_rol_visible" class="col-span-1 font-semibold" for="rol">rol</label>
        <Combo v-if="_rol_visible" :id_prop="id_rol" @emitido="capturar_valor" :peticion="get_roles_usuarios"></Combo>
    </div>
    <div v-if="mostrar_errores" class="w-80 mx-auto my-3 text-red-700 font-semibold">
        <p class="break-before-all">{{errores}}</p>
    </div>
</template>
<script>
import { get_roles_usuarios } from '../variables/rutas';
import Combo from '../components/ui/Combo.vue';
export default {
    name: 'FormUsuario',
    props:{
        datos:{
            type: Object,
            requred: false
        },
        rol_visible:{
            type: Boolean,
            required: false
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
            id_rol: 2,
            mostrar_errores: false,
            errores: '',
            _rol_visible: false
        }
    },
    methods: {
        cargar_datos(){
            try {
                this._rol_visible = this.rol_visible ?? false;
                this.id = this.datos.id ?? 0;
                this.id_persona = this.datos.id_persona ?? 0;
                this.id_rol = this.datos.id_rol ?? 2;
                this.usuario = this.datos.usuario ?? '';
                this.contrasena = this.datos.contrasena ?? '';
                this.emitir_datos();
            } catch (error) {
                
            }
        },
        capturar_valor(id) {
            this.id_rol = id;
            this.emitir_datos();
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
            let regex_contrasena = /^.{4,}$/;
            let regex_usuario = /^.{3,}$/;
            this.usuario = this.usuario.replace(/\s/g, '');
            this.contrasena = this.contrasena.replace(/\s/g, '');
            if(!regex_usuario.test(this.usuario)){
                mensaje += 'Usuario debe tener al menos 3 caracteres. '
            }
            if(!regex_contrasena.test(this.contrasena)){
                mensaje += 'Su contrasena debe tener al menos 4 caracteres. '
            }
            if(mensaje === ''){
                return true;
            }
            return mensaje;
        }
    },
}
</script>