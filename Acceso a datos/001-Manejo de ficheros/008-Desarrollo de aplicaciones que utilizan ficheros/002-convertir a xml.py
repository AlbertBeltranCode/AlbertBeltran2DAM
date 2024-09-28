import json  # Importa la librería json para trabajar con archivos y datos en formato JSON.
import xml.etree.ElementTree as ET  # Importa ElementTree para crear y manipular estructuras XML.

# Función que convierte un diccionario en un objeto XML.
def dict_to_xml(tag, d):
    # Crea el elemento raíz con el nombre 'tag'.
    elem = ET.Element(tag)
    
    # Recorre los pares clave-valor del diccionario.
    for key, val in d.items():
        # Para cada clave, crea un subelemento y le asigna el valor como texto.
        child = ET.SubElement(elem, key)
        child.text = str(val)  # Convierte el valor a cadena (string) y lo asigna como contenido del elemento XML.
    
    return elem  # Devuelve el elemento raíz con los subelementos correspondientes.

# Función que guarda un diccionario como un archivo XML.
def save_dict_to_xml(filename, root_tag, dictionary):
    # Convierte el diccionario en un objeto XML, usando la etiqueta 'root_tag' como el elemento raíz.
    root = dict_to_xml(root_tag, dictionary)
    
    # Crea un árbol XML a partir del elemento raíz.
    tree = ET.ElementTree(root)
    
    # Escribe el árbol XML en un archivo con el nombre 'filename'.
    tree.write(filename, encoding='utf-8', xml_declaration=True)  # Especifica que se use codificación UTF-8 y añade la declaración XML.

# Abre el archivo 'cliente.json' en modo lectura.
with open('cliente.json', 'r') as archivo:
    # Carga el contenido JSON en la variable 'datos'.
    datos = json.load(archivo)

# Imprime el contenido del archivo JSON (es decir, el diccionario que se ha cargado).
print(datos)

# Convierte los datos JSON en XML y los guarda en un archivo llamado 'cliente.xml'.
save_dict_to_xml('cliente.xml', 'cliente', datos)




