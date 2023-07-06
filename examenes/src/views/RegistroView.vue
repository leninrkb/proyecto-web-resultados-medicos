<template lang="es">
    <div class='container mx-auto font-sans'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="p-3 text-gray-400">
            <h2 class="text-2xl">Registro</h2>
            <h2 class="text-xl">Crea tu usuario</h2>
            <br>
            <Card class="text-gray-800 font-sans w-fit mx-auto">
                <FormPersona @persona="capturar_persona"></FormPersona>
            </Card>
        </div>
    </div>
</template>
<script>
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
                ]
            }
        }
    },
    methods: {
        capturar_persona(persona){
            console.log(persona);
        }
    },
}
</script>