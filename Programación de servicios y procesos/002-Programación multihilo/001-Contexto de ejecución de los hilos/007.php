<?php
// Define el nombre del archivo que contiene las tareas
$file = "tareas.txt";

// Lee el contenido del archivo "tareas.txt" y lo convierte en un array,
// donde cada elemento del array es una línea del archivo
$lines = file($file);

// Asigna la primera línea del archivo a la variable $tarea
$tarea = $lines[0];

// Muestra (imprime) la primera línea del archivo (la tarea asignada)
echo $lines[0];

// Elimina la primera línea del array, ya que esa tarea ha sido asignada
array_shift($lines);

// Guarda el contenido restante del array en el archivo "tareas.txt",
// sobrescribiendo el archivo original sin la primera línea
// 'implode' convierte el array de líneas en un solo string, sin modificarlas
file_put_contents($file, implode("", $lines));

// Abre el archivo "asignaciones.txt" en modo de añadir (append)
// Si el archivo no existe, lo crea automáticamente
$myfile = fopen("asignaciones.txt", "a");

// Prepara el texto a escribir en el archivo "asignaciones.txt",
// donde se incluye el nombre del usuario pasado por la URL y la tarea asignada
$txt = "Al usuario " . $_GET["usuario"] . " le ha tocado la tarea: " . $tarea . "\n";

// Escribe el texto en el archivo "asignaciones.txt"
fwrite($myfile, $txt);

// Cierra el archivo "asignaciones.txt" para asegurarse de que los cambios se guarden
fclose($myfile);
?>
