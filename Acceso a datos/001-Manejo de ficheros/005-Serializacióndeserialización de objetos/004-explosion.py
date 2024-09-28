archivo = open("archivo.txt",'r') #Abrimos el archivo
contenido = archivo.read() #Leemos el archivo
print(contenido) #Mostramos en pantalla el contenido del archivo
lista = contenido.split("|") #Separamos el contenido del archivo con barras verticales
print(lista) #Mostramos en pantalla el contenido de la lista

variable1 = lista[0] #Asignamos a la variable 1 el primer valor de la lista
variable2 = lista[1] #Asignamos a la variable 2 el segundo valor de la lista

print(variable1) #Mostramos por pantalla la variable 1
print(variable2) #Mostramos por pantalla la variable 2
