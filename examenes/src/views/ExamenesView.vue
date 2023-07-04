<template lang="es">
    <div class='container mx-auto'>
        <Toolbar :datos=datos></Toolbar>
        <br>
        <div class="p-3 text-gray-400">
            Examenes disponibles
            - tabla con los examenes disponibles
        </div>
    </div>
</template>
<script>
import Toolbar from '@/components/ui/Toolbar.vue';
import { registro, login } from '../variables/rutas';
export default {
    name: 'ExamenesView',
    components: {
        Toolbar
    },
    data() {
        return {
            datos: {
                titulo: 'Biolab',
                enlaces: [  ],
                primarios: [
                    {
                        titulo: 'Registrarse',
                        ruta: registro
                    },
                    {
                        titulo: 'Iniciar Sesion',
                        ruta: login
                    },
                ]
            }
        }
    },
}
</script>