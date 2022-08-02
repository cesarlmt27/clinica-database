create table clinica (
    id serial PRIMARY KEY,
    nombre VARCHAR(50),
    direccion VARCHAR(50),
    telefono INT,
    cantidad_habitaciones INT
);

insert into clinica (nombre, direccion, telefono, cantidad_habitaciones) values ('Indisa', 'Los Espantapoles 1855, Providencia', '26789', 5);

insert into clinica (nombre, direccion, telefono, cantidad_habitaciones) values ('Alemana', 'Av. Vitacura 5951, Vitacura', '222101', 2);

insert into clinica (nombre, direccion, telefono, cantidad_habitaciones) values ('RedSalud', 'Av. Vitacura 4850, Vitacura', '600678', 3);

insert into clinica (nombre, direccion, telefono, cantidad_habitaciones) values ('Santa Maria', 'Av. Bellavista 0415, Providencia', '28900', 4);

insert into clinica (nombre, direccion, telefono, cantidad_habitaciones) values ('Davila', 'Av. Recoleta 464, Recoleta', '287000', 1);
