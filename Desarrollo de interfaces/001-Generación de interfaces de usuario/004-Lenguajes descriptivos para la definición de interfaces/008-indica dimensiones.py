import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()

marco = tk.Frame(ventana) # Contenedor para los widgets
marco.pack(padx=10,pady=10) 

def seleccionaEntrada(): 
    ruta = filedialog.askopenfilename() # Abre diálogo para seleccionar un archivo
    print("La ruta de tu video es:",ruta) # Mostramos la ruta del video de entrada

# Botón para seleccionar el archivo de video
selector_video_entrada = tk.Button(
    marco,
    text="Selecciona el video de entrada", # Texto en el botón
    command=seleccionaEntrada # Llama a la función cuando se hace clic
    )

selector_video_entrada.pack(padx=50,pady=50); # Empaqueta el botón dentro del marco con márgenes

tk.Label( #Definimos las dimensiones de anchura de salida que queremos que tenga el video
    marco,
    text="Indica la anchura de salida que quieres" 
    ).pack(padx=50,pady=20);

ventana.mainloop() # Inicia la ventana principal

