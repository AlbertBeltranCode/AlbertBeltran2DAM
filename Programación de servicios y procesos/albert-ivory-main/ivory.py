# main.py
from funciones.pais import main as country_block_main
from funciones.user_agent_block import main as user_agent_block_main

def main():
    print("Iniciando el bloqueo de IPs por país...")
    country_block_main()

    print("\nIniciando el bloqueo de IPs por agente de usuario...")
    user_agent_block_main()

    print("\nProceso de bloqueo de IPs completado.")

if __name__ == "__main__":
    main()

