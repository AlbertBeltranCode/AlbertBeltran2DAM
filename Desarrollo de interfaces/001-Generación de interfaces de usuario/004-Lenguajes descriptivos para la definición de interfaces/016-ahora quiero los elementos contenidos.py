import xml.etree.ElementTree as ET # Importamos la librería ElementTree para trabajar con archivos XML

# Cargamos el archivo XML y lo parseamos en un árbol de elementos
arbol = ET.parse('013-interfaz.xml') 
# Obtenemos la raíz del árbol XML
raiz = arbol.getroot()

# Imprimimos la raíz del documento XML
print(raiz)
for elemento in raiz: # Por cada elemento dentro de la raiz hacemos un print de dicho elemento
    print(elemento)
