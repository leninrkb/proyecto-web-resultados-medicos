create table genero(
	id serial primary key,
	genero varchar(50) not null
);

create table persona(
	id serial primary key,
	id_genero integer not null,
	cedula varchar(10) not null,
	nombres varchar(50) not null,
	apellidos varchar(50) not null,
	fecha_nacimiento date not null,
	correo varchar(50),
	constraint fk_id_genero foreign key (id_genero) references genero(id)
    constraint uk_cedula unique (cedula)
);

create table rol_usuario(
	id serial primary key,
	rol varchar(50) not null,
	descripcion varchar(500) not null,
	constraint uk_rol unique(rol)
);

create table usuario(
	id serial primary key,
	id_persona integer not null,
	id_rol integer  not null,
	usuario varchar(50) not null,
	contrasena varchar(50) not null,
	constraint uk_usuario unique (usuario),
	constraint uk_id_persona unique (id_persona),
	constraint fk_id_rol foreign key (id_rol) references rol_usuario(id)
    constraint fk_id_persona foreign key (id_persona) references persona(id)
);

create table estado_examen(
	id serial primary key,
	estado varchar(50) not null,
	descripcion varchar(500) not null,
	constraint uk_estado unique(estado)
);

create table tipo_examen(
	id serial primary key,
	tipo varchar(100) not null,
	referencia varchar(500) not null,
	descripcion varchar(500) not null,
	precio numeric(7,2) not null,
	constraint uk_tipo unique(tipo)
);

create table institucion(
	id serial primary key,
	institucion varchar(200) not null,
	razon_social varchar(500) not null,
	descripcion varchar(500) not null,
	ubicacion varchar(500) not null,
	path_img text not null,
	constraint uk_institucion unique(institucion)
);

create table examen(
	id serial primary key,
	id_institucion integer not null,
	id_persona integer not null,
	id_estado integer not null,
	examen varchar(200) not null,
	motivo varchar(500) not null,
	fecha_realiza date not null,
	observacion varchar(500) not null,
	constraint fk_id_institucion foreign key (id_institucion) references institucion(id),
	constraint fk_id_persona foreign key (id_persona) references persona(id) on delete cascade, 
	constraint fk_id_estado foreign key (id_estado) references estado_examen(id) 
);

create table detalle_examen(
	id serial primary key,
	id_examen integer not null,
	id_tipo integer not null,
	id_estado integer not null,
	resultado varchar(500) not null,
	observacion varchar(500) not null,
	constraint fk_id_examen foreign key (id_examen) references examen(id) on delete cascade,
	constraint fk_id_tipo foreign key (id_tipo) references tipo_examen(id), 
	constraint fk_id_estado foreign key (id_estado) references estado_examen(id),
	constraint uk_id_examen_tipo unique(id_examen, id_tipo)
);

