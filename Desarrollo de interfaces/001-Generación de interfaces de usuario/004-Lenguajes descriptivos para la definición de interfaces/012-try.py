import tkinter as tk
from tkinter import filedialog
import subprocess
import os

ventana = tk.Tk()  # Crear la ventana principal

marco = tk.Frame(ventana)  # Marco para contener los widgets
marco.pack(padx=10, pady=10)  # Empaquetar el marco con márgenes

anchura = tk.StringVar()  # Variable que almacena la anchura
altura = tk.StringVar()  # Variable que almacena la altura

# Variables para las rutas de los archivos de entrada y salida
salida = None
entrada = None

def procesar():
    global entrada, salida
    # Verificar si las rutas de entrada y salida no están vacías
    if not entrada or not salida:
        print("Por favor, selecciona los archivos de entrada y salida.")
        return

    # Normalizar las rutas de archivo para evitar problemas
    entrada = os.path.normpath(entrada)
    salida = os.path.normpath(salida)

    # Asegurarse de que las rutas están entre comillas simples
    command = ['ffmpeg', '-i', entrada, '-vf', f'scale={anchura.get()}:{altura.get()}', salida]

    try:
        # Ejecutar el comando FFmpeg con argumentos separados
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Mostrar la salida y posibles errores en la consola
        print("FFmpeg output:", result.stdout)
        print("FFmpeg error (if any):", result.stderr)
        
        if result.returncode == 0:
            print("Video procesado con éxito")
        else:
            print("Error en el procesamiento del video")

    except Exception as e:
        print("Error ejecutando el comando:", e)

def seleccionaEntrada():
    global entrada
    entrada = filedialog.askopenfilename()

def seleccionaSalida():
    global salida
    salida = filedialog.asksaveasfilename()

# Botón para seleccionar el video de entrada
selector_video_entrada = tk.Button(
    marco,
    text="Selecciona el video de entrada",  # Texto del botón
    command=seleccionaEntrada  # Llama a seleccionaEntrada al hacer clic
)
selector_video_entrada.pack(padx=50, pady=20)  # Empaquetar con márgenes

# Etiqueta para la anchura
tk.Label(
    marco,
    text="Indica la anchura de salida que quieres"
).pack(padx=50, pady=20)

# Campo de entrada para la anchura
tk.Entry(
    marco,
    textvariable=anchura  # Vincula la entrada a la variable 'anchura'
).pack(padx=50, pady=20)

# Etiqueta para la altura
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
selector_video_salida.pack(padx=50, pady=20)

# Botón para iniciar el proceso
tk.Button(
    marco,
    text="Comenzamos",  # Texto del botón
    command=procesar  # Llama a procesar al hacer clic
).pack(padx=50, pady=20)

ventana.mainloop()  # Inicia el bucle principal de la ventana
