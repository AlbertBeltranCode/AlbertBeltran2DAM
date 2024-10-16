<?php

// Establece una conexión a la base de datos MySQL
($enlace = mysqli_connect(
	"localhost", // El servidor de la base de datos (localhost en este caso)
	"accesoadatos", // Nombre de usuario para la conexión
	"accesoadatos", // Contraseña para el usuario
	"accesoadatos" // Nombre de la base de datos a la que se conecta
)) or die("error");
// Si la conexión falla, muestra un mensaje de error
?>

