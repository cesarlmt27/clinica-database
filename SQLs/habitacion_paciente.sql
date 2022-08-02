create table habitacion_paciente (
    id serial PRIMARY KEY,
    clinica_id INT,
    numero_habitacion INT,
    paciente_id INT,
    estado boolean  
);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (1,1, 14, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (1,2, 12, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (1,3, 10, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (1,4, 8, true);

insert into habitacion_paciente (clinica_id,numero_habitacion,  paciente_id, estado) values (2,1, 6, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (2,2, 4, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (3,1, 2, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (3,2, 15, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (3,3, 13, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (4,1, 11, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (4,2, 9, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (4,3, 7, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (4,4, 5, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (5,1, 3, true);

insert into habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) values (1,5, 1, true);



