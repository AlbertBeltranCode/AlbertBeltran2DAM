import json  # Importa el módulo json para trabajar con formatos JSON.
import os  # Importa el módulo os para interactuar con el sistema de archivos.
import errno  # Importa el módulo errno para manejar errores relacionados con el sistema operativo.
import tkinter as tk  # Importa tkinter, que es una librería para crear interfaces gráficas en Python.

# Definición de la clase Cliente.
class Cliente:
    def __init__(self):
        # Inicializa un cliente con un ID, nombre, apellidos y dos listas de correos electrónicos.
        self.idcliente = None
        self.nombre = None
        self.apellidos = None
        self.emails = {"personal": [], "profesional": []}  # Diccionario con listas de emails.

    # Convierte los atributos del cliente a un diccionario.
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "emails": self.emails
        }

# Definición de la clase Producto.
class Producto:
    def __init__(self):
        # Inicializa un producto con nombre, precio, peso y dimensiones.
        self.nombre = None
        self.precio = None
        self.peso = None
        self.dimensiones = {"x": None, "y": None, "z": None}  # Diccionario de dimensiones.

# Definición de la carpeta donde se guardará la base de datos.
carpeta = "basededatos"
continuas = True  # Variable para controlar si se continúa ejecutando el programa.

# Intenta crear la carpeta si no existe.
try:
    os.makedirs(carpeta)
except OSError as e:
    # Si la carpeta ya existe, se muestra un mensaje.
    if e.errno == errno.EEXIST:
        print(f"La carpeta ya existe.")
    # Si hay un error de permisos, se detiene la ejecución relacionada con el guardado.
    elif e.errno == errno.EACCES:
        continuas = False
        print("Error de permisos en la carpeta - no puedo guardar")
    # Manejo de otros errores inesperados.
    else:
        print(f"Unexpected error: {e}")

# Creación de la ventana principal de tkinter.
ventana = tk.Tk()

# Creación de un marco dentro de la ventana con padding para organizar los elementos.
marco = tk.Frame(ventana, padx=20, pady=20)
marco.pack(padx=20, pady=20)  # Empaqueta el marco dentro de la ventana principal.

# Añade etiquetas y campos de entrada para capturar datos del cliente.
tk.Label(marco, text="Id de cliente").pack(padx=10, pady=10)
tk.Entry(marco).pack(padx=10, pady=10)

tk.Label(marco, text="Nombre").pack(padx=10, pady=10)
tk.Entry(marco).pack(padx=10, pady=10)

tk.Label(marco, text="Apellidos").pack(padx=10, pady=10)
tk.Entry(marco).pack(padx=10, pady=10)

tk.Label(marco, text="Email personal").pack(padx=10, pady=10)
tk.Entry(marco).pack(padx=10, pady=10)

tk.Label(marco, text="Email profesional").pack(padx=10, pady=10)
tk.Entry(marco).pack(padx=10, pady=10)

# Botón para guardar un cliente, ejecutará la función guardaCliente cuando se presione.
tk.Button(marco, text="Guardamos este cliente", command=guardaCliente).pack(padx=10, pady=10)

# Botón para guardar todos los clientes a la base de datos, ejecutará la función guardaDB cuando se presione.
tk.Button(marco, text="Guardamos todos los clientes a base de datos", command=guardaDB).pack(padx=10, pady=10)

# Inicia el bucle principal de la ventana (se queda esperando a que el usuario interactúe con la interfaz).
ventana.mainloop()



        


