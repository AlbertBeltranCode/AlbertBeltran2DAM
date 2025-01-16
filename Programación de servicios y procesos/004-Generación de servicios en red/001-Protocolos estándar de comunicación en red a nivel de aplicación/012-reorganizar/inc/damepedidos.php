<?php
// Conexión a la base de datos
$mysqli = mysqli_connect("localhost", "crimson", "crimson", "crimson");

// Verifica si la conexión fue exitosa
if (mysqli_connect_errno()) {
    echo "Fallo en la conexión a MySQL: " . mysqli_connect_error();
    exit();
}

$peticion = "
    SELECT 
        clientes.nombre AS nombre,
        clientes.apellidos AS apellidos,
        pedidos.fecha AS fecha_pedido,
        lineaspedido.productos_nombre AS producto,
        lineaspedido.cantidad AS cantidad
    FROM clientes
    LEFT JOIN pedidos ON clientes.Identificador = pedidos.clientes_nombre
    LEFT JOIN lineaspedido ON pedidos.Identificador = lineaspedido.pedidos_fecha
";

$resultado = mysqli_query($mysqli, $peticion);

$datos = [];
while ($fila = mysqli_fetch_assoc($resultado)) {
    $cliente_key = $fila['nombre'] . " " . $fila['apellidos'];
    if (!isset($datos[$cliente_key])) {
        $datos[$cliente_key] = [
            "cliente" => [
                "nombre" => $fila['nombre'],
                "apellidos" => $fila['apellidos']
            ],
            "pedidos" => []
        ];
    }

    if ($fila['fecha_pedido']) {
        $pedido_key = $fila['fecha_pedido'];
        if (!isset($datos[$cliente_key]["pedidos"][$pedido_key])) {
            $datos[$cliente_key]["pedidos"][$pedido_key] = [
                "fecha" => $fila['fecha_pedido'],
                "lineaspedido" => []
            ];
        }

        if ($fila['producto'] && $fila['cantidad']) {
            $datos[$cliente_key]["pedidos"][$pedido_key]["lineaspedido"][] = [
                "producto" => $fila['producto'],
                "cantidad" => $fila['cantidad']
            ];
        }
    }
}

echo "<table border='1'>";
echo "<tr><th>Nombre</th><th>Apellidos</th><th>Fecha Pedido</th><th>Producto</th><th>Cantidad</th></tr>";

foreach ($datos as $cliente) {
    foreach ($cliente['pedidos'] as $pedido) {
        foreach ($pedido['lineaspedido'] as $linea) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($cliente['cliente']['nombre']) . "</td>";
            echo "<td>" . htmlspecialchars($cliente['cliente']['apellidos']) . "</td>";
            echo "<td>" . htmlspecialchars($pedido['fecha']) . "</td>";
            echo "<td>" . htmlspecialchars($linea['producto']) . "</td>";
            echo "<td>" . htmlspecialchars($linea['cantidad']) . "</td>";
            echo "</tr>";
        }
    }
}

echo "</table>";
?>
