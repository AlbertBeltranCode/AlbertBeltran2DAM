<?php
///////////////////// TAREAS /////////////////////////////////////////////////

// Define el nombre del archivo que contiene las tareas
$file = "tareas.txt";

// Lee el contenido del archivo "tareas.txt" y lo convierte en un array,
// donde cada elemento del array es una línea del archivo
$lines = file($file);

// Guarda la primera línea del archivo (la primera tarea) en la variable $tarea
$tarea = $lines[0];

// Muestra la primera tarea en pantalla (esto es enviado a la parte del cliente)
echo $lines[0];

// Elimina la primera línea del array, ya que esa tarea ya ha sido asignada
array_shift($lines);

// Guarda el contenido restante del array en el archivo "tareas.txt",
// sobrescribiendo el archivo original sin la primera línea (ya asignada)
file_put_contents($file, implode("", $lines));

///////////////////// ASIGNACIONES /////////////////////////////////////////////////

// Abre el archivo "asignaciones.txt" en modo de añadir (append),
// Si el archivo no existe, lo crea automáticamente
$myfile = fopen("asignaciones.txt", "a");

// Prepara el texto a escribir en el archivo "asignaciones.txt",
// incluye el nombre del usuario pasado como parámetro en la URL y la tarea asignada
$txt = "Al usuario " . $_GET["usuario"] . " le ha tocado la tarea: " . $tarea . "\n";

// Escribe el texto en el archivo "asignaciones.txt"
fwrite($myfile, $txt);

// Cierra el archivo "asignaciones.txt" para asegurarse de que los cambios se guarden
fclose($myfile);

?>
