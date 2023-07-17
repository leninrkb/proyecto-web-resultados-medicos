<template lang="es">
    <div class="text-gray-200 text-lg font-sans">
        <div class="flex flex-wrap gap-3">
            <button class="rounded-lg bg-teal-600 p-1 px-2
            animation duration-300
            hover:ring-1 hover:ring-teal-200
            active:bg-teal-800">
            <router-link :to="nuevo_examen">Nuevo Examen</router-link>
            </button>

            <button class="rounded-lg bg-teal-600 p-1 px-2
            animation duration-300
            hover:ring-1 hover:ring-teal-200
            active:bg-teal-800">
            <router-link :to="eliminar_examen">Eliminar Examen</router-link>
            </button>

            <button class="rounded-lg bg-teal-600 p-1 px-2
            animation duration-300
            hover:ring-1 hover:ring-teal-200
            active:bg-teal-800">
            <router-link :to="nuevo_detalle">Nuevo Detalle</router-link>
            </button>
        </div>
        <br>
        <div class="">
            <router-view></router-view>
        </div>
    </div>
</template>
<script>
import { nuevo_examen, nuevo_detalle, eliminar_examen } from '../../variables/rutas';
export default {
    name:'AdministrarExamenes',
    data() {
        return {
            nuevo_examen,
            nuevo_detalle,
            eliminar_examen,
        }
    },
}
</script>