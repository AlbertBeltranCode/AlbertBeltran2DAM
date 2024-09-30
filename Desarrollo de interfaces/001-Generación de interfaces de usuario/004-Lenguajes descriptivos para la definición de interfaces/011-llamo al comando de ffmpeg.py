import tkinter as tk
from tkinter import filedialog
import subprocess  # Para ejecutar comandos en el sistema

ventana = tk.Tk()  # Crear la ventana principal

marco = tk.Frame(ventana)  # Marco que contiene los widgets
marco.pack(padx=10, pady=10)  # Empaquetar el marco con márgenes

anchura = tk.StringVar()  # Variable para almacenar la anchura que el usuario introduce
altura = tk.StringVar()  # Variable para almacenar la altura que el usuario introduce

# Variables para las rutas de los archivos de entrada y salida
salida = None
entrada = None

def procesar():
    # Función que se ejecuta al presionar "Comenzamos"
    print("Vamos a por ello")
    
    # Comando FFmpeg para redimensionar el video
    command = "ffmpeg -i '" + entrada + "' -vf scale=" + anchura.get() + ":" + altura.get() + " '" + salida + "'"
    print(command)  # Imprimir el comando en consola para ver su estructura

    # Ejecuta el comando usando subprocess y captura la salida
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("Output:", result.stdout)  # Muestra la salida del comando

def seleccionaEntrada():
    # Abre el diálogo para seleccionar el archivo de entrada
    global entrada
    entrada = filedialog.askopenfilename()

def seleccionaSalida():
    # Abre el diálogo para seleccionar la ubicación del archivo de salida
    global salida
    salida = filedialog.asksaveasfilename()

# Botón para seleccionar el video de entrada
selector_video_entrada = tk.Button(
    marco,
    text="Selecciona el video de entrada",  # Texto del botón
    command=seleccionaEntrada  # Llama a seleccionaEntrada al hacer clic
)
selector_video_entrada.pack(padx=50, pady=20)  # Empaqueta el botón con márgenes

# Etiqueta para la anchura del video de salida
tk.Label(
    marco,
    text="Indica la anchura de salida que quieres"
).pack(padx=50, pady=20)

# Campo de entrada para la anchura
tk.Entry(
    marco,
    textvariable=anchura  # Vincula la entrada a la variable 'anchura'
).pack(padx=50, pady=20)

# Etiqueta para la altura del video de salida
tk.Label(
    marco,
    text="Indica la altura de salida que quieres"
).pack(padx=50, pady=20)

# Campo de entrada para la altura
tk.Entry(
    marco,
    textvariable=altura  # Vincula la entrada a la variable 'altura'
).pack(padx=50, pady=20)

# Botón para seleccionar el archivo de salida
selector_video_salida = tk.Button(
    marco,
    text="Selecciona el video de salida",  # Texto del botón
    command=seleccionaSalida  # Llama a seleccionaSalida al hacer clic
)
selector_video_salida.pack(padx=50, pady=20)  # Empaqueta el botón con márgenes

# Botón que inicia el procesamiento al hacer clic
tk.Button(
    marco,
    text="Comenzamos",  # Texto del botón
    command=procesar  # Llama a la función procesar
).pack(padx=50, pady=20)

ventana.mainloop()  # Inicia el bucle principal de la ventana