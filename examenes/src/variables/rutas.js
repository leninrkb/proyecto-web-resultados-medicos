export const home = '/';
export const registro = '/registro';
export const examenes_disponibles = '/examenes_disponibles';
export const login = '/login';
export const resumen = '/resumen/';

// admin
export const inicio_admin = '/inicio';
export const examenes_pacientes = inicio_admin + '/examenes';
export const disponibles = inicio_admin + '/disponibles';
export const pacientes = inicio_admin + '/pacientes';

//api
export const get_generos = 'http://127.0.0.1:8000/genero/get/';
export const create_persona = 'http://127.0.0.1:8000/persona/create';
export const create_usuario = 'http://127.0.0.1:8000/usuario/create';
export const get_roles_usuarios = 'http://127.0.0.1:8000/rol_usuario/get';
export const delete_persona = 'http://127.0.0.1:8000/persona/delete/';
export const autenticar = 'http://127.0.0.1:8000/usuario/autenticar/';
export const get_examenes = 'http://127.0.0.1:8000/examen/get/';
export const get_examen_id = 'http://127.0.0.1:8000/examen/get/';
export const get_personas = 'http://127.0.0.1:8000/persona/get/';
export const get_instituciones = 'http://127.0.0.1:8000/institucion/get/';
export const get_estados = 'http://127.0.0.1:8000/estado_examen/get/';
export const get_tipos_examen = 'http://127.0.0.1:8000/tipo_examen/get/';
export const get_detalle = 'http://127.0.0.1:8000/detalle/get/';