<template lang="es">
    <div class="text-gray-200 font-sans">
        <h3 class="font-sans text-xl capitalize">Todos los examenes de los pacientes</h3>
        <br>
        <h3><strong>Seleccionado: </strong> {{examen.persona == undefined ? 'ninguno' : 'ID ' + examen.persona.id +' - '+ examen.persona.nombres}}</h3>
    </div>
    <Tabla :mostrar="termino_pacientes" :datos="pacientes" @fila="capturar_fila" @recargar="recargar"></Tabla>
</template>
<script>
import Tabla from '../../components/ui/Tabla.vue';
import { GeneroService, PersonaService } from '../../variables/servicios';
import { examen } from '../../variables/examen';

export default {
    name: 'Pacientes',
    components: {
        Tabla
    },
    data() {
        return {
            pacientes: { titulos: undefined, registros: undefined },
            termino_pacientes: false,
            generos: undefined,
            examen: examen()
        }
    },
    methods: {
        async cargar_personas() {
            this.termino_pacientes = false;
            try {
                this.generos = await GeneroService.get_generos();
                this.pacientes.titulos = ['id', 'cedula', 'nombres', 'apellidos', 'fecha_nacimiento', 'genero'];
                this.pacientes.registros = await PersonaService.get_personas();
                this.pacientes.registros.forEach(element => {
                    let genero_tmp = this.generos.find(genero => genero.id == element.id_genero);
                    element.genero = genero_tmp.genero;
                });
                this.termino_pacientes = true;
            } catch (error) {
                this.termino_pacientes = true;
            }
        },
        recargar(){
            this.cargar_personas();
        },
        capturar_fila(fila){
            this.examen.setPersona(fila);
        },
    },
    mounted() {
        this.cargar_personas();
    },
}
</script>