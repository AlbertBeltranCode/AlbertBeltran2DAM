<?php
    // Verificar que se haya recibido el parámetro "entrada"
    if (!isset($_GET['entrada'])) {
        echo json_encode([]);
        exit();
    }

    // Crear instancia de SQLite3 y aplicar ajustes para manejo de bloqueos
    $db = new SQLite3('database.db');
    $db->busyTimeout(5000); // Espera hasta 5000 ms para liberar bloqueos
    $db->exec("PRAGMA journal_mode = WAL;"); // Activa el modo WAL para mejorar la concurrencia

    // Escapar la entrada para evitar inyección SQL
    $entrada = $db->escapeString($_GET['entrada']);

    // Ejecutar la consulta
    $query = "SELECT * FROM palabras WHERE previas = '".$entrada."'";
    $result = $db->query($query);

    $arreglo = [];
    while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
         $arreglo[] = $row['siguiente'];
    }
    
    echo json_encode($arreglo);
?>
