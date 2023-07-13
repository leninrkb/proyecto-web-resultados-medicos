export const home = '/';
export const registro = 'registro';
export const examenes_disponibles = '/examenes_disponibles';
export const login = '/login';

// admin
export const inicio_admin = '/inicio';
export const examenes_pacientes = inicio_admin + '/examenes';
export const disponibles = inicio_admin + '/disponibles';
export const pacientes = inicio_admin + '/pacientes';

//api
export const get_generos = 'http://127.0.0.1:8000/genero/get';
export const create_persona = 'http://127.0.0.1:8000/persona/create';
export const create_usuario = 'http://127.0.0.1:8000/usuario/create';
export const get_roles_usuarios = 'http://127.0.0.1:8000/rol_usuario/get';
export const delete_persona = 'http://127.0.0.1:8000/persona/delete/';
export const autenticar = 'http://127.0.0.1:8000/usuario/autenticar/';
export const get_examenes = 'http://127.0.0.1:8000/examen/get/';
export const get_examen_id = 'http://127.0.0.1:8000/examen/get/';