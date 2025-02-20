<?php
// Detalles de conexión (igual que en ejecuta.php)
$host = "localhost";
$username = "crimson";
$password = "crimson";
$database = "crimson";

// Crear conexión
$conn = new mysqli($host, $username, $password, $database);

// Verificar conexión
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Verificar que se haya enviado la consulta SQL
if (!isset($_POST['sql'])) {
    die("No se proporcionó ninguna consulta SQL.");
}

// Decodificar la consulta SQL enviada
$sql = base64_decode($_POST['sql']);

// Ejecutar la consulta
$result = $conn->query($sql);
if (!$result) {
    die("La consulta falló: " . $conn->error);
}

// Establecer cabeceras para forzar la descarga del archivo CSV
header('Content-Type: text/csv; charset=utf-8');
header('Content-Disposition: attachment; filename=data.csv');

// Abrir el flujo de salida
$output = fopen('php://output', 'w');

// Obtener los nombres de las columnas y escribir la primera línea del CSV
$fields = $result->fetch_fields();
$headers = array();
foreach ($fields as $field) {
    $headers[] = $field->name;
}
fputcsv($output, $headers);

// Escribir las filas de datos en el CSV
while ($row = $result->fetch_assoc()) {
    fputcsv($output, $row);
}

fclose($output);
$conn->close();
?>
