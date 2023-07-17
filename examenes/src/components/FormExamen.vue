<template lang="es">
    <div>
        <Card class="text-gray-800 font-sans">
            <Combo llave="institucion" :peticion="get_instituciones" id_prop="1"  @emitido="capturar_evento('institucion',$event)"></Combo>
        </Card>
    </div>
</template>
<script>
import Card from './ui/Card.vue';
import Combo from './ui/Combo.vue';
import { get_instituciones } from '../variables/rutas';
export default {
    name:'FormExamen',
    components:{
        Combo, Card
    },
    data() {
        return {
            get_instituciones
        }
    },
    methods: {
        capturar_evento(tipo, evento){
            console.log(tipo);
            console.log(evento);
        },
    },
}
</script>