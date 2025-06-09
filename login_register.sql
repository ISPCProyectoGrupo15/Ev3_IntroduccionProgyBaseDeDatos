-- CREACION DE LA BASE DE DATOS  Y LO BORRA SI ES QUE
-- EXISTE ESA BASE DE DATOS

DROP DATABASE IF EXISTS login_register;
CREATE DATABASE login_register; 

-- Creacion Tabla Roles 
CREATE TABLE rol (
        role_id_1 INT NOT NULL PRIMARY KEY 
    ,   role_name VARCHAR(20)
);

-- Creacion Tabla Usuarios 
CREATE TABLE usuarios (
        id_user INT NOT NULL PRIMARY KEY  AUTO_INCREMENT
    ,   id_role INT NOT NULL
    ,   username VARCHAR(20)
    ,   email  VARCHAR(256) UNIQUE
    ,   first_name VARCHAR(50)
    ,   last_name VARCHAR(50)
    ,   passwordHash VARCHAR(256)
    ,   fecha_nacimiento DATETIME
    
    ,   CONSTRAINT FK_role FOREIGN KEY (id_role)
        REFERENCES rol (role_id_1)
);

-- Crear Roles
INSERT INTO rol (role_id_1, role_name) VALUES 
(1, 'ADMIN'),
(2, 'STANDARD_USER');

-- Crear Usuarios
INSERT INTO usuarios (id_role, username, email, first_name, last_name, passwordHash, fecha_nacimiento) VALUES 
(1, 'admin01', 'admin@gmail.com', 'Juan', 'opazo', 'admin123', '1990-05-15'),
(2, 'user01', 'luvarela@hotmail.com', 'Luciana', 'varela', 'lu1234', '1992-08-22'),
(2, 'user02', 'juyu@gamil.com', 'juan', 'yunes', 'jy1234', '1985-12-10'),
(2, 'user03', 'alelopez@yahoo.com', 'Ale', 'lopez', 'ale123', '1995-03-18');

-- Actualizar Usuarios por Id
UPDATE usuarios 
SET 
    email = 'Csanchez@yahoo.com',
    first_name = 'Cesar',
    last_name = 'Sanchez',
    passwordHash = 'cs12345'
WHERE id_user = 3;

-- Elimianar Usuarios por Id
DELETE FROM usuarios WHERE id_user = 4;


-- Leer Usuarios 
SELECT * FROM login_register.usuarios;

SELECT * FROM login_register.usuarios WHERE login_register.usuarios.id_role = 2;

-- Leer Roles
SELECT * FROM login_register.rol;