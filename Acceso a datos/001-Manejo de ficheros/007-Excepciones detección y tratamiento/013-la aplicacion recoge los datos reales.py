import json  # Importamos la librería json para guardar datos en formato JSON.
import os  # Permite realizar operaciones con el sistema de archivos del sistema operativo.
import errno  # Gestiona errores específicos del sistema operativo.
import tkinter as tk  # Librería para crear interfaces gráficas de usuario.

# Definición de la clase Cliente.
class Cliente:
    # El constructor (__init__) toma varios parámetros para inicializar las propiedades de un cliente.
    def __init__(self, idcliente, nuevonombre, nuevosapellidos, listapersonal, listaprofesional):
        self.idcliente = idcliente  # Almacena el ID del cliente.
        self.nombre = nuevonombre  # Almacena el nombre del cliente.
        self.apellidos = nuevosapellidos  # Almacena los apellidos del cliente.
        self.emails = {  # Almacena los emails en un diccionario con dos tipos: personal y profesional.
            "personal": listapersonal,
            "profesional": listaprofesional
        }

    # Convierte los atributos del cliente a un diccionario.
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "emails": self.emails
        }

# Definición de la carpeta donde se guardará la base de datos.
carpeta = "basededatos"
continuas = True  # Variable que determina si se puede continuar con las operaciones.
clientes = []  # Lista para almacenar objetos Cliente.

# Intento de crear la carpeta "basededatos" si no existe.
try:
    os.makedirs(carpeta)
except OSError as e:
    # Si la carpeta ya existe, se informa al usuario.
    if e.errno == errno.EEXIST:
        print(f"La carpeta ya existe.")
    # Si hay un error de permisos, se detiene el guardado.
    elif e.errno == errno.EACCES:
        continuas = False
        print("Error de permisos en la carpeta - no puedo guardar")
    # Manejo de otros errores inesperados.
    else:
        print(f"Unexpected error: {e}")

# Función para guardar un cliente en la lista.
def guardaCliente():
    global clientes  # Utilizamos la lista de clientes global.
    # Agrega un nuevo cliente a la lista con los datos recogidos de la interfaz.
    clientes.append(
        Cliente(
            idcliente.get(),  # Obtiene el ID del cliente de la interfaz.
            nombre.get(),  # Obtiene el nombre del cliente.
            apellidos.get(),  # Obtiene los apellidos del cliente.
            personal.get(),  # Obtiene el email personal.
            profesional.get()  # Obtiene el email profesional.
        )
    )

# Función para guardar todos los clientes en la base de datos como archivos JSON.
def guardaDB():
    for cliente in clientes:  # Recorre cada cliente en la lista.
        archivo = open(carpeta + "/" + cliente.idcliente + ".json", 'w')  # Crea un archivo con el ID del cliente como nombre.
        json.dump(cliente.to_dict(), archivo, indent=4)  # Escribe los datos del cliente en formato JSON.
        archivo.close()  # Cierra el archivo tras escribir.

# Creación de la ventana principal con tkinter.
ventana = tk.Tk()

# Creación de un marco dentro de la ventana con márgenes para organizar los widgets.
marco = tk.Frame(ventana, padx=20, pady=20)
marco.pack(padx=20, pady=20)  # Empaqueta el marco en la ventana principal.

# Definición de variables de tkinter para enlazar con los campos de entrada de datos.
nombre = tk.StringVar()  # Variable para almacenar el nombre del cliente.
apellidos = tk.StringVar()  # Variable para los apellidos.
idcliente = tk.StringVar()  # Variable para el ID del cliente.
personal = tk.StringVar()  # Variable para el email personal.
profesional = tk.StringVar()  # Variable para el email profesional.

# Añadimos etiquetas y campos de entrada para capturar datos de cliente.
tk.Label(marco, text="Id de cliente").pack(padx=10, pady=10)
tk.Entry(marco, textvariable=idcliente).pack(padx=10, pady=10)

tk.Label(marco, text="Nombre").pack(padx=10, pady=10)
tk.Entry(marco, textvariable=nombre).pack(padx=10, pady=10)

tk.Label(marco, text="Apellidos").pack(padx=10, pady=10)
tk.Entry(marco, textvariable=apellidos).pack(padx=10, pady=10)

tk.Label(marco, text="Email personal").pack(padx=10, pady=10)
tk.Entry(marco, textvariable=personal).pack(padx=10, pady=10)

tk.Label(marco, text="Email profesional").pack(padx=10, pady=10)
tk.Entry(marco, textvariable=profesional).pack(padx=10, pady=10)

# Botón para guardar un cliente. Llama a la función guardaCliente cuando se presiona.
tk.Button(marco, text="Guardamos este cliente", command=guardaCliente).pack(padx=10, pady=10)

# Botón para guardar todos los clientes en la base de datos. Llama a guardaDB.
tk.Button(marco, text="Guardamos todos los clientes a base de datos", command=guardaDB).pack(padx=10, pady=10)

# Inicia el bucle principal de la ventana (espera interacción del usuario).
ventana.mainloop()




        


