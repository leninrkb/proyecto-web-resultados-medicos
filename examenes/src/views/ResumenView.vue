<template lang="es">
    <div>
        resumen view {{id_examen}}
    </div>
</template>
<script>
export default {
    name:'ResumenView',
    data() {
        return {
            id_examen: undefined
        }
    },
    methods: {
        
    },
    mounted() {
        this.id_examen = this.$route.params.id;
        
    },
}
</script>