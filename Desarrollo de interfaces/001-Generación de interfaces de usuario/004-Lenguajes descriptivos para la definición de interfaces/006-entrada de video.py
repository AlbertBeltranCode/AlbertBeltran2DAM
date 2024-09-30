import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()

marco = tk.Frame(ventana)  # Contenedor para los widgets
marco.pack(padx=10, pady=10)

def seleccionaEntrada():
    ruta = filedialog.askopenfilename()  # Abre diálogo para seleccionar un archivo

# Botón para seleccionar el archivo de video
selector_video_entrada = tk.Button(
    marco,
    text="Selecciona el video de entrada",  # Texto en el botón
    command=seleccionaEntrada  # Llama a la función cuando se hace clic
)

selector_video_entrada.pack(padx=50, pady=50)  # Empaqueta el botón dentro del marco con márgenes

ventana.mainloop()  # Inicia la ventana principal