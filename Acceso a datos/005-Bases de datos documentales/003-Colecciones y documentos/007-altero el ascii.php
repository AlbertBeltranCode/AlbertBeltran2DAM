<?php

$contrasena = "Albert";

for($i = 0;$i<strlen($contrasena);$i++){
	echo $contrasena[$i]." - ".ord($contrasena[$i])." - ".(ord($contrasena[$i])+5)."<br>";
}

?>

