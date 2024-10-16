<?php

// Establece una conexión a la base de datos MySQL
($enlace = mysqli_connect(
	"localhost", // El servidor de la base de datos (localhost en este caso)
	"accesoadatos", // Nombre de usuario para la conexión
	"accesoadatos", // Contraseña para el usuario
	"accesoadatos" // Nombre de la base de datos a la que se conecta
)) or die("error"); // Si la conexión falla, muestra un mensaje de error

// En caso de que ya la hayas creado, dara fatal error
// Ejecuta una consulta SQL para crear una tabla llamada 'clientes'
mysqli_query(
	$enlace,
	"
		CREATE TABLE clientes (
			Identificador INT NOT NULL AUTO_INCREMENT, 
			nombre VARCHAR(255) NOT NULL,             
			apellidos VARCHAR(255) NOT NULL,          
			PRIMARY KEY (Identificador)               
		) ENGINE = InnoDB;                            
	"
);
?>

