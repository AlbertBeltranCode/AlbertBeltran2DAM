<?php

$mysqli = mysqli_connect("localhost", "accesoadatos", "accesoadatos", "accesoadatos"); // Establece la conexión a la base de datos MySQL con las credenciales proporcionadas
$query = "SELECT * FROM empleados"; // Define la consulta SQL para seleccionar todos los registros de la tabla 'empleados'
$result = mysqli_query($mysqli, $query); // Ejecuta la consulta y almacena el resultado en la variable $result
while ($row = mysqli_fetch_assoc($result)) { // Itera sobre cada fila del resultado como un array asociativo
    var_dump($row); // Muestra el contenido de la fila actual en formato legible
}

?>