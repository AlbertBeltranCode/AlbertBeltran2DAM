<?php
ini_set("display_errors", 1); // Habilito la visualización de errores en la ejecución del script
ini_set("display_startup_errors", 1); // Habilito la visualización de errores que ocurren durante el inicio del script
error_reporting(E_ALL); // Configuro el reporte de todos los tipos de errores

include "ConexionDB.php"; // Incluyo el archivo que contiene la definición de la clase conexionDB

$conexion = new conexionDB(); // Creo una nueva instancia de la clase conexionDB para establecer una conexión a la base de datos

echo $conexion->seleccionaTabla("pedidos"); // Llamo al método seleccionaTabla de la instancia de conexionDB para obtener y mostrar los datos de la tabla "pedidos"
?>