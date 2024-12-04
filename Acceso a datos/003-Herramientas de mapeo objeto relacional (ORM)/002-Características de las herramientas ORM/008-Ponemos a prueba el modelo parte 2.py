import mysql.connector
###################################### CREO UNA CLASE QUE ES EL MODELO DE DATOS
class Profesor:
    def __init__(self):
        self.nombre = None  # Atributo para almacenar el nombre del profesor
        self.descripcion = None  # Atributo para almacenar la descripción del profesor
        self.alumnos =  None  # Atributo que representará una relación con otra tabla (lista de alumnos)
clase = "Profesor"  # Nombre de la tabla/clase en la base de datos

##################################### PREPARO UNA CONEXIÓN CON EL SERVIDOR

conexion = mysql.connector.connect(
            host='localhost',  # Dirección del servidor de la base de datos
            database='accesoadatos',  # Nombre de la base de datos
            user='accesoadatos',  # Usuario para conectarse a la base de datos
            password='accesoadatos'  # Contraseña del usuario de la base de datos
        )

cursor = conexion.cursor(dictionary=True)  # Configuro el cursor para obtener resultados como diccionarios

##################################### CREO UNA LISTA DE PRODUCTOS DE LA BASE DE DATOS

profesores = []  # Creo una lista vacía para almacenar los objetos Profesor

peticion = "SELECT * FROM "+clase  # Preparo la consulta para seleccionar todos los registros de la tabla
cursor.execute(peticion)  # Ejecuto la consulta en la base de datos

filas = cursor.fetchall()  # Recupero todas las filas obtenidas de la consulta
for fila in filas:  # Itero sobre cada fila recuperada
    profesor = Profesor()  # Creo una nueva instancia de Profesor
    for clave, valor in fila.items():  # Itero sobre cada clave y valor de la fila
        setattr(profesor, clave, valor)  # Establezco el valor correspondiente en la instancia de Profesor

    # Ahora busco si hay tablas externas relacionadas
    for clave, valor in vars(profesor).items():  # Itero sobre los atributos del profesor
        if valor == None:  # Si el atributo tiene un valor None, podría indicar una relación con otra tabla
            setattr(profesor, clave, [])  # Cambio el valor None por una lista vacía
            print("parece que hay una tabla externa en :", clave)  # Indico que se detectó una tabla relacionada
            peticion2 = "SELECT "+clave+" FROM "+clave+" WHERE FK = "+str(profesor.Identificador)  
            # Preparo una consulta para seleccionar registros de la tabla relacionada
            cursor.execute(peticion2)  # Ejecuto la consulta en la tabla relacionada
            filas2 = cursor.fetchall()  # Recupero las filas de la tabla relacionada
            for fila2 in filas2:  # Itero sobre cada fila recuperada de la tabla relacionada
                print(fila2)  # Imprimo la fila recuperada
                # Agrego los valores de la tabla relacionada a la lista correspondiente
                getattr(profesor, clave).append(fila2[clave])  
    profesores.append(profesor)  # Agrego el profesor a la lista de profesores

print(vars(profesores[0]))  # Imprimo los atributos del primer profesor en la lista

profesores = []  # Inicializo nuevamente la lista de profesores (vacía)
conexion.commit()  # Confirmo las operaciones realizadas en la base de datos
















