create table ficha_medica (
    id serial PRIMARY KEY,
    diagnostico VARCHAR(50),
    alergias VARCHAR(50),
    tipo_sangre VARCHAR(50),
    peso INT,
    inter_quirurgica VARCHAR(50),
    enfer_cronica VARCHAR(50),
    paciente_id INT
);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Por Diagnosticar', 'NO', 'A', 87, 'NO', 'Demencia', 15);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Por Diagnosticar', 'NO', 'A', 42, 'NO', 'NO', 14);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Por Diagnosticar', 'NO', 'A', 60, 'NO', 'NO', 13);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Desmayo', 'NO', 'A', 79, 'Aneurisma cardiaco', 'NO', 12);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Trabajo de parto', 'Farmacos', 'B', 31, 'Biopsia Intestinal', 'NO', 11);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Trabajo de parto', 'Farmacos', 'B', 51, 'Neumonectomia', 'NO', 10);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Ataque Cardio Vascular', 'Alimentos', 'B', 42, 'Lobectomia', 'NO', 9);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Lesion Grave', 'Alimentos', 'B', 79, 'Laringectomia', 'NO', 8);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Lesion Grave', 'Alimentos', 'AB', 84, 'Laringectomia', 'NO', 7);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Lesion Leve', 'Alimentos y Farmacos', 'AB', 51, 'NO', 'VIH', 6);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Lesion Leve', 'Alimentos y Farmacos', 'AB', 34, 'NO', 'Parkinson', 5);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Lesion Leve', 'NO', 'AB', 51, 'NO', 'Hipertension', 4);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Consulta Regular', 'NO', 'O', 44, 'Biopsia Cerebral', 'Artritis', 2);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Consulta Regular', 'NO', 'B', 54, 'Biopsia Cerebral', 'Artritis', 3);

insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, enfer_cronica, paciente_id) values ('Consulta Regular', 'Alimentos', 'O', 51, 'Amputacion Extremidad Inferior', 'Artritis', 1);
