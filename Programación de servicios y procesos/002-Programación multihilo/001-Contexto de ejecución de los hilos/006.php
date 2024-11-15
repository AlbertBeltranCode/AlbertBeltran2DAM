<?php
// Nombre del archivo que contiene las tareas
$file = "tareas.txt";

// Lee el contenido del archivo "tareas.txt" y lo convierte en un array,
// donde cada elemento es una línea del archivo
$lines = file($file);

// Guarda la primera línea del archivo en la variable $tarea
$tarea = $lines[0];

// Muestra (imprime) la primera línea del archivo (la tarea asignada)
echo $lines[0];

// Elimina la primera línea del array (la que ya se mostró y asignó)
array_shift($lines);

// Guarda el contenido restante del array en el archivo "tareas.txt",
// sobrescribiendo el archivo original sin la primera línea.
// 'implode' convierte el array de líneas en un string
file_put_contents($file, implode("", $lines));

// Abre (o crea si no existe) el archivo "asignaciones.txt" en modo de añadir (append)
$myfile = fopen("asignaciones.txt", "a");

// Prepara el texto a escribir en el archivo "asignaciones.txt",
// incluye el nombre del usuario pasado por la URL y la tarea asignada
$txt = "Al usuario " . $_GET["usuario"] . " le ha tocado la tarea: " . $tarea . "\n";

// Escribe el texto preparado en el archivo "asignaciones.txt"
fwrite($myfile, $txt);

// Cierra el archivo "asignaciones.txt" para asegurar que los cambios se guarden correctamente
fclose($myfile);
?>
