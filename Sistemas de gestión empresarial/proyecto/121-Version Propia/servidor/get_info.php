<?php
header('Content-Type: application/json');

// Verifica si los parámetros están disponibles
$tabla = isset($_GET['tabla']) ? $_GET['tabla'] : '';
$id = isset($_GET['id']) ? $_GET['id'] : '';
$nombre = isset($_GET['nombre']) ? (string)$_GET['nombre'] : '';
error_log("Nombre recibido: " . $nombre);

error_log("Tabla: " . $tabla);
error_log("ID: " . $id);
error_log("Nombre: " . $nombre); // Verifica el valor de nombre

// Aquí iría tu lógica para obtener los datos
// Simulamos que los datos son obtenidos correctamente
if ($tabla && $id) {
    // Asigna cada columna como un campo separado
    $response = [
        'Nombre' => (string)$nombre,  // Asegura que $nombre es una cadena
        'Email' => 'juan@example.com',
        'Teléfono' => '123456789',
        'Dirección' => 'Calle Ficticia 123',
        'tabla' => $tabla,
        'id' => $id
    ];

    echo json_encode($response); // Devuelve los datos en formato JSON
} else {
    // En caso de error, devolver un mensaje de error en JSON
    echo json_encode(['error' => 'Datos no encontrados']);
}
?>
