<?php
	
	$peticion = "
            SELECT 
               *
               FROM clavesapi
               WHERE clave = '".$_POST['clave']."'
        ";
        $resultado = mysqli_query($mysqli, $peticion);
        if ($fila = mysqli_fetch_assoc($resultado)) {
        	echo "Acceso correcto, vamos con la inserción";
        }else{
        	die("Error de acceso");
        }
		 if($_SERVER['SERVER_ADDR'] == "::1"){
		 
		 }else{
		 	die("Error de IP no admitida");
		 }
			 	// Aqui ponemos la logica de insertar cliente
			 		if(isset($_POST['nombre']) && isset($_POST['apellidos']) && isset($_POST['email']) && isset($_POST['direccion']) && isset($_POST['poblacion']) && isset($_POST['cp']) && isset($_POST['pais']) && isset($_POST['texto'])){
			 			$peticion = "
				      INSERT INTO 
				      clientes 
				      (nombre,apellidos,email,direccion,poblacion,cp,pais,texto) 
				      VALUES 
				      (
						   '".$_POST['nombre']."',
						   '".$_POST['apellidos']."',
						   '".$_POST['email']."',
						   '".$_POST['direccion']."',
						   '".$_POST['poblacion']."',
						   '".$_POST['cp']."',
						   '".$_POST['pais']."',
						   '".$_POST['texto']."'
				      );
				  ";
				  $resultado = mysqli_query($mysqli, $peticion);
			 		}else{
			 			echo "error en la peticion";
			 		}
?>
