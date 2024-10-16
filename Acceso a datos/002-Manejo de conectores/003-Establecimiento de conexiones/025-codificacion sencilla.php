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
		// Inicializo las propiedades de conexión
		$this->servidor = "localhost"; // Asigno el servidor de la base de datos
		$this->usuario = "accesoadatos"; // Asigno el usuario de la base de datos
		$this->contrasena = "accesoadatos"; // Asigno la contraseña de la base de datos
		$this->basededatos = "accesoadatos"; // Asigno el nombre de la base de datos

		$this->conexion = mysqli_connect($this->servidor, $this->usuario, $this->contrasena, $this->basededatos); // Establezco la conexión con la base de datos
	}
	public function seleccionaTabla($tabla)
	{
		// Método para seleccionar datos de una tabla
		// Construyo la consulta SQL
		$query = "SELECT * FROM " . $tabla . ";"; // Formulo la consulta dinámica
		$result = mysqli_query($this->conexion, $query); // Ejecuto la consulta
		$resultado = []; // Inicializo un array vacío para los resultados
		while ($row = mysqli_fetch_assoc($result)) {
			// Itero sobre cada fila del resultado
			$resultado[] = $row; // Agrego cada fila al array de resultados
		}
		$json = json_encode($resultado, JSON_PRETTY_PRINT); // Codifico el array como JSON
		return $json; // Devuelvo el JSON resultante
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

?>
