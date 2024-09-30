import xml.etree.ElementTree as ET
import tkinter as tk
import ttkbootstrap

ventana = tk.Tk() # Creamos la ventana principal

# Cargamos el archivo XML y lo parseamos en un árbol de elementos
arbol = ET.parse('013-interfaz.xml') 
# Obtenemos la raíz del árbol XML
raiz = arbol.getroot()

for elemento in raiz: # Por cada elemento dentro de la raiz,
                       # filtrando los tipos de elementos disponibles segun su tipo
    if elemento.tag == "boton":
        tk.Button(ventana,text=elemento.text).pack(padx=20,pady=20) #Creamos un boton
    elif elemento.tag == "texto":
        tk.Label(ventana,text=elemento.text).pack(padx=20,pady=20) #Creamos un texto
    elif elemento.tag == "entrada": #Creamos una entrada
        tk.Entry(ventana).pack(padx=20,pady=20)

ventana.mainloop() # Inicia el bucle principal de la ventana