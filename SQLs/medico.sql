create table medico (
	id serial PRIMARY KEY,
	nombre VARCHAR(50),
	apellido VARCHAR(50),
	edad INT,
	rut INT,
	dv VARCHAR(1),
	especialidad VARCHAR(50),
	clinica_id INT
);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Belva', 'Kosel', 42, 26218137, 4, 'Geriatria',1);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Fidelio', 'Wankling', 56, 26084763, 1, 'Radiologia',2);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Portia', 'Lilloe', 55, 20698750, 4, 'Oncologia',5);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Bernadette', 'Skelcher', 44, 28531184, 0, 'Cirugia Digestiva',4);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Gloriane', 'Downing', 57, 25993222, 9, 'Cardiologia',3);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Brana', 'Mensler', 29, 15606029, 6, 'Anestesia',3);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Zelda', 'Niche', 44, 28895192, 9, 'Psiquiatria',1);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Charyl', 'Verduin', 36, 12217799, 4, 'Oftalmologia',2);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Jill', 'Rothera', 43, 22703801, 2, 'Neurologia',5);

insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('Griffin', 'La Grange', 48, 26384525, 5, 'Cirugia General',4);
