<?php

// Establece una conexión a la base de datos MySQL y maneja el error en caso de fallo
($enlace = mysqli_connect("localhost", "accesoadatos", "accesoadatos", "accesoadatos")) or die("error");

// Lee el contenido del archivo "004-modelodedatos.json" y lo almacena en la variable $json
$json = file_get_contents("004-modelodedatos.json");

// Convierte el contenido JSON en un array asociativo PHP
$datos = json_decode($json, true);

// Muestra el contenido del array $datos utilizando la función var_dump
var_dump($datos);

// Agrega un salto de línea para separar la salida
echo "<br><br>";

// Itera sobre el array $datos utilizando un bucle foreach
foreach ($datos as $dato) {
	// Muestra el contenido de cada elemento del array $dato utilizando la función var_dump
	var_dump($dato);

	// Extrae el valor de la clave "nombre" de cada elemento del array $dato
	$nombredetabla = $dato["nombre"];

	// Construye una cadena para crear una tabla con el nombre extraído
	$cadena = "CREATE TABLE " . $nombredetabla . " ( ";
	$cadena .= " ) "; // Aquí se puede añadir la definición de columnas

	// Muestra la cadena SQL generada
	echo $cadena;
	echo "<br><br>";
}
?>