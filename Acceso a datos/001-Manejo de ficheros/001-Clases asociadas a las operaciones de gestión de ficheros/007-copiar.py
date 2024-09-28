import shutil #Importamos la libreria shutil para copiar y remover archivos
 
origen = 'origen/documento.txt' #Carpeta de origen del archivo
destino = 'destino/documento.txt' #Carpeta destino del archivo
 
shutil.copy(origen, destino) #Copia el archivo de origen en la carpeta de destino

