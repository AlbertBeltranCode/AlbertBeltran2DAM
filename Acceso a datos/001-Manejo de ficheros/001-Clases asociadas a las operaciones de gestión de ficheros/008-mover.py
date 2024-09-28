import shutil #Importamos la libreria shutil para copiar y remover archivos
 
origen = 'origen/documento.txt' #Carpeta de origen del archivo
destino = 'destino/documento.txt' #Carpeta destino del archivo
 
shutil.move(origen, destino) #Mueve el archivo de la carpeta origen a la carpeta destino

