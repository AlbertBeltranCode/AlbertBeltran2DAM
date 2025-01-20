<?php
// Permitir acceso desde cualquier origen
header("Access-Control-Allow-Origin: *");

// Especificar los métodos HTTP permitidos
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");

// Permitir encabezados específicos en la solicitud
header("Access-Control-Allow-Headers: Content-Type, Authorization");

// Manejar solicitudes preflight (OPTIONS)
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    // Responder con un estado exitoso para solicitudes preflight
    http_response_code(200);
    exit;
}

// Tu lógica PHP aqu
?>

<?php

ini_set('display_errors', 1);																								// Activo errores
	ini_set('display_startup_errors', 1);																				// Activo errores de inicio
	error_reporting(E_ALL);	
	
$mysqli = mysqli_connect("localhost", "crimson", "crimson", "crimson");

$peticion = "SELECT * FROM productos";

$resultado = mysqli_query($mysqli, $peticion);

$json = [];
while ($fila = mysqli_fetch_assoc($resultado)) {
    $json[] = $fila;
}
$json = json_encode($json, JSON_PRETTY_PRINT);
echo $json;

?>
