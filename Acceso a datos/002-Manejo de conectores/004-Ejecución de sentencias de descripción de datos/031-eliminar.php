<?php
ini_set("display_errors", 1); // Habilito la visualización de errores
ini_set("display_startup_errors", 1); // Habilito la visualización de errores de inicio
error_reporting(E_ALL); // Configuro el reporte de todos los errores

class conexionDB // Defino una nueva clase para manejar la conexión a la base de datos
{
	private $servidor; // Declaro una propiedad privada para el servidor
	private $usuario; // Declaro una propiedad privada para el usuario
	private $contrasena; // Declaro una propiedad privada para la contraseña
	private $basededatos; // Declaro una propiedad privada para la base de datos
	private $conexion; // Declaro una propiedad privada para la conexión a la base de datos

	public function __construct()
	{
		// Constructor de la clase
		$this->servidor = "localhost"; // Asigno el servidor de la base de datos
		$this->usuario = "accesoadatos"; // Asigno el usuario de la base de datos
		$this->contrasena = "accesoadatos"; // Asigno la contraseña de la base de datos
		$this->basededatos = "accesoadatos"; // Asigno el nombre de la base de datos

		$this->conexion = mysqli_connect($this->servidor, $this->usuario, $this->contrasena, $this->basededatos); // Establezco la conexión con la base de datos
	}

	public function seleccionaTabla($tabla)
	{
		// Método para seleccionar datos de una tabla
		$query = "SELECT * FROM " . $tabla . ";"; // Formulo la consulta dinámica para seleccionar todos los registros
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		$resultado = []; // Inicializo un array vacío para almacenar los resultados
		while ($row = mysqli_fetch_assoc($result)) {
			// Itero sobre cada fila del resultado
			//$resultado[] = $row; // Los añado al array (comentado)
			$fila = []; // Inicializo un array para la fila actual
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
		// Método para listar las tablas de la base de datos
		$query = "SHOW TABLES;"; // Formulo la consulta para mostrar todas las tablas
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		$resultado = []; // Inicializo un array vacío para almacenar los resultados
		while ($row = mysqli_fetch_assoc($result)) {
			// Itero sobre cada fila del resultado
			//$resultado[] = $row; // Los añado al array (comentado)
			$fila = []; // Inicializo un array para la fila actual
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
		$campos = ""; // Inicializo un string para guardar los nombres de los campos
		$datos = ""; // Inicializo un string para guardar los datos a insertar
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
		"; // Preparo la consulta de inserción
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		return 0; // Devuelvo 0 para indicar que la inserción fue exitosa
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
			"; // Empiezo a formatear la consulta de actualización
		foreach ($valores as $clave => $valor) {
			// Itero sobre cada uno de los datos a actualizar
			$query .= $clave . "='" . $valor . "', "; // Agrego el campo y valor al string de actualización
		}
		$query = substr($query, 0, -2); // Le quito los dos últimos caracteres al string de actualización
		$query .=
			"
			WHERE Identificador = " .
			$id .
			"
			"; // Agrego la cláusula WHERE para especificar el registro a actualizar
		echo $query; // Muestro la consulta de actualización
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		return ""; // Devuelvo un string vacío
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
			"; // Preparo la consulta de eliminación
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
	}

	private function codifica($entrada)
	{
		// Método privado para codificar strings en base64
		return base64_encode($entrada); // Codifico la entrada en base64
	}

	private function decodifica($entrada)
	{
		// Método privado para decodificar strings en base64
		return base64_decode($entrada); // Decodifico la entrada en base64
	}
}

$conexion = new conexionDB(); // Instancio la clase de conexión

echo $conexion->eliminaTabla("clientes", "5"); // Ejecuto el método de eliminación
?>
