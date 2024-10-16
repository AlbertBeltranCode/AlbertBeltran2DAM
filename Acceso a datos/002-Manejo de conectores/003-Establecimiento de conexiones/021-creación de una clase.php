<?php
class conexionDB // Define una clase llamada 'conexionDB'
{
	public $servidor; // Propiedad para almacenar el servidor de la base de datos
	public $usuario; // Propiedad para almacenar el nombre de usuario de la base de datos
	public $contrasena; // Propiedad para almacenar la contraseña de la base de datos
	public $basededatos; // Propiedad para almacenar el nombre de la base de datos

	public function __construct()
	{
		// Constructor de la clase
		$this->servidor = "localhost"; // Inicializa la propiedad 'servidor' con el valor 'localhost'
		$this->usuario = "accesoadatos"; // Inicializa la propiedad 'usuario' con el valor 'accesoadatos'
		$this->contrasena = "accesoadatos"; // Inicializa la propiedad 'contrasena' con el valor 'accesoadatos'
		$this->basededatos = "accesoadatos"; // Inicializa la propiedad 'basededatos' con el valor 'accesoadatos'

		$mysqli = mysqli_connect($this->servidor, $this->usuario, $this->contrasena, $this->basededatos); // Establece la conexión a la base de datos MySQL
	}
	public function seleccionaTabla($tabla)
	{
		// Define un método llamado 'seleccionaTabla' que toma un parámetro '$tabla'
		$query = "SELECT * FROM " . $tabla . ";"; // Construye la consulta SQL para seleccionar todos los registros de la tabla especificada
		$result = mysqli_query($mysqli, $query); // Ejecuta la consulta y almacena el resultado en la variable $result
		$resultado = []; // Inicializa un array vacío para almacenar los resultados
		while ($row = mysqli_fetch_assoc($result)) {
			// Itera sobre cada fila del resultado como un array asociativo
			$resultado[] = $row; // Agrega la fila actual al array $resultado
		}
		$json = json_encode($resultado, JSON_PRETTY_PRINT); // Convierte el array $resultado a formato JSON con formato legible (con sangrías)
		return $json; // Devuelve el JSON resultante
	}
}

?>
