import os
import re
import threading
from tkinter import Tk, StringVar, filedialog, END
from tkinter import PhotoImage
from ttkbootstrap import ttk, Style
from ttkbootstrap.constants import *
from PIL import Image, ImageTk  # Importa Pillow para cargar la imagen

def filtrar_directorios(dirs):
    """
    Filtra y elimina los directorios que comienzan con un punto.

    Args:
        dirs (list): Lista de nombres de directorios.
    """
    # Modifica la lista en su lugar para excluir directorios que comienzan con '.'
    dirs[:] = [d for d in dirs if not d.startswith('.')]

def listar_estructura_markdown(ruta, archivo_salida):
    """
    Genera la estructura del directorio en formato Markdown con listas desordenadas,
    excluyendo directorios ocultos.

    Args:
        ruta (str): Ruta de la carpeta a analizar.
        archivo_salida (str): Nombre del archivo Markdown de salida.
    """
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("# Estructura del Proyecto\n\n")
        for root, dirs, files in os.walk(ruta):
            # Filtrar directorios ocultos
            filtrar_directorios(dirs)

            # Calcular el nivel de profundidad
            relative_path = os.path.relpath(root, ruta)
            if relative_path == '.':
                level = 0
            else:
                level = relative_path.count(os.sep) + 1
            indent = '    ' * level  # 4 espacios por nivel de indentación

            # Escribir el nombre de la carpeta
            carpeta = os.path.basename(root)
            if carpeta:  # Evitar escribir una línea vacía para la ruta raíz si es necesario
                f.write(f"{indent}- **🗀  {carpeta}/**\n")

            # Escribir los archivos dentro de la carpeta, excluyendo los de directorios ocultos
            for file in files:
                if not file.startswith('.'):  # Opcional: también puedes excluir archivos ocultos
                    file_indent = '    ' * (level + 1)
                    f.write(f"{file_indent}- 🗋  {file}\n")


# ... Aquí van las demás funciones como las que tienes ...

def main():
    # Configuración de la ventana principal
    root = Tk()
    root.title("Generador de Estructura Markdown")
    root.geometry("800x800")
    style = Style(theme='cosmo')  # Usando el tema "clear"

    # Cargar la imagen de portada
    portada = Image.open("portada.png")  # Asegúrate de que la imagen está en el mismo directorio que el script
    portada = portada.resize((512, 512))  # Ajustamos el tamaño si es necesario
    portada_img = ImageTk.PhotoImage(portada)  # Convertimos la imagen para usarla en Tkinter

    # Crear un Label para mostrar la imagen de portada
    portada_label = ttk.Label(root, image=portada_img)
    portada_label.pack(pady=10)  # La imagen se mostrará en la parte superior con algo de espacio

    # Variables para almacenar las rutas
    ruta_carpeta = StringVar()
    ruta_archivo = StringVar()

    # Funciones para seleccionar carpetas y archivos
    def seleccionar_carpeta():
        carpeta = filedialog.askdirectory()
        if carpeta:
            ruta_carpeta.set(carpeta)

    def seleccionar_archivo():
        archivo = filedialog.asksaveasfilename(defaultextension=".md",
                                               filetypes=[("Markdown files", "*.md")])
        if archivo:
            ruta_archivo.set(archivo)

    # Función para actualizar la etiqueta de estado
    def actualizar_label(texto):
        estado_var.set(texto)
        root.update_idletasks()

    # Diseño de la UI
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill=BOTH, expand=True)

    # Selección de carpeta de origen
    carpeta_label = ttk.Label(frame, text="Carpeta de Origen:")
    carpeta_label.grid(row=0, column=0, sticky=W, pady=5)

    carpeta_entry = ttk.Entry(frame, textvariable=ruta_carpeta, width=50)
    carpeta_entry.grid(row=0, column=1, pady=5, padx=5)

    carpeta_button = ttk.Button(frame, text="Seleccionar Carpeta", command=seleccionar_carpeta)
    carpeta_button.grid(row=0, column=2, pady=5)

    # Selección de archivo de salida
    archivo_label = ttk.Label(frame, text="Archivo de Salida (.md):")
    archivo_label.grid(row=1, column=0, sticky=W, pady=5)

    archivo_entry = ttk.Entry(frame, textvariable=ruta_archivo, width=50)
    archivo_entry.grid(row=1, column=1, pady=5, padx=5)

    archivo_button = ttk.Button(frame, text="Seleccionar Archivo", command=seleccionar_archivo)
    archivo_button.grid(row=1, column=2, pady=5)

    # Botón para iniciar el proceso
    procesar_button = ttk.Button(frame, text="Iniciar Proceso",
                                 command=lambda: iniciar_proceso(
                                     ruta_carpeta.get(),
                                     ruta_archivo.get(),
                                     actualizar_label
                                 ))
    procesar_button.grid(row=2, column=1, pady=20)

    # Etiqueta para mostrar el estado
    estado_var = StringVar()
    estado_var.set("Esperando para iniciar...")
    estado_label = ttk.Label(frame, textvariable=estado_var, bootstyle="info")
    estado_label.grid(row=3, column=0, columnspan=3, pady=10)

    # Ajuste de columnas
    frame.columnconfigure(1, weight=1)

    root.mainloop()


if __name__ == "__main__":
        main()
