<?php
	$coleccion = ['DELETE', 'DROP', 'TRUNCATE'];
	$entradas = $_REQUEST;
	foreach ($entradas as $clave=>$valor) {
		 
		$entrada = $clave;
		if (array_filter($coleccion, fn($elemento) => strpos($entrada, $elemento) !== false)) {
			 die("No permitido");
		} 
		$entrada = $valor;
		if (array_filter($coleccion, fn($elemento) => strpos($entrada, $elemento) !== false)) {
			 die("No permitido");
		} 
		 
	}
	echo "todo ok";
?>
