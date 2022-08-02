create table entrada_salida_paciente (
    id serial PRIMARY KEY,
    fecha_entrada DATE,
    fecha_salida DATE,
    paciente_id INT,
    clinica_id INT,
    estado boolean
);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/07/23', '2022/01/01', 1, 1, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/01/15', '2022/11/15', 2, 1, true);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/04/19', '2022/06/29', 3, 1, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/11/19', '2022/02/23', 4, 1, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/12/04', '2022/06/17', 5, 2, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/03/08', '2022/10/14', 6, 2, true);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/08/30', '2021/09/18', 7, 3, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/10/15', '2022/02/23', 8, 3, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/09/04', '2022/01/09', 9, 3, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2022/05/18', '2022/05/19', 10, 4, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2022/01/02', '2022/04/05', 11, 4, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/07/22', '2021/08/21', 12, 4, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/11/13', '2021/11/14', 13, 4, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/06/22', '2021/07/20', 14, 5, false);

insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) values ('2021/10/29', '2022/01/06', 15, 1, true);
