import socket
import threading
import json
import os
import sys
import logging
from datetime import datetime

def load_server_config(config_path='server_config_sample.json'):
    if not os.path.exists(config_path):
        print(f"[ERROR] Server configuration file '{config_path}' not found.")
        sys.exit(1)
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            # Validar campos requeridos
            required_fields = ['host', 'port', 'message_file', 'log_file']
            for field in required_fields:
                if field not in config:
                    raise ValueError(f"Falta '{field}' en la configuración del servidor.")
            return config
    except json.JSONDecodeError as e:
        print(f"[ERROR] Error al analizar '{config_path}': {e}")
        sys.exit(1)
    except ValueError as ve:
        print(f"[ERROR] {ve}")
        sys.exit(1)

def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def log_connection(addr, status):
    logging.info(f"{status} desde {addr[0]}:{addr[1]}")

def handle_client(conn, addr, message_file):
    log_connection(addr, "Conexión")
    print(f"[NUEVA CONEXIÓN] {addr} conectado.")
    with conn:
        try:
            while True:
                data = conn.recv(1024)  # Recibir datos del cliente
                if not data:
                    break  # No hay más datos, el cliente ha cerrado la conexión
                message = data.decode('utf-8')
                print(f"[RECIBIDO] {addr}: {message}")

                # Guardar el mensaje en un archivo de texto
                with open(message_file, 'a') as file:
                    file.write(f"{addr}: {message}\n")

                # Preparar y enviar una respuesta de vuelta al cliente
                response = f"El servidor ha recibido tu mensaje: {message}"
                conn.sendall(response.encode('utf-8'))
        except ConnectionResetError:
            print(f"[DESCONECTANDO] {addr} conexión reiniciada.")
    log_connection(addr, "Desconexión")
    print(f"[DESCONECTADO] {addr} desconectado.")

def start_server():
    # Cargar la configuración del servidor
    config = load_server_config()

    HOST = config['host']
    PORT = config['port']
    MESSAGE_FILE = config['message_file']
    LOG_FILE = config['log_file']

    # Configurar el registro de conexiones
    setup_logging(LOG_FILE)

    # Crear un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Permitir reutilización de la dirección
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Vincular el socket a la dirección y puerto
        try:
            server.bind((HOST, PORT))
        except socket.error as e:
            print(f"[ERROR] No se pudo vincular a {HOST}:{PORT}: {e}")
            sys.exit(1)
        server.listen()
        print(f"[ESCUCHANDO] El servidor está escuchando en {HOST}:{PORT}")
        logging.info(f"Servidor iniciado en {HOST}:{PORT}")

        while True:
            # Esperar una nueva conexión de cliente
            conn, addr = server.accept()
            # Manejar la conexión del cliente en un nuevo hilo
            client_thread = threading.Thread(target=handle_client, args=(conn, addr, MESSAGE_FILE))
            client_thread.start()
            print(f"[CONEXIONES ACTIVAS] {threading.active_count() - 1}")

if __name__ == "__main__":
    print("[EMPEZANDO] El servidor está iniciándose...")
    start_server()
