variable1 = "hola" #Creamos una variable y le asignamos el valor de String
variable2 = "que tal" #Creamos una variable2 y le asignamos el valor de String

archivo = open("archivo.txt",'w') #Creamos un archivo txt
archivo.write(variable1+"|"+variable2) #Escribimos las 2 variables dentro del archivo
archivo.close()

