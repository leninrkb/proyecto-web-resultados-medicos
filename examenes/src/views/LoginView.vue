<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="p-3 text-gray-400">
            <h2 class="text-2xl">Login</h2>
            <h2 class="text-xl">Ingresa al sistema</h2>
            <br>
            <Card class="text-gray-800 font-sans w-fit mx-auto">
                <h2 class="font-bold ">Login</h2><br>
                <FormUsuario @emitido="capturar_usuario"></FormUsuario>
                <br>
                <div  class="flex flex-row-reverse gap-3">
                    <button v-if="!cargando" class=" active:translate-x-3 animation ease-in-out duration-200 hover:bg-green-500 hover:text-gray-800  rounded-md p-2 bg-emerald-600 text-gray-200" 
                    @click="autenticar()">Ingresar</button>
                    <img v-else class="w-6 h-6 animate-spin" :src="arrows_rotate" alt="arrows rotate">
                </div>
                <div>
                    <p class="font-semibold italic">{{mensaje}}</p>
                </div>
            </Card>
        </div>
    </div>
</template>
<script>
import FormUsuario from '@/components/FormUsuario.vue';
import Toolbar from '@/components/ui/Toolbar.vue';
import {registro, examenes_disponibles, home, inicio_admin} from '../variables/rutas';
import Card from '@/components/ui/Card.vue';
import { arrows_rotate } from "../variables/svg";
import { autenticar } from '../variables/rutas';
import axios from 'axios';
import { sesion } from '../variables/sesion';

export default {
    name: 'LoginView',
    components:{
        Toolbar,
        Card,
        FormUsuario
    },
    data(){
        return{
            datos:{
                titulo:'Biolab',
                enlaces:[
                    {
                        titulo: 'Examenes',
                        ruta: examenes_disponibles
                    }
                ],
                primarios:[
                    {
                        titulo:'Registrarse',
                        ruta: registro
                    },
                    {
                        titulo:'Regresar',
                        ruta: home
                    }
                ]
            },
            usuario_capturado: undefined,
            cargando: false,
            arrows_rotate: arrows_rotate,
            mensaje:'',
            sesion: sesion()
        }
    },
    methods: {
        capturar_usuario(usuario){
            this.mensaje = '';
            if(usuario != false){
                this.usuario_capturado = usuario;
            }
        },
        autenticar(){
            this.mensaje = '';
            this.cargando = true;
            axios.post(autenticar,{
                parameter: this.usuario_capturado
            })
            .then(resp => {
                let usuario = resp.data.result;
                if(usuario != false){
                    console.log(usuario);
                    this.mensaje = 'autenticado';
                    this.validar_tipo_usuario(usuario)
                }else{
                    this.mensaje = 'credenciales incorrectas';
                }
                this.cargando = false;
            })
            .catch(error => {
                this.cargando = false;
                this.mensaje = 'ocurrio un error';
            })
        },
        validar_tipo_usuario(usuario){
            if(usuario.id_rol == 1){
                this.sesion.nuevaSesion(usuario);
                this.$router.push(inicio_admin);
            }else if(usuario.id_rol == 2){
                console.log('entra paciente');
            }
        }
    },
}
</script>