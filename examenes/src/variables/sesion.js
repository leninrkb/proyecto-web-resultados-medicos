import { defineStore } from 'pinia';

export const sesion = defineStore('session', {
    state: () => ({
        usuario: undefined,
        contrasena: undefined,
        id_rol: undefined
    }),
    actions:{
        nuevaSesion(usuario){
            this.usuario = usuario.usuario;
            this.contrasena = usuario.contrasena;
            this.id_rol = usuario.id_rol;
        },
        terminarSesion(){
            this.usuario = undefined;
            this.contrasena = undefined;
            this.id_rol = undefined;
        }
    }
  });