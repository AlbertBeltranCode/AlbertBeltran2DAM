<?php
// Nombre del archivo que contiene las tareas
$file = "tareas.txt";

// Lee el contenido del archivo y lo convierte en un array,
// donde cada elemento del array es una línea del archivo
$lines = file($file);

// Muestra (imprime) la primera línea del archivo
echo $lines[0];

// Elimina la primera línea del array (la que ya se mostró)
array_shift($lines);

// Guarda el contenido restante del array en el archivo,
// sobrescribiendo el archivo original sin la primera línea.
// 'implode' convierte el array de líneas en un string, usando '' como separador
file_put_contents($file, implode("", $lines));

?>
