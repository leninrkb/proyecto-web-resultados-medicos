import { defineStore } from 'pinia';

export const examen = defineStore('examen', {
    state: () => ({
        examen: undefined,
        detalle: undefined,
        persona: undefined
    }),
    actions:{
        eliminarExamen(){
            this.examen = undefined;
            this.detalle = undefined;
            this.persona = undefined;
        },
        setPersona(persona){
            this.persona = persona;
        },
    }
  });