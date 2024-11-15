<?php

// Abre el archivo "resultados.txt" en modo de añadir (append),
// Si el archivo no existe, lo crea automáticamente
$myfile = fopen("resultados.txt", "a");

// Crea una nueva línea con el resultado recibido a través de la URL (parámetro 'resultado')
// El "\n" al final agrega un salto de línea para separar cada resultado
$txt = $_GET["resultado"] . "\n";

// Escribe la nueva línea con el resultado en el archivo "resultados.txt"
fwrite($myfile, $txt);

// Cierra el archivo "resultados.txt" para asegurarse de que los cambios se guarden
fclose($myfile);

?>
