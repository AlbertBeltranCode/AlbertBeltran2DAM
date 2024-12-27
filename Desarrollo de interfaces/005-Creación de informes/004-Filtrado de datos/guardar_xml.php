<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener los datos del formulario
    $dni = $_POST['dni'];
    $iban = $_POST['iban'];
    $cp = $_POST['cp'];
    $email = $_POST['email'];

    // Crear un objeto SimpleXMLElement
    $xml = new SimpleXMLElement('<formularios/>');

    // Agregar un nuevo formulario al XML
    $formulario = $xml->addChild('formulario');
    $formulario->addChild('dni', $dni);
    $formulario->addChild('iban', $iban);
    $formulario->addChild('cp', $cp);
    $formulario->addChild('email', $email);

    // Guardar el archivo XML
    $xml->asXML('datos_formulario.xml');

    // Confirmación de envío
    echo "Los datos se han guardado correctamente.";
}
?>
