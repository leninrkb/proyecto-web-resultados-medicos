create table genero(
	id serial primary key,
	genero varchar(50) not null
);

create table persona(
	id serial primary key,
	cedula varchar(10) not null,
	nombres varchar(50) not null,
	apellidos varchar(50) not null,
	fecha_nacimiento date not null,
	id_genero integer not null,
	constraint fk_id_genero foreign key (id_genero) references genero(id)
    constraint uk_cedula unique (cedula)
);

create table rol_usuario(
	id serial primary key,
	rol varchar(50) not null,
	descripcion varchar(50) not null,
	constraint uk_descripcion unique(rol)
);

create table usuario(
	id serial primary key,
	id_persona integer not null,
	usuario varchar(50) not null,
	contrasena varchar(50) not null,
	id_rol integer  not null,
	constraint uk_usuario unique (usuario),
	constraint fk_id_rol foreign key (id_rol) references rol_usuario(id)
    constraint fk_id_persona foreign key (id_persona) references persona(id)
);

