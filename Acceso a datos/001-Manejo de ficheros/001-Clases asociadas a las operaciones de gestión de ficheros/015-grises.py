import os #Importamos la libreria del sitema
from PIL import Image, ImageOps #Importamos la libreria PIL con las funcionalidades Image e ImageOps

lista = os.listdir("fotos") #Creamos una lista a la que asignamos el directorio fotos

for archivo in lista: #Mediante un bucle for, recorremos la lista por cada archivo de el directorio fotos
    print("ok") #Escribimos un OK para cada foto
    imagen = Image.open(r"fotos/"+archivo) #Abrimos la foto
    imagen2 = ImageOps.grayscale(imagen) #Aplicamos un filtro gris a la foto
    imagen.close() #Cerramos el proceso de PIL correspondiente
    imagen2.save('fotos/'+archivo) #Guardamos el archivo
    imagen2.close() #Cerramos el proceso de PIl correspondiente
