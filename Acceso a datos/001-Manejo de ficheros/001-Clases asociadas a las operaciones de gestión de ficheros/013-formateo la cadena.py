import os #Importamos la libreria del sitema
import PIL.Image #Importamos la libreria PIL que nos permite trabajar con imagenes/fotografias

lista = os.listdir("fotos") #Creamos una lista a la que asignamos el directorio fotos

for archivo in lista: #Mediante un bucle for, recorremos la lista por cada archivo de el directorio fotos
    print(archivo)
    imagen = PIL.Image.open('fotos/'+archivo) #Abrimos la fotografia
    datosexif = imagen._getexif() #Recogemos los datos de la fotografia
    cadena = datosexif[306].replace(":","-").replace(" ","_") #Recogemos el valor 306, que en este caso es la fecha de la toma de la foto y nos aseguramos de remplazar los : por guiones
    print(cadena)
   
