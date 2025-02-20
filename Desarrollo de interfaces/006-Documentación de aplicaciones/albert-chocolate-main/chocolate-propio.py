import os
import threading
import datetime
from tkinter import Tk, StringVar, BooleanVar, filedialog
from ttkbootstrap import ttk, Style
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

def convertir_tamano(bytes):
    """Convierte bytes a un formato legible (KB, MB, GB)"""
    if bytes < 1024:
        return f"{bytes} B"
    elif bytes < 1024**2:
        return f"{bytes/1024:.2f} KB"
    elif bytes < 1024**3:
        return f"{bytes/(1024**2):.2f} MB"
    else:
        return f"{bytes/(1024**3):.2f} GB"

def filtrar_directorios(dirs):
    """Filtra directorios que comienzan con un punto"""
    dirs[:] = [d for d in dirs if not d.startswith('.')]

def get_selected_extensions(ext_vars, all_files_var):
    """Obtiene las extensiones seleccionadas de los checkboxes"""
    if all_files_var.get():
        return None  # None significa incluir todos los archivos
    return [ext for ext, var in ext_vars.items() if var.get()]

def should_include_file(file_path, selected_extensions):
    """Verifica si un archivo debe ser incluido basado en las extensiones"""
    if selected_extensions is None:
        return True
    file_ext = os.path.splitext(file_path)[1].lower().lstrip('.')
    return file_ext in selected_extensions

def listar_estructura_markdown(ruta, archivo_salida, selected_extensions):
    """Genera la estructura del directorio con metadatos y filtrado"""
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("# Estructura del Proyecto\n\n")
        for root, dirs, files in os.walk(ruta):
            filtrar_directorios(dirs)
            
            relative_path = os.path.relpath(root, ruta)
            level = 0 if relative_path == '.' else relative_path.count(os.sep) + 1
            indent = '    ' * level
            
            carpeta = os.path.basename(root)
            if carpeta:
                mtime = os.path.getmtime(root)
                fecha_dir = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"{indent}- **🗀  {carpeta}/** (Última modificación: {fecha_dir})\n")
            
            for file in files:
                file_path = os.path.join(root, file)
                if not file.startswith('.') and should_include_file(file_path, selected_extensions):
                    try:
                        stat = os.stat(file_path)
                        size = convertir_tamano(stat.st_size)
                        fecha_creacion = datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                        fecha_modificacion = datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                        
                        file_indent = '    ' * (level + 1)
                        metadata = f"Tamaño: {size}, Creado: {fecha_creacion}, Modificado: {fecha_modificacion}"
                        f.write(f"{file_indent}- 🗋  {file} ({metadata})\n")
                    except Exception as e:
                        file_indent = '    ' * (level + 1)
                        f.write(f"{file_indent}- 🗋  {file} (Error al obtener metadatos)\n")
                        print(f"Error procesando {file_path}: {e}")

def procesar(carpeta, archivo_md, actualizar_label, ext_vars, all_files_var):
    """Ejecuta el procesamiento con filtrado"""
    try:
        selected_ext = get_selected_extensions(ext_vars, all_files_var)
        listar_estructura_markdown(carpeta, archivo_md, selected_ext)
        actualizar_label(f"Proceso completado. Archivo generado: {archivo_md}")
    except Exception as e:
        actualizar_label(f"Error: {str(e)}")

def iniciar_proceso(carpeta, archivo_md, actualizar_label, ext_vars, all_files_var):
    """Inicia el procesamiento en un hilo separado"""
    hilo = threading.Thread(target=procesar, args=(carpeta, archivo_md, actualizar_label, ext_vars, all_files_var))
    hilo.start()

