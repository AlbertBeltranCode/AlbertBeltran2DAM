import pandas as pd  # Importamos la librería pandas, que se usa para manipular y analizar datos estructurados.

# Carga un archivo de hoja de cálculo OpenDocument (.ods) en un DataFrame de pandas.
df = pd.read_excel('clientes.ods', engine='odf')
# El parámetro 'engine="odf"' especifica el motor que pandas debe usar para leer archivos en formato ODS.

# Muestra las primeras cinco filas del DataFrame para verificar los datos.
print(df.head())

# Define la ruta donde se guardará el archivo JSON.
ruta = 'clientesdesdeexcel.json'

# Convierte el DataFrame a formato JSON y lo guarda en la ruta especificada.
# 'orient="records"' organiza los datos como una lista de registros (uno por fila).
# 'lines=True' guarda cada registro en una línea separada (esto es útil para JSON de línea única, como en algunos logs).
df.to_json(ruta, orient='records', lines=True)