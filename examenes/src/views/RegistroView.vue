<template lang="es">
    <div class='container mx-auto font-sans'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="mx-5 sm:mx-24">

        <div class="p-3 text-gray-400">
            <h2 class="text-2xl">Registro</h2>
            <h2 class="text-xl">Crea tu usuario</h2>
            <br>
            <Card class="text-gray-800 font-sans w-fit mx-auto">
                <h2 class="font-bold ">Registro</h2><br>
                <FormPersona @emitido="capturar_persona"></FormPersona>
                <br>
                <hr>
                <br>
                <FormUsuario rol_visible="true" @emitido="capturar_usuario"></FormUsuario>
                <br>
                <div  class="flex flex-row-reverse gap-3">
                    <button v-if="!cargando" class=" active:translate-x-3 animation ease-in-out duration-200 hover:bg-green-500 hover:text-gray-800  rounded-md p-2 bg-emerald-600 text-gray-200" @click="crear_persona">Siguiente</button>
                    <img v-else class="w-6 h-6 animate-spin" :src="arrows_rotate" alt="arrows rotate">
                </div>
                <div>
                    <p class="font-semibold italic">{{mensaje}}</p>
                </div>
            </Card>

        </div>
        </div>
    </div>
</template>
<script>
import FormUsuario from '@/components/FormUsuario.vue';
import { create_persona, delete_persona } from '../variables/rutas';
import { create_usuario } from '../variables/rutas';
import axios from "axios";
import Card from "../components/ui/Card.vue";
import FormPersona from "../components/FormPersona.vue";
import Toolbar from '@/components/ui/Toolbar.vue';
import { home, examenes_disponibles, login } from '../variables/rutas';
import { arrows_rotate } from "../variables/svg";

export default {
    name: 'RegistroView',
    components: {
        Toolbar,
        Card,
        FormPersona,
        FormUsuario
    },
    beforeMount(){
        window.addEventListener('beforeunload', this.eliminar_persona);
    },
    beforeUnmount() {
        window.removeEventListener('beforeunload', this.eliminar_persona);
        this.eliminar_persona();
        
    },
    data() {
        return {
            datos: {
                titulo: 'Biolab',
                enlaces: [
                    {
                        titulo: 'Examenes',
                        ruta: examenes_disponibles
                    }
                ],
                primarios: [
                    {
                        titulo: 'Iniciar Sesion',
                        ruta: login
                    },
                    {
                        titulo: 'Regresar',
                        ruta: home
                    }
                ],

            },
            persona: undefined,
            mensaje: '',
            datos_usuario: {
                id: 0,
                id_persona: 0,
                id_rol: 2,
                usuario: '',
                contrasena: ''
            },
            persona_creada:false,
            usuario_creado: false,
            cargando: false,
            arrows_rotate: arrows_rotate

        }
    },
    methods: {
        capturar_persona(persona) {
            this.persona = persona
        },
        capturar_usuario(usuario) {
            this.datos_usuario = usuario;
        },
        crear_persona() {
            if(this.persona_creada == true){
                this.crear_usuario(this.persona);
                return;
            }else if (this.persona !== undefined) {
                this.mensaje = '';
                let url = create_persona;
                this.cargando = true;
                axios.post(url, {
                    "parameter": {
                        "id": 0,
                        "cedula": this.persona.cedula,
                        "nombres": this.persona.nombres,
                        "apellidos": this.persona.apellidos,
                        "fecha_nacimiento": this.persona.fecha_nacimiento,
                        "id_genero": this.persona.id_genero
                    }
                })
                .then(resp => {
                    this.persona_creada = true;
                    this.persona = resp.data.result;
                    this.mensaje = 'datos personales registrados';
                    this.cargando = false;
                    this.crear_usuario(this.persona);
                })
                .catch(error => {
                    this.cargando = false;
                    this.mensaje = 'error al registrar datos personales';
                });
            } else {
                this.mensaje = 'no se puede hacer la peticion';
            }
        },
        crear_usuario(persona) {
            if (this.datos_usuario == false) {
                return;
            }
            this.datos_usuario.id_persona = persona.id;
            this.cargando = true;
            axios.post(create_usuario, {
                parameter: this.datos_usuario
            })
            .then(resp => {
                this.mensaje = 'se ha registrado el usuario';
                this.usuario_creado = true;
                this.cargando = false;
                this.$router.push(login);
            })
            .catch(error => {
                this.cargando = false;
                this.mensaje = 'error al registrar usuario';
            });
        },
        eliminar_persona(event){
            if(this.usuario_creado == false){
                try {
                    let url = delete_persona + this.persona.id;
                    axios.delete(url);
                } catch (error) { }
            }
            
        }
    },
}
</script>