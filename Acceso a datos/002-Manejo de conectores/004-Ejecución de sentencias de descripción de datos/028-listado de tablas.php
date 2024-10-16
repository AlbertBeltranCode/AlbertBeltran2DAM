<?php
ini_set("display_errors", 1); // Habilito la visualización de errores
ini_set("display_startup_errors", 1); // Habilito la visualización de errores de inicio
error_reporting(E_ALL); // Configuro el reporte de todos los errores

class conexionDB // Defino una nueva clase
{
	private $servidor; // Declaro una propiedad privada para el servidor
	private $usuario; // Declaro una propiedad privada para el usuario
	private $contrasena; // Declaro una propiedad privada para la contraseña
	private $basededatos; // Declaro una propiedad privada para la base de datos
	private $conexion; // Declaro una propiedad privada para la conexión

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
		$query = "SELECT * FROM " . $tabla . ";"; // Formulo la consulta dinámica
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		$resultado = []; // Inicializo un array vacío para los resultados
		while ($row = mysqli_fetch_assoc($result)) {
			// Itero sobre cada fila del resultado
			//$resultado[] = $row; // Los añado al array
			$fila = []; // Inicializo un array para la fila
			foreach ($row as $clave => $valor) {
				// Itero sobre cada clave y valor de la fila
				$fila[$clave] = $valor; // Agrego el valor al array de fila
			}
			$resultado[] = $fila; // Agrego la fila al array de resultados
		}
		$json = json_encode($resultado, JSON_PRETTY_PRINT); // Codifico el array como JSON
		return $json; // Devuelvo el JSON resultante
	}

	public function listadoTablas()
	{
		// Método para listar las tablas de la base de datos
		$query = "SHOW TABLES;"; // Formulo la consulta para mostrar tablas
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		$resultado = []; // Inicializo un array vacío para los resultados
		while ($row = mysqli_fetch_assoc($result)) {
			// Itero sobre cada fila del resultado
			//$resultado[] = $row; // Los añado al array
			$fila = []; // Inicializo un array para la fila
			foreach ($row as $clave => $valor) {
				// Itero sobre cada clave y valor de la fila
				$fila[$clave] = $valor; // Agrego el valor al array de fila
			}
			$resultado[] = $fila; // Agrego la fila al array de resultados
		}
		$json = json_encode($resultado, JSON_PRETTY_PRINT); // Codifico el array como JSON
		return $json; // Devuelvo el JSON resultante
	}

	public function insertaTabla($tabla, $valores)
	{
		// Método para insertar datos en una tabla
		// Implementar lógica de inserción aquí
	}

	public function actualizaTabla($tabla, $valores)
	{
		// Método para actualizar datos en una tabla
		// Implementar lógica de actualización aquí
	}

	public function eliminaTabla($tabla, $id)
	{
		// Método para eliminar datos de una tabla
		// Implementar lógica de eliminación aquí
	}

	private function codifica($entrada)
	{
		// Método privado para codificar
		return base64_encode($entrada); // Retorno la entrada codificada en base64
	}

	private function decodifica($entrada)
	{
		// Método privado para decodificar
		return base64_decode($entrada); // Retorno la entrada decodificada de base64
	}
}

$conexion = new conexionDB(); // Instancio la clase de conexión

echo $conexion->seleccionaTabla("empleados"); // Imprimo el resultado de la selección de la tabla 'empleados'
echo "<br><br>";
echo $conexion->listadoTablas(); // Imprimo el resultado del listado de tablas

?>
