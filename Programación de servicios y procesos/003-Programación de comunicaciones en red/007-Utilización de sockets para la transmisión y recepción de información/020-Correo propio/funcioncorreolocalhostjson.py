import json
import os
from datetime import datetime

# Definir la ruta para almacenar los correos en formato JSON
CORREOS_PATH = "correos.json"

# Inicializar el archivo de correos si no existe
def inicializar_storage():
    if not os.path.exists(CORREOS_PATH):
        with open(CORREOS_PATH, "w") as f:
            json.dump([], f)

# Guardar correos en el archivo JSON
def guardar_correo(correo):
    with open(CORREOS_PATH, "r") as f:
        correos = json.load(f)
    correos.append(correo)
    with open(CORREOS_PATH, "w") as f:
        json.dump(correos, f, indent=4)

# Leer todos los correos del archivo JSON
def obtener_correos():
    with open(CORREOS_PATH, "r") as f:
        return json.load(f)

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

# Inicializar el almacenamiento al importar este módulo
inicializar_storage()

