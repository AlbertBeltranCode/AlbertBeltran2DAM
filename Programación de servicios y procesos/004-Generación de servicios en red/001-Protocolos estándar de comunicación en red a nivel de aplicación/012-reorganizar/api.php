<?php
include "inc/error.php";

$mysqli = mysqli_connect("localhost", "crimson", "crimson", "crimson");

header('Content-Type: application/json');  // Aseguramos que la respuesta sea JSON

// Asegúrate de que siempre devuelvas JSON
if (isset($_GET['o'])) {
    switch ($_GET['o']) {
        case "clientes":
            include "inc/damepedidos.php";  // El archivo que maneja la respuesta de clientes
            break;
        case "insertarCliente":
            include "inc/insertarcliente.php";  // El archivo para insertar cliente
            break;
        default:
            echo json_encode(['error' => 'Acción no válida']);  // Devuelve error como JSON
            break;
    }
} else {
    echo json_encode(['error' => 'El parámetro "o" no se ha recibido']);  // Devuelve el error si no hay parámetro 'o'
}
?>
