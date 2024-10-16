<?php

class conexionDB // Defino una nueva clase para manejar la conexión a la base de datos
{
	private $servidor; // Declaro una propiedad privada para el servidor de la base de datos
	private $usuario; // Declaro una propiedad privada para el usuario de la base de datos
	private $contrasena; // Declaro una propiedad privada para la contraseña de la base de datos
	private $basededatos; // Declaro una propiedad privada para el nombre de la base de datos
	private $conexion; // Declaro una propiedad privada para la conexión a la base de datos

	public function __construct()
	{
		// Constructor de la clase
		// Inicializo las propiedades con los datos de conexión
		$this->servidor = "localhost"; // Asigno el servidor de la base de datos
		$this->usuario = "crimson"; // Asigno el nombre de usuario para la base de datos
		$this->contrasena = "crimson"; // Asigno la contraseña para la base de datos
		$this->basededatos = "crimson"; // Asigno el nombre de la base de datos

		// Establezco la conexión a la base de datos utilizando los datos proporcionados
		$this->conexion = mysqli_connect($this->servidor, $this->usuario, $this->contrasena, $this->basededatos);
	}

	public function seleccionaTabla($tabla)
	{
		// Método para seleccionar registros de una tabla
		// Formulo una consulta SQL para obtener información sobre las columnas con restricciones en la tabla especificada
		$query =
			"SELECT 
				*
			FROM 
				information_schema.key_column_usage
			WHERE 
				table_name = '" .
			$tabla .
			"'
				AND
				REFERENCED_TABLE_NAME IS NOT NULL
				;"; // Solo selecciona columnas que tienen restricciones (foreign keys)

		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta contra la base de datos
		$restricciones = []; // Inicializo un array vacío para guardar las restricciones

		// Recupero los datos del servidor y los almaceno en el array $restricciones
		while ($row = mysqli_fetch_assoc($result)) {
			$restricciones[] = $row; // Agrego cada restricción al array
		}

		// Formulo una consulta SQL para seleccionar todos los registros de la tabla especificada
		$query = "SELECT * FROM " . $tabla . ";";
		$result = mysqli_query($this->conexion, $query);

		$resultado = []; // Inicializo un array vacío para guardar los resultados

		// Recupero los datos del servidor y los almaceno en el array $resultado
		while ($row = mysqli_fetch_assoc($result)) {
			$fila = []; // Inicializo un array vacío para guardar cada fila
			foreach ($row as $clave => $valor) {
				$pasas = true; // Asumo que no hay restricción en la columna
				foreach ($restricciones as $restriccion) {
					if ($clave == $restriccion["COLUMN_NAME"]) {
						// Si la columna tiene una restricción, realizo otra consulta para obtener los datos referenciados
						$query2 =
							"
							SELECT * 
							FROM " .
							$restriccion["REFERENCED_TABLE_NAME"] .
							"
							;";
						$result2 = mysqli_query($this->conexion, $query2);
						$cadena = ""; // Inicializo un string vacío para concatenar los datos referenciados
						while ($row2 = mysqli_fetch_assoc($result2)) {
							foreach ($row2 as $campo) {
								$cadena .= $campo . "-"; // Concateno los campos referenciados con un guion
							}
						}

						$fila[$clave] = rtrim($cadena, "-"); // Almaceno la cadena de datos referenciados en la fila y elimino el último guion
						$pasas = false; // Cambiamos el estado de la variable a falso
					}
				}
				if ($pasas == true) {
					// Si no hay restricciones, guardo el valor original
					$fila[$clave] = $valor; // En ese caso el valor de la variable es el valor real de la tabla
				}
			}
			$resultado[] = $fila; // Agrego la fila al resultado
		}

		$json = json_encode($resultado, JSON_PRETTY_PRINT); // Codifico el resultado como JSON
		return $json; // Devuelvo el JSON
	}

	public function listadoTablas()
	{
		// Método para obtener un listado de tablas en la base de datos
		$query = "SHOW TABLES;"; // Formulo una consulta SQL para obtener el listado de tablas
		$result = mysqli_query($this->conexion, $query);

		$resultado = []; // Inicializo un array vacío para guardar los resultados

		// Recupero los datos del servidor y los almaceno en el array $resultado
		while ($row = mysqli_fetch_assoc($result)) {
			$fila = [];
			foreach ($row as $clave => $valor) {
				$fila[$clave] = $valor;
			}
			$resultado[] = $fila;
		}

		$json = json_encode($resultado, JSON_PRETTY_PRINT); // Codifico el resultado como JSON
		return $json; // Devuelvo el JSON
	}

	public function insertaTabla($tabla, $valores)
	{
		// Método para insertar un nuevo registro en una tabla
		$campos = ""; // Inicializo un string vacío para guardar los campos
		$datos = ""; // Inicializo un string vacío para guardar los datos

		// Formulo la consulta SQL para insertar el registro
		foreach ($valores as $clave => $valor) {
			$campos .= $clave . ","; // Agrego el nombre del campo al string
			$datos .= "'" . $valor . "',"; // Agrego el valor del campo al string
		}
		$campos = substr($campos, 0, -1); // Elimino la última coma del string
		$datos = substr($datos, 0, -1); // Elimino la última coma del string

		$query =
			"
			INSERT INTO " .
			$tabla .
			" 
			(" .
			$campos .
			") 
			VALUES (" .
			$datos .
			");
			"; // Formulo la consulta SQL para insertar el registro

		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta contra la base de datos
		return 0; // Devuelvo un valor de éxito
	}

	public function actualizaTabla($tabla, $valores, $id)
	{
		// Método para actualizar un registro en una tabla
		$query =
			"
			UPDATE " .
			$tabla .
			" 
			SET
			"; // Formulo la consulta SQL para actualizar el registro

		foreach ($valores as $clave => $valor) {
			$query .= $clave . "='" . $valor . "', "; // Agrego los campos y valores a la consulta
		}
		$query = substr($query, 0, -2); // Elimino los dos últimos caracteres de la consulta
		$query .=
			"
			WHERE Identificador = " .
			$id .
			"
			"; // Agrego la cláusula WHERE para especificar el registro a actualizar

		echo $query; // Imprimo la consulta SQL para depuración
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta contra la base de datos
		return ""; // Devuelvo un valor vacío
	}

	public function eliminaTabla($tabla, $id)
	{
		// Método para eliminar un registro en una tabla
		$query =
			"
			DELETE FROM " .
			$tabla .
			" 
			WHERE Identificador = " .
			$id .
			"
			"; // Formulo la consulta SQL para eliminar el registro

		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta contra la base de datos
	}

	private function codifica($entrada)
	{
		// Método privado para codificar una cadena utilizando base64
		return base64_encode($entrada);
	}

	private function decodifica($entrada)
	{
		// Método privado para decodificar una cadena utilizando base64
		return base64_decode($entrada);
	}
}

?>
