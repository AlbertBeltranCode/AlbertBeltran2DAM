import os #Importamos la libreria del sitema

lista = os.listdir("fotos") #Creamos una lista a la que asignamos el directorio fotos

for archivo in lista: #Mediante un bucle for, recorremos la lista por cada archivo de el directorio fotos
    print(archivo)
