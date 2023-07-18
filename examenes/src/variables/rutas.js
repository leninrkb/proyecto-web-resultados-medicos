export const home = '/';
export const registro = '/registro';
export const examenes_disponibles = '/examenes_disponibles';
export const login = '/login';
export const resumen = 'http://localhost:8080/resumen/';



// admin
export const inicio_admin = '/inicio';
export const examenes_pacientes = inicio_admin + '/examenes';
export const administrar = inicio_admin + '/administrar';
    export const nuevo_examen = administrar + '/nuevo_examen';
    export const nuevo_detalle = administrar + '/nuevo_detalle';
    export const eliminar_examen = administrar + '/eliminar_examen';
export const pacientes = inicio_admin + '/pacientes';




//paciente
export const inicio_paciente = '/inicio_paciente';




//api
const sitio = 'http://127.0.0.1:8000';
export const get_generos = sitio + '/genero/get/';
export const create_persona = sitio + '/persona/create';
export const create_usuario = sitio + '/usuario/create';
export const get_roles_usuarios = sitio + '/rol_usuario/get';
export const delete_persona = sitio + '/persona/delete/';
export const autenticar = sitio + '/usuario/autenticar/';
export const get_examenes = sitio + '/examen/get/';
export const get_examen_id = sitio + '/examen/get/';
export const get_personas = sitio + '/persona/get/';
export const get_instituciones = sitio + '/institucion/get/';
export const get_estados = sitio + '/estado_examen/get/';
export const get_tipos_examen = sitio + '/tipo_examen/get/';
export const get_detalle = sitio + '/detalle/get/';
export const create_examen = sitio + '/examen/create';
export const create_detalle = sitio + '/detalle/create';
export const delete_examen = sitio + '/examen/delete/';
export const get_usuario = sitio + '/usuatio/get/';