<?php

	$mysqli = mysqli_connect("localhost", "crimson", "crimson", "crimson"); // Establece una conexión a la base de datos MySQL

	$query = "CALL SeleccionaClientesBueno('car');"; // Define una consulta SQL que llama a un procedimiento almacenado llamado SeleccionaClientesBueno() con el parámetro 'car'

	$result = mysqli_query($mysqli, $query); // Ejecuta la consulta en la base de datos y almacena el resultado en $result

	while ($row = mysqli_fetch_row($result)) { // Recorre cada fila del resultado de la consulta
		  var_dump($row); // Muestra el contenido de la fila actual
	}

?>