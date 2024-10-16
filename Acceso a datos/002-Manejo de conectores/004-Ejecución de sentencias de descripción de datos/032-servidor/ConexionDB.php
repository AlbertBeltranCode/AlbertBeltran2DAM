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
		// Método para seleccionar todos los registros de una tabla
		$query = "SELECT * FROM " . $tabla . ";"; // Formulo la consulta para seleccionar todos los registros de la tabla especificada
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		$resultado = []; // Inicializo un array vacío para almacenar los resultados
		while ($row = mysqli_fetch_assoc($result)) {
			// Itero sobre cada fila del resultado
			//$resultado[] = $row; // (comentado) Agregaría la fila directamente al array de resultados
			$fila = []; // Inicializo un array para almacenar los datos de la fila
			foreach ($row as $clave => $valor) {
				// Itero sobre cada clave y valor de la fila
				$fila[$clave] = $valor; // Agrego el valor al array de fila
			}
			$resultado[] = $fila; // Agrego la fila al array de resultados
		}
		$json = json_encode($resultado, JSON_PRETTY_PRINT); // Codifico el array de resultados como JSON
		return $json; // Devuelvo el JSON resultante
	}

	public function listadoTablas()
	{
		// Método para listar todas las tablas de la base de datos
		$query = "SHOW TABLES;"; // Formulo la consulta para mostrar las tablas de la base de datos
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		$resultado = []; // Inicializo un array vacío para almacenar los nombres de las tablas
		while ($row = mysqli_fetch_assoc($result)) {
			// Itero sobre cada fila del resultado
			//$resultado[] = $row; // (comentado) Agregaría la fila directamente al array de resultados
			$fila = []; // Inicializo un array para almacenar los datos de la fila
			foreach ($row as $clave => $valor) {
				// Itero sobre cada clave y valor de la fila
				$fila[$clave] = $valor; // Agrego el valor al array de fila
			}
			$resultado[] = $fila; // Agrego la fila al array de resultados
		}
		$json = json_encode($resultado, JSON_PRETTY_PRINT); // Codifico el array de resultados como JSON
		return $json; // Devuelvo el JSON resultante
	}

	public function insertaTabla($tabla, $valores)
	{
		// Método para insertar nuevos registros en una tabla
		$campos = ""; // Inicializo un string para almacenar los nombres de los campos
		$datos = ""; // Inicializo un string para almacenar los datos a insertar
		foreach ($valores as $clave => $valor) {
			// Itero sobre cada uno de los datos a insertar
			$campos .= $clave . ","; // Agrego el nombre del campo al string
			$datos .= "'" . $valor . "',"; // Agrego el dato al string, rodeado de comillas simples
		}
		$campos = substr($campos, 0, -1); // Le quito la última coma al string de campos
		$datos = substr($datos, 0, -1); // Le quito la última coma al string de datos
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
			"; // Formulo la consulta de inserción
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		return 0; // Devuelvo un valor de éxito (0)
	}

	public function actualizaTabla($tabla, $valores, $id)
	{
		// Método para actualizar registros en una tabla
		$query =
			"
			UPDATE " .
			$tabla .
			" 
			SET
			"; // Formulo la consulta de actualización
		foreach ($valores as $clave => $valor) {
			// Itero sobre cada uno de los datos a actualizar
			$query .= $clave . "='" . $valor . "', "; // Agrego la asignación de valor al string
		}
		$query = substr($query, 0, -2); // Le quito los dos últimos caracteres (coma y espacio)
		$query .=
			"
			WHERE Identificador = " .
			$id .
			"
			"; // Agrego la cláusula WHERE para especificar el registro a actualizar
		echo $query; // Muestro la consulta de actualización
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		return ""; // Devuelvo un valor vacío
	}

	public function eliminaTabla($tabla, $id)
	{
		// Método para eliminar registros en una tabla
		$query =
			"
			DELETE FROM " .
			$tabla .
			" 
			WHERE Identificador = " .
			$id .
			"
			"; // Formulo la consulta de eliminación
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
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
