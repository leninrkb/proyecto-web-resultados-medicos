import axios from 'axios';
import { 
    get_generos, 
    get_examenes, 
    get_personas, 
    get_instituciones, 
    get_estados, 
    get_examen_id,
    get_tipos_examen,
    get_detalle
} from './rutas';

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
    },
    async get_persona_id(id) {
        try {
            let resp = await axios.get(get_personas + id);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
};

export const ExamenService = {
    async get_examenes() {
        try {
            let resp = await axios.get(get_examenes);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
    async get_examen_id(id) {
        try {
            let resp = await axios.get(get_examen_id + id);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
};

export const GeneroService = {
    async get_generos() {
        try {
            let resp = await axios.get(get_generos);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
    async get_genero_id(id) {
        try {
            let resp = await axios.get(get_generos + id);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
};

export const TipoExamenService = {
    async get_tipos() {
        try {
            let resp = await axios.get(get_tipos_examen);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
    async get_tipos_id(id) {
        try {
            let resp = await axios.get(get_tipos_examen + id);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
};

export const DetalleExamenService = {
    async get_detalle() {
        try {
            let resp = await axios.get(get_detalle);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
    async get_detalle_id(id) {
        try {
            let resp = await axios.get(get_detalle + id);
            return resp.data.result;
        } catch (error) {
            return false;
        }
    },
};

export default { 
    InstitucionService, EstadoService, PersonaService, ExamenService,
    TipoExamenService
};