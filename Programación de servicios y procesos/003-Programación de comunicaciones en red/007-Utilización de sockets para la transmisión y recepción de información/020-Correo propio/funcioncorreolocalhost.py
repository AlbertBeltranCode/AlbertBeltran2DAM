import os
import xml.etree.ElementTree as ET
from datetime import datetime
import xml.dom.minidom

# Definir la ruta para almacenar los correos en formato XML
CORREOS_PATH = "correos.xml"

# Inicializar el archivo XML si no existe
def inicializar_storage():
    if not os.path.exists(CORREOS_PATH):
        root = ET.Element("correos")
        tree = ET.ElementTree(root)
        tree.write(CORREOS_PATH)

# Función para guardar el XML de manera legible con formato y saltos de línea
def guardar_correo(correo):
    tree = ET.parse(CORREOS_PATH)
    root = tree.getroot()

    correo_element = ET.SubElement(root, "correo")
    ET.SubElement(correo_element, "Asunto").text = correo["Asunto"]
    ET.SubElement(correo_element, "De").text = correo["De"]
    ET.SubElement(correo_element, "Para").text = correo["Para"]
    ET.SubElement(correo_element, "Cuerpo").text = correo["Cuerpo"]
    ET.SubElement(correo_element, "Fecha").text = correo["Fecha"]

    # Dar formato al XML con saltos de línea y una buena indentación
    tree_str = ET.tostring(root, encoding="utf-8", method="xml").decode("utf-8")
    reparsed = xml.dom.minidom.parseString(tree_str)
    formatted_xml = reparsed.toprettyxml(indent="  ")

    # Escribir el XML formateado en el archivo
    with open(CORREOS_PATH, "w") as f:
        f.write(formatted_xml)

# Obtener todos los correos desde el archivo XML
def obtener_correos():
    tree = ET.parse(CORREOS_PATH)
    root = tree.getroot()

    correos = []
    for correo_element in root.findall("correo"):
        correo = {
            "Asunto": correo_element.find("Asunto").text,
            "De": correo_element.find("De").text,
            "Para": correo_element.find("Para").text,
            "Cuerpo": correo_element.find("Cuerpo").text,
            "Fecha": correo_element.find("Fecha").text,
        }
        correos.append(correo)
    
    return correos

# Recibir todos los correos
def recibir():
    return obtener_correos()

# Recibir correos por fecha
def recibir_por_fecha(fecha_objetivo):
    correos = obtener_correos()
    for correo in correos:
        if correo["Fecha"].startswith(fecha_objetivo):
            return correo
    return {"mensaje": "Correo no encontrado para la fecha especificada"}

# Enviar un correo (simulación)
def enviar(desde, para, asunto, mensaje):
    correo = {
        "Asunto": asunto,
        "De": desde,
        "Para": para,
        "Cuerpo": mensaje,
        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    guardar_correo(correo)
    return {"mensaje": "Correo enviado correctamente"}

# Inicializar el almacenamiento al importar este módulo
inicializar_storage()
