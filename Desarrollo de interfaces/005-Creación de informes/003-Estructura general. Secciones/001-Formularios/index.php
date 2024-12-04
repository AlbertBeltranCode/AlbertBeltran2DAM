<?php
$jsonFile = 'estructura.json';

$jsonContent = file_get_contents($jsonFile);

$dataArray = json_decode($jsonContent, true);

forEach($dataArray as $clave=>$valor){
	echo '
	<input 
		type="'.$valor['tipo'].'" 
		name="'.$valor['nombre'].'" 
		placeholder="'.$valor['nombre'].'"
	>';
}

?>

