import { defineStore } from 'pinia';

export const examen = defineStore('examen', {
    state: () => ({
        examen: undefined,
        detalle: undefined,
        persona: undefined,
        institucion: undefined
    }),
    actions:{
        eliminarExamen(){
            this.examen = undefined;
            this.detalle = undefined;
            this.persona = undefined;
            this.institucion = undefined;
        },
        setPersona(persona){
            this.persona = persona;
        },
        setExamen(examen){
            this.examen = examen;
        },
        setDetalle(detalle){
            this.detalle = detalle;
        },
        setInstitucion(institucion){
            this.institucion = institucion;
        },
    }
  });