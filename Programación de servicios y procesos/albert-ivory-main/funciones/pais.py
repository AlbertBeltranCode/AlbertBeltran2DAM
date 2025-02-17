import json
import os
import ipaddress

def save_blocked_ips_to_json(ips, file_path):
    """
    Guarda las IPs bloqueadas en un archivo JSON.

    :param ips: Lista de IPs bloqueadas
    :param file_path: Ruta donde se guardará el archivo JSON
    """
    try:
        with open(file_path, 'w') as json_file:
            json.dump({"blocked_ips": list(ips)}, json_file, indent=4)
        print(f"IPs bloqueadas guardadas en {file_path}")
    except Exception as e:
        print(f"Error al guardar las IPs bloqueadas en JSON: {e}")

def main():
    # Ruta al archivo de registro de Apache
    log_file_path = "/var/log/apache2/jocarsa-oldlace-access.log"

    # Ruta al archivo JSON donde se guardarán las IPs bloqueadas
    json_file_path = os.path.join(os.path.dirname(__file__), 'ips_bloqueadas.json')

    # Leer el archivo de registro
    try:
        with open(log_file_path, 'r') as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo {log_file_path} no existe.")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # Recopilar las IPs basadas en la lógica del país (esto es un marcador de posición)
    blacklisted_ips = set()
    for linea in lineas:
        try:
            # Suponiendo que el formato del registro es similar al formato combinado de registros:
            # IP - - [fecha] "solicitud" estado tamaño "referer" "user-agent"
            partes = linea.split('"')
            if len(partes) >= 6:
                pais = partes[5].strip()
                if pais == "BlockedCountry":  # Reemplazar con la lógica real del país
                    ip = linea.split()[0]
                    ipaddress.IPv4Address(ip)
                    blacklisted_ips.add(ip)
        except ipaddress.AddressValueError:
            continue
        except IndexError:
            continue

    # Ordenar las IPs bloqueadas (opcional: por frecuencia u otro criterio)
    ordenado_blacklisted = sorted(blacklisted_ips)

    # Imprimir la lista ordenada de IPs bloqueadas
    print("IPs bloqueadas por país:")
    for ip in ordenado_blacklisted:
        print(ip)

    # Guardar las IPs bloqueadas en un archivo JSON
    if ordenado_blacklisted:
        save_blocked_ips_to_json(ordenado_blacklisted, json_file_path)
    else:
        print("No hay IPs bloqueadas por país para guardar.")
