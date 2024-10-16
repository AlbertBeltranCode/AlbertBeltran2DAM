<?php

// Configura PHP para mostrar todos los errores y advertencias
ini_set("display_errors", 1);
ini_set("display_startup_errors", 1);
error_reporting(E_ALL);

// Establece una conexión a la base de datos MySQL y maneja el error en caso de fallo
($enlace = mysqli_connect("localhost", "accesoadatos", "accesoadatos", "accesoadatos")) or die("error");

// Lee el contenido del archivo "004-modelodedatos.json" y lo almacena en la variable $json
$json = file_get_contents("004-modelodedatos.json");

// Convierte el contenido JSON en un array asociativo PHP
$datos = json_decode($json, true);

// Itera sobre el array $datos utilizando un bucle foreach
foreach ($datos as $dato) {
	// Extrae el valor de la clave "nombre" de cada elemento del array $dato
	$nombredetabla = $dato["nombre"];

	// Inicia la construcción de la cadena SQL para crear la tabla
	$cadena = "CREATE TABLE " . $nombredetabla . " ( Identificador INT NOT NULL AUTO_INCREMENT , ";

	// Itera sobre las columnas definidas en el array $dato
	foreach ($dato["columnas"] as $columna) {
		// Añade la definición de cada columna a la cadena SQL
		$cadena .= $columna["nombre"] . " " . $columna["tipo"] . " ";
		// Si el tipo de columna no es TEXT, agrega la longitud
		if ($columna["tipo"] != "TEXT") {
			$cadena .= " (" . $columna["longitud"] . ") ";
		}
		$cadena .= ",";
	}

	// Agrega la clave primaria a la cadena SQL
	$cadena .= "PRIMARY KEY (Identificador) ";

	// Cierra la definición de la tabla en la cadena SQL y especifica el motor de almacenamiento
	$cadena .= " )  ENGINE = InnoDB";

	// Muestra la cadena SQL generada
	echo $cadena;

	// Ejecuta la consulta SQL para crear la tabla
	mysqli_query($enlace, $cadena);
}
?>


