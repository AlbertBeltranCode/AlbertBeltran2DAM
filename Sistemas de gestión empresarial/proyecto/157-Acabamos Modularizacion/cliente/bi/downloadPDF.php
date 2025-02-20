<?php
// Asegúrate de tener instalada la librería FPDF y que la ruta sea correcta
require('fpdf/fpdf.php');

// Detalles de conexión (mismos que en ejecuta.php)
$host = "localhost";
$username = "crimson";
$password = "crimson";
$database = "crimson";

// Crear conexión
$conn = new mysqli($host, $username, $password, $database);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Validar y decodificar la consulta SQL enviada
if (!isset($_POST['sql'])) {
    die("No se proporcionó ninguna consulta SQL.");
}
$sql = base64_decode($_POST['sql']);
$result = $conn->query($sql);
if (!$result) {
    die("La consulta falló: " . $conn->error);
}

// Crear una nueva instancia de FPDF y configurar el PDF
$pdf = new FPDF();
$pdf->AddPage();
$pdf->SetFont('Arial','B',12);

// Obtener y escribir los encabezados de la tabla
$fields = $result->fetch_fields();
$columnWidths = [];
foreach ($fields as $field) {
    // Definir un ancho fijo o calcularlo dinámicamente
    $columnWidths[] = 40;
    $pdf->Cell(40,10, $field->name, 1);
}
$pdf->Ln();

// Escribir las filas de datos
$pdf->SetFont('Arial','',12);
while ($row = $result->fetch_assoc()) {
    foreach ($row as $value) {
        $pdf->Cell(40,10, $value, 1);
    }
    $pdf->Ln();
}

// Forzar la descarga del archivo PDF
$pdf->Output('D', 'data.pdf');
$conn->close();
?>
