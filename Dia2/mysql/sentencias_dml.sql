-- SENTENCIAS DML
-- CRUD
-- C - INSERT
-- R - SELECT
-- U - UPDATE
-- D - DELETE

-- INSERT

insert into
    alumno (Nro_documento, Nombre)
values ('100', 'Paul Zapana');
-- INSERTAR VARIOS REGISTROS

insert into
    alumno (Nro_documento, Nombre)
VALUES ('200', 'Ana Martinez'),
    ('300', 'Luis Lopez'),
    ('400', 'Arturo Gonzales'),
    ('500', 'Monica Tejada'),
    ('600', 'Raul Rivera'),
    ('700', 'Andrea Valencia'),
    ('800', 'Sofia Mamani'),
    ('900', 'Carlos Perez'),
    ('1000', 'Jesus Concha');

-- ACTUALIZAR DATOS(UPDATE)
update alumno SET Email = 'codigo@gmail.com';

-- UPDATE CON WHERE
update alumno set Email = 'paulvargas0894@gmail.com' where id = 1;

-- UPDATE CON FUNCIONES
update alumno
set
    Email = CONCAT(
        lower(
            replace (Nombre, ' ', '.')
        ),
        '@gmail.com'
    )
where
    id > 1;

-- SELECT
select * from alumno;

select Nombre, Email from alumno;

select Nombre from alumno where id > 5;

select * from alumno order by Nombre asc;

-- DELETE
delete from alumno where id = 20;

delete from alumno;

truncate table alumno;