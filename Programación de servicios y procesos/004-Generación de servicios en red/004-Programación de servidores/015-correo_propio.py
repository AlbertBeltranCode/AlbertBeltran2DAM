import psutil
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

interval = 1

print("Empezamos el cálculo de valores normales")

# Función para enviar correos electrónicos
def envio_correo(destinatario, asunto, cuerpo):
    try:
        # Configuración del servidor SMTP
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        remitente = "correoejemplo"
        contraseña = "contraseñaejemplo"

        # Crear el mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = remitente
        mensaje["To"] = destinatario
        mensaje["Subject"] = asunto
        mensaje.attach(MIMEText(cuerpo, "plain"))

        # Conectarse al servidor y enviar el correo
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        servidor.quit()

        print("Correo enviado con éxito a", destinatario)
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Función para calcular el uso de red en un intervalo dado
def get_network_usage(interval):
    initial_net_io = psutil.net_io_counters()
    time.sleep(interval)
    net_io = psutil.net_io_counters()
    subida = (net_io.bytes_sent - initial_net_io.bytes_sent) / interval
    descarga = (net_io.bytes_recv - initial_net_io.bytes_recv) / interval
    return subida, descarga

# Verificar y calcular valores de red
if not os.path.exists("red.txt"):
    total_subida = 0
    total_descarga = 0

    for _ in range(10):
        s, d = get_network_usage(interval)
        total_subida += s
        total_descarga += d

    subida = total_subida / 10
    descarga = total_descarga / 10

    with open("red.txt", 'w') as archivo:
        archivo.write(f"{subida},{descarga}")
else:
    with open("red.txt", 'r') as archivo:
        linea = archivo.readline()

    partido = linea.split(",")
    subida = float(partido[0])
    descarga = float(partido[1])

# Enviar el correo siempre al final del script
envio_correo(
    destinatario="ejemplovideo@gmail.com",
    asunto="Ejecución del Script de Monitoreo",
    cuerpo=f"Subida promedio: {subida:.2f} bytes/s\nDescarga promedio: {descarga:.2f} bytes/s"
)
