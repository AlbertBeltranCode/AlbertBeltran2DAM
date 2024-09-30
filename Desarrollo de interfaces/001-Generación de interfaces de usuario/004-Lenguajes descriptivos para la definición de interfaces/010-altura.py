import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()  # Crear la ventana principal

marco = tk.Frame(ventana)  # Crear un marco que contiene los widgets
marco.pack(padx=10, pady=10)  # Empaquetar el marco con un pequeño margen

anchura = tk.IntVar()  # Variable para la anchura de salida
altura = tk.IntVar()  # Variable para la altura de salida

# Variables para los archivos de entrada y salida
salida = None  
entrada = None

def procesar():
    # Función que se ejecutará al pulsar el botón "Comenzamos"
    print("Vamos a por ello")

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
    command=seleccionaEntrada  # Llama a la función seleccionaEntrada al hacer clic
)

selector_video_entrada.pack(padx=50, pady=20)  # Empaqueta el botón con márgenes

# Etiqueta para pedir la anchura de salida
tk.Label(
    marco,
    text="Indica la anchura de salida que quieres"
).pack(padx=50, pady=20)

# Campo de entrada para indicar la anchura deseada
tk.Entry(
    marco,
    textvariable=anchura  # La anchura introducida se vincula a la variable 'anchura'
).pack(padx=50, pady=20)

# Etiqueta para pedir la altura de salida
tk.Label(
    marco,
    text="Indica la altura de salida que quieres"
).pack(padx=50, pady=20)

# Campo de entrada para indicar la altura deseada
tk.Entry(
    marco,
    textvariable=altura  # La altura introducida se vincula a la variable 'altura'
).pack(padx=50, pady=20)

# Botón para seleccionar el archivo de salida
selector_video_salida = tk.Button(
    marco,
    text="Selecciona el video de salida",  # Texto del botón
    command=seleccionaSalida  # Llama a la función seleccionaSalida al hacer clic
)

selector_video_salida.pack(padx=50, pady=20)  # Empaqueta el botón con márgenes

# Botón para iniciar el proceso
tk.Button(
    marco,
    text="Comenzamos",  # Texto del botón
    command=procesar  # Llama a la función procesar al hacer clic
).pack(padx=50, pady=20)

ventana.mainloop()  # Inicia el bucle principal de la ventana
