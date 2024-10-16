<?php
if (isset($_POST["usuario"])) {
	// Configuración de errores: muestra todos los errores y advertencias
	ini_set("display_errors", 1);
	ini_set("display_startup_errors", 1);
	error_reporting(E_ALL);

	// Establece conexión a la base de datos MySQL, mostrando un error si falla
	($enlace = mysqli_connect($_POST["servidor"], $_POST["usuario"], $_POST["contrasena"], $_POST["basededatos"])) or
		die("error");

	// Lee el contenido del archivo JSON que contiene la definición de la base de datos
	$json = file_get_contents("004-modelodedatos.json");
	// Convierte el contenido JSON en un array asociativo de PHP
	$datos = json_decode($json, true);

	// Itera sobre cada tabla definida en el JSON
	foreach ($datos as $dato) {
		// Extrae el nombre de la tabla
		$nombredetabla = $dato["nombre"];

		// Inicia la construcción de la cadena SQL para crear la tabla
		$cadena =
			"CREATE TABLE " .
			$nombredetabla .
			" ( 
				  Identificador INT NOT NULL AUTO_INCREMENT , ";

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

		// Ejecuta la consulta SQL para crear la tabla
		mysqli_query($enlace, $cadena);
	}
} else {
	// Código a ejecutar si no se ha enviado el formulario
	?>
<!doctype html>
<html>
	<head>
		<title>
			Instalador de bases de datos
		</title>
	</head>
	<body>
		<form method="POST" action="?">
		<h1>Instalador</h1>
			<input type="text" name="usuario" placeholder="Usuario de la base de datos">
			<input type="text" name="contrasena" placeholder="Contraseña de la base de datos">
			<input type="text" name="servidor" placeholder="Servidor de la base de datos">
			<input type="text" name="basededatos" placeholder="Nombre de la base de datos">
			<input type="submit">
		</form>
	</body>
</html>

<?php
} ?>


