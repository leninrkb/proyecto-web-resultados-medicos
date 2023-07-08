<template lang="es">
    <div class='container mx-auto font-sans'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="p-3 text-gray-400">
            <h2 class="text-2xl">Registro</h2>
            <h2 class="text-xl">Crea tu usuario</h2>
            <br>
            <Card class="text-gray-800 font-sans w-fit mx-auto">
                <FormPersona  @persona="capturar_persona"></FormPersona>
                <div class="flex flex-row-reverse gap-3">
                    <button class=" active:translate-x-3 animation ease-in-out duration-200 hover:bg-green-500 hover:text-gray-800  rounded-md p-2 bg-emerald-600 text-gray-200" @click="crear_persona">Siguiente</button>
                </div>
                <div>
                    <p class="font-semibold italic">{{mensaje}}</p>
                </div>
            </Card>

        </div>
    </div>
</template>
<script>
import {create_persona} from '../variables/rutas';
import axios from "axios";
import Card  from "../components/ui/Card.vue";
import FormPersona  from "../components/FormPersona.vue";
import Toolbar from '@/components/ui/Toolbar.vue';
import { home, examenes_disponibles, login } from '../variables/rutas';
export default {
    name: 'RegistroView',
    components: {
        Toolbar,
        Card,
        FormPersona
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
            persona_creada: undefined,
            datos_persona: {
                id: 12,
                cedula: '1231231231',
                nombres: 'lenin',
                apellidos: 'acosta',
                fecha_nacimiento: '2000-06-03',
                id_genero: 6,
            }
        }
    },
    methods: {
        capturar_persona(persona){
            this.persona = persona
        },
        crear_persona(){
            if(this.persona !== undefined){
                this.mensaje = '';
                let url = create_persona;
                axios.post(url,{
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
                    this.mensaje = resp.data.message;
                    this.persona_creada = resp.data.result;
                })
                .catch(error => {
                    this.mensaje = 'ha ocurrido un error: ' + error.message;
                });
            }else{
                this.mensaje = 'no se puede hacer la peticion';
            }
        }
    },
}
</script>