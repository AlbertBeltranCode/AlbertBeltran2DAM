<?php
header('Content-Type: application/json');

// Database credentials
$host = 'localhost';
$dbname = 'crimson';
$username = 'crimson'; // Usuario predeterminado en XAMPP
$password = 'crimson';     // Contraseña vacía en XAMPP

// Connect to the database using PDO
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit;
}

// Verify if parameters are available
$id = isset($_GET['id']) ? intval($_GET['id']) : 0;

if ($id) {
    try {
        // Query to fetch order history for a specific customer
        $stmt = $pdo->prepare("
            SELECT 
                p.fecha AS FechaPedido,
                prod.nombre AS Producto,
                l.cantidad AS Cantidad
            FROM lineaspedido l
            INNER JOIN pedidos p ON l.pedidos_fecha = p.Identificador
            INNER JOIN productos prod ON l.productos_nombre = prod.Identificador
            WHERE p.clientes_nombre = :id
            ORDER BY p.fecha DESC
        ");
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->execute();

        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

        if ($result) {
            // Return data as JSON
            echo json_encode($result);
        } else {
            echo json_encode(['error' => 'No orders found for this customer']);
        }
    } catch (PDOException $e) {
        echo json_encode(['error' => 'Query failed: ' . $e->getMessage()]);
    }
} else {
    echo json_encode(['error' => 'Invalid customer ID']);
}
?>


