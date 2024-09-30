import xml.etree.ElementTree as ET # Importamos la librería ElementTree para trabajar con archivos XML

# Cargamos el archivo XML y lo parseamos en un árbol de elementos
arbol = ET.parse('013-interfaz.xml') 
# Obtenemos la raíz del árbol XML
raiz = arbol.getroot()

for elemento in raiz:  # Por cada elemento dentro de la raiz hacemos un print de dicho elemento,
                       # filtrando los tipos de elementos disponibles segun su tipo
    if elemento.tag == "boton":
        print("tienes un boton")
    elif elemento.tag == "texto":
        print("tienes un texto")
    elif elemento.tag == "entrada":
        print("tienes una entrada")
