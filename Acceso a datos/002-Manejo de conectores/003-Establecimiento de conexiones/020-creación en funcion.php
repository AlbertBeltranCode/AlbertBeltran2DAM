<?php
function selecciona($tabla) // Define una función llamada 'selecciona' que toma un parámetro '$tabla'
{
	$mysqli = mysqli_connect("localhost", "accesoadatos", "accesoadatos", "accesoadatos"); // Establece la conexión a la base de datos MySQL con las credenciales proporcionadas
	$query = "SELECT * FROM " . $tabla . ";"; // Construye la consulta SQL para seleccionar todos los registros de la tabla especificada
	$result = mysqli_query($mysqli, $query); // Ejecuta la consulta y almacena el resultado en la variable $result
	$resultado = []; // Inicializa un array vacío para almacenar los resultados
	while ($row = mysqli_fetch_assoc($result)) { // Itera sobre cada fila del resultado como un array asociativo
		$resultado[] = $row; // Agrega la fila actual al array $resultado
	}
	$json = json_encode($resultado, JSON_PRETTY_PRINT); // Convierte el array $resultado a formato JSON con formato legible (con sangrías)
	return $json; // Devuelve el JSON resultante
}

echo selecciona("clientes"); // Llama a la función 'selecciona' con la tabla 'clientes' y imprime el resultado JSON
?>
