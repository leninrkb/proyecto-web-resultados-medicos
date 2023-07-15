import axios from 'axios';
import { get_examenes, get_personas, get_instituciones, get_estados } from './rutas';

export const InstitucionService = {
    async get_instituciones() {
        try {
            let resp = await axios.get(get_instituciones);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
    async get_instituciones_id(id) {
        try {
            let resp = await axios.get(get_instituciones + id);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    }
};

export const EstadoService = {
    async get_estados() {
        try {
            let resp = await axios.get(get_estados);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    }
};

export const PersonaService = {
    async get_personas() {
        try {
            let resp = await axios.get(get_personas);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    }
};

export const ExamenService = {
    async get_examenes() {
        try {
            let resp = await axios.get(get_examenes);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    }
};

export default { InstitucionService, EstadoService, PersonaService, ExamenService };