def create_filetype_filters(frame):
    """Crea los checkboxes de filtrado por tipo de archivo"""
    filter_frame = ttk.Labelframe(frame, text="Filtros de Tipo de Archivo", padding=10)
    filter_frame.grid(row=4, column=0, columnspan=3, pady=10, sticky="ew")
    
    extensions = {
        'all': ('Todos los archivos', True),
        'py': ('Python (.py)', False),
        'js': ('JavaScript (.js)', False),
        'html': ('HTML (.html)', False),
        'css': ('CSS (.css)', False),
        'md': ('Markdown (.md)', False),
        'txt': ('Archivos de texto (.txt)', False)
    }
    
    ext_vars = {}
    checkboxes = {}
    all_files_var = BooleanVar(value=True)
    
    # Create "All Files" checkbox
    all_cb = ttk.Checkbutton(
        filter_frame,
        text=extensions['all'][0],
        variable=all_files_var,
        command=lambda: toggle_all_files(ext_vars, checkboxes, all_files_var)
    )
    all_cb.grid(row=0, column=0, sticky=W, padx=5)
    
    # Create individual checkboxes
    for idx, (ext, (text, default)) in enumerate(extensions.items()):
        if ext == 'all':
            continue
        var = BooleanVar(value=default)
        ext_vars[ext] = var
        
        cb = ttk.Checkbutton(
            filter_frame,
            text=text,
            variable=var,
            state=DISABLED if all_files_var.get() else NORMAL
        )
        cb.grid(row=idx//3 + 1, column=idx%3, sticky=W, padx=5, pady=2)
        checkboxes[ext] = cb
    
    return ext_vars, all_files_var, checkboxes

def toggle_all_files(ext_vars, checkboxes, all_files_var):
    """Alterna el estado de los checkboxes individuales"""
    new_state = NORMAL if not all_files_var.get() else DISABLED
    
    # Update state and clear selections
    for ext, cb in checkboxes.items():
        cb.configure(state=new_state)
        if all_files_var.get():
            ext_vars[ext].set(False)  # Access the variable directly from ext_vars
        # En una implementación real necesitarías acceder a los widgets directamente
        # Esta es una versión simplificada

def main():
    root = Tk()
    root.title("Generador de Estructura Markdown")
    root.geometry("1000x850")
    style = Style(theme='cosmo')

    try:
        portada = Image.open("portada.png")
        portada = portada.resize((512, 512))
        portada_img = ImageTk.PhotoImage(portada)
        portada_label = ttk.Label(root, image=portada_img)
        portada_label.pack(pady=10)
    except FileNotFoundError:
        print("Advertencia: Imagen de portada no encontrada")

    ruta_carpeta = StringVar()
    ruta_archivo = StringVar()
    estado_var = StringVar()

    def seleccionar_carpeta():
        if carpeta := filedialog.askdirectory():
            ruta_carpeta.set(carpeta)

    def seleccionar_archivo():
        if archivo := filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md")]
        ):
            ruta_archivo.set(archivo)

    def actualizar_label(texto):
        estado_var.set(texto)
        root.update_idletasks()

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill=BOTH, expand=True)

    ttk.Label(frame, text="Carpeta de Origen:").grid(row=0, column=0, sticky=W, pady=5)
    ttk.Entry(frame, textvariable=ruta_carpeta, width=50).grid(row=0, column=1, pady=5, padx=5)
    ttk.Button(frame, text="Seleccionar Carpeta", command=seleccionar_carpeta).grid(row=0, column=2, pady=5)

    ttk.Label(frame, text="Archivo de Salida (.md):").grid(row=1, column=0, sticky=W, pady=5)
    ttk.Entry(frame, textvariable=ruta_archivo, width=50).grid(row=1, column=1, pady=5, padx=5)
    ttk.Button(frame, text="Seleccionar Archivo", command=seleccionar_archivo).grid(row=1, column=2, pady=5)

    ext_vars, all_files_var, checkboxes = create_filetype_filters(frame)

    ttk.Button(frame, text="Iniciar Proceso",
              command=lambda: iniciar_proceso(
                  ruta_carpeta.get(),
                  ruta_archivo.get(),
                  actualizar_label,
                  ext_vars,
                  all_files_var)
              ).grid(row=5, column=1, pady=20)

    estado_label = ttk.Label(frame, textvariable=estado_var, bootstyle="info")
    estado_label.grid(row=6, column=0, columnspan=3, pady=10)
    estado_var.set("Esperando para iniciar...")

    frame.columnconfigure(1, weight=1)
    root.mainloop()

if __name__ == "__main__":
    main()
