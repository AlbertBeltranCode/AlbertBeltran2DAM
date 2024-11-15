<?php
// Nombre del archivo que contiene las tareas
$file = "tareas.txt";

// Lee el contenido del archivo y lo convierte en un array,
// donde cada elemento del array es una línea del archivo
$lines = file($file);

// Guarda la primera línea del archivo en la variable $tarea
$tarea = $lines[0];

// Muestra (imprime) la primera línea del archivo (la tarea asignada)
echo $lines[0];

// Elimina la primera línea del array (la que ya se mostró)
array_shift($lines);

// Guarda el contenido restante del array en el archivo,
// sobrescribiendo el archivo original sin la primera línea
// 'implode' convierte el array de líneas en un string
file_put_contents($file, implode("", $lines));

// Abre el archivo "asignaciones.txt" en modo de añadir (append)
// Si el archivo no existe, lo crea automáticamente
$myfile = fopen("asignaciones.txt", "a");

// Prepara el texto a escribir en el archivo "asignaciones.txt"
// Incluye el nombre del usuario pasado por la URL y la tarea asignada
$txt = "Al usuario " . $_GET["usuario"] . " le ha tocado la tarea: " . $tarea . "\n";

// Escribe el texto en el archivo "asignaciones.txt"
fwrite($myfile, $txt);

// Cierra el archivo para asegurar que los cambios se guarden
fclose($myfile);
?>
