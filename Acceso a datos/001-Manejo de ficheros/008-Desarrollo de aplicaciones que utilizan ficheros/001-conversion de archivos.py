import json #Importamos la libreria JSON
import xml #Importamos la libreria XML

with open('cliente.json', 'r') as archivo: #Leemos el archivo cliente.json y lo asginamos como archivo
    datos = json.load(archivo) 

print(datos) #Mostramos los datos del archivo .json


