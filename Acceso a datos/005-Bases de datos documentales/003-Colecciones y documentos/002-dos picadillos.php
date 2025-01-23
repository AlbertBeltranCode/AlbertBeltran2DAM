<?php
	
	$contrasena = "Albert";
	
	$picadillo = md5($contrasena);
	$picadillo2 = md5($contrasena);
	
	echo $picadillo;
	echo "<br>";
	echo $picadillo2;
?>
