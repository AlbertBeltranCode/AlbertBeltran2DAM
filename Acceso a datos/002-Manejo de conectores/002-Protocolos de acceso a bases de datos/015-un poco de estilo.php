<?php
if (isset($_POST["usuario"])) {
	// Verifica si se ha enviado el formulario con el campo "usuario"
	ini_set("display_errors", 1); // Habilita la visualización de errores de PHP
	ini_set("display_startup_errors", 1); // Habilita la visualización de errores de inicio
	error_reporting(E_ALL); // Configura el nivel de reporte de errores para mostrar todos

	// Intenta conectarse a la base de datos usando las credenciales proporcionadas
	($enlace = mysqli_connect($_POST["servidor"], $_POST["usuario"], $_POST["contrasena"], $_POST["basededatos"])) or
		die("error"); // Termina el script y muestra un mensaje de error si la conexión falla

	$json = file_get_contents("004-modelodedatos.json"); // Lee el contenido del archivo JSON que define la estructura de la base de datos
	$datos = json_decode($json, true); // Decodifica el JSON a un array asociativo de PHP

	foreach ($datos as $dato) {
		// Itera sobre cada tabla definida en el JSON
		$nombredetabla = $dato["nombre"]; // Obtiene el nombre de la tabla actual
		$cadena =
			"CREATE TABLE " .
			$nombredetabla .
			" ( 
				  Identificador INT NOT NULL AUTO_INCREMENT , "; // Inicia la cadena SQL para crear la tabla con el identificador

		foreach ($dato["columnas"] as $columna) {
			// Itera sobre las columnas definidas para la tabla
			$cadena .= $columna["nombre"] . " " . $columna["tipo"] . " "; // Añade la definición de cada columna a la cadena SQL
			if ($columna["tipo"] != "TEXT") {
				// Verifica si el tipo de columna no es TEXT
				$cadena .= " (" . $columna["longitud"] . ") "; // Añade la longitud de la columna si aplica
			}
			$cadena .= ","; // Añade una coma al final de la definición de cada columna
		}
		$cadena .= "PRIMARY KEY (Identificador) "; // Añade la clave primaria a la definición de la tabla
		$cadena .= " )  ENGINE = InnoDB"; // Especifica el motor de almacenamiento para la tabla
		// echo $cadena; // Muestra la cadena SQL generada para depuración (comentado)
		mysqli_query($enlace, $cadena); // Ejecuta la consulta SQL para crear la tabla en la base de datos
	}
} else {
	// Si no se ha enviado el formulario
	?>
<!doctype html>
<html>
	<head>
		<title>
			Instalador de bases de datos
		</title>
		<style>
			body,html{ /* Estilos para el cuerpo y el documento HTML */
				height:100%;padding:0px;margin:0px; /* Configura la altura, el padding y el margen */
				background:url(fondo.jpg);background-size:cover; /* Establece una imagen de fondo que cubre toda la pantalla */
			}
			form{ /* Estilos para el formulario */
				width:300px;height:400px;background:rgba(255,255,255,0.5); /* Define el tamaño y el fondo del formulario */
				box-sizing:border-box;padding:20px;border-radius:20px; /* Ajusta el box model y redondea las esquinas */
				position:absolute;top:50%;left:50%;margin-left:-150px;margin-top:-200px; /* Centra el formulario en la pantalla */
				text-align:center;color:white; /* Alinea el texto al centro y establece el color del texto */
				backdrop-filter:blur(20px); /* Aplica un efecto de desenfoque al fondo del formulario */
			}
			form input{ /* Estilos para los campos de entrada dentro del formulario */
				width:100%;padding:10px 0px;margin:5px 0px; /* Define el tamaño y el margen de los campos */
				outline:none;border:none;border-bottom:1px solid white;background:none; /* Elimina el borde y establece el estilo del fondo */
			}
			form input::placeholder{ /* Estilos para el texto de los placeholders en los campos de entrada */
				color:white; /* Establece el color del texto del placeholder */
			}
			form input[type=submit]{ /* Estilos específicos para el botón de envío */
				background:white; /* Establece el fondo del botón */
				border-radius:20px; /* Redonde a las esquinas del botón */
				color:black; /* Establece el color del texto del botón */
			}
		</style>
	</head>
	<body>
		<form method="POST" action="?"> <!-- Formulario que envía los datos al mismo archivo PHP -->
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

