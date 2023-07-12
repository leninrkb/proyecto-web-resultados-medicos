<template lang="es">
    <h3 class="text-gray-200 font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
    <br>
    <TablaExamenesPacientes></TablaExamenesPacientes>
</template>
<script>
import TablaExamenesPacientes from './TablaExamenesPacientes.vue';

export default {
    name:'ExamenesPacientes',
    components:{
        TablaExamenesPacientes
    }
}
</script>