<?php

	$coleccion = ['DELETE', 'DROP', 'TRUNCATE'];
	$entrada = $_POST['entrada'];

	if (array_filter($coleccion, fn($elemento) => strpos($entrada, $elemento) !== false)) {
		 echo "positivo";
	} else {
		 echo "negativo";
	}

?>
