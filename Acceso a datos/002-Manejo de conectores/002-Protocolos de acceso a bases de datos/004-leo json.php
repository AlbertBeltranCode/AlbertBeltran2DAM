<?php

// Establece una conexión a la base de datos MySQL
($enlace = mysqli_connect("localhost", "accesoadatos", "accesoadatos", "accesoadatos")) or die("error");

// Lee el contenido del archivo "004-modelodedatos.json" y lo almacena en la variable $json
$json = file_get_contents("004-modelodedatos.json");

// Convierte el contenido JSON en un array asociativo PHP
$datos = json_decode($json, true);

// Muestra el contenido del array $datos utilizando la función var_dump
var_dump($datos);
?>


