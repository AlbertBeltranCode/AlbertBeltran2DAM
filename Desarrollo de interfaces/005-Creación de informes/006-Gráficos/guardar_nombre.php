<?php
if (isset($_POST['nombre'])) {
    $nombre = $_POST['nombre'];

    // Cargar el archivo XML
    $xml = simplexml_load_file('nombres.xml');

    // Crear un nuevo nodo <nombre> y añadirlo al XML
    $nuevoNombre = $xml->addChild('nombre', $nombre);

    // Guardar el archivo XML con formato legible
    guardarXMLFormateado($xml);
    
    echo "Nombre guardado correctamente";
} else if (isset($_POST['vaciar']) && $_POST['vaciar'] == 'true') {
    // Si se solicita vaciar el archivo XML
    $xml = simplexml_load_file('nombres.xml');
    // Eliminar todos los nodos <nombre>
    foreach ($xml->children() as $child) {
        unset($child[0]);
    }
    // Guardar el archivo XML vacío
    guardarXMLFormateado($xml);
    echo "Archivo XML vaciado";
} else {
    echo "No se ha recibido el nombre";
}

// Función para guardar el XML con formato legible (saltos de línea)
function guardarXMLFormateado($xml) {
    // Convertir el objeto SimpleXML a XML
    $dom = dom_import_simplexml($xml);
    $xmlFormatted = $dom->ownerDocument->saveXML($dom->ownerDocument->documentElement);

    // Añadir saltos de línea para hacerlo más legible
    $xmlFormatted = preg_replace('/(>)(<)(\/*)/', "$1\n$2$3", $xmlFormatted);

    // Guardar el archivo XML con el formato actualizado
    file_put_contents('nombres.xml', $xmlFormatted);
}
?>
