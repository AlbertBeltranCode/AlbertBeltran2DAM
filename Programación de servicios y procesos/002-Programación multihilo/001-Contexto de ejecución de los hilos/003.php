<?php
// Abre el archivo "usuarios.txt" en modo de añadir (append)
// Si el archivo no existe, lo crea automáticamente
$myfile = fopen("usuarios.txt", "a");

// Obtiene el parámetro 'usuario' de la URL y le añade un salto de línea
$txt = $_GET["usuario"] . "\n";

// Escribe el texto obtenido en el archivo
fwrite($myfile, $txt);

// Cierra el archivo para asegurar que los cambios se guarden
fclose($myfile);
?>
