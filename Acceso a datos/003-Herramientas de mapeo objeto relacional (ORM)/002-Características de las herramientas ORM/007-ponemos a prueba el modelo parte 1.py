import mysql.connector
###################################### CREO UNA CLASE QUE ES EL MODELO DE DATOS
class Profesor:
    def __init__(self,
                    nuevonombre,  # Parámetro para inicializar el nombre del profesor
                    nuevadescripcion,  # Parámetro para inicializar la descripción del profesor
                     nuevosalumnos):  # Parámetro para inicializar la lista de alumnos del profesor
        self.nombre = nuevonombre  # Atributo que almacena el nombre del profesor
        self.descripcion = nuevadescripcion  # Atributo que almacena la descripción del profesor
        self.alumnos =  nuevosalumnos  # Atributo que almacena la lista de alumnos
clase = "Profesor"  # Nombre de la tabla/clase en la base de datos

##################################### PREPARO UNA CONEXIÓN CON EL SERVIDOR

conexion = mysql.connector.connect(
            host='localhost',  # Dirección del servidor de la base de datos
            database='accesoadatos',  # Nombre de la base de datos
            user='accesoadatos',  # Usuario para conectarse a la base de datos
            password='accesoadatos'  # Contraseña del usuario de la base de datos
        )

cursor = conexion.cursor()  # Configuro el cursor para interactuar con la base de datos

##################################### CREO UNA LISTA DE PROFESORES

profesores = []  # Lista vacía para almacenar objetos de tipo Profesor

profesores.append(Profesor("Jose Vicente", "Profesor de informatica", ['Albert', 'Jose Manuel', 'Dragos']))  
# Agrego un objeto Profesor con un nombre, descripción y lista de alumnos

##################################### BORRAMOS LA TABLA ANTERIOR POR SI ACASO HAY DATOS ANTERIOR

peticion = "DROP TABLE IF EXISTS "+clase  # Preparo una consulta para eliminar la tabla si ya existe
cursor.execute(peticion)  # Ejecuto la consulta

##################################### CREACIÓN DINÁMICA DE LA TABLA EN LA BASE DE DATOS

peticion = "CREATE TABLE IF NOT EXISTS "+clase+" (Identificador INT NOT NULL AUTO_INCREMENT,"  
# Inicio la consulta para crear una tabla con un campo de Identificador auto-incremental

atributos = [attr for attr in dir(profesores[0]) if not callable(getattr(profesores[0], attr)) and not attr.startswith("__")]  
# Obtengo los atributos de la clase Profesor que no sean métodos ni especiales (mágicos)

for atributo in atributos:  # Itero sobre los atributos obtenidos
    if not isinstance(getattr(profesores[0], atributo), list):  
        # Si el atributo no es una lista, es un campo simple
        peticion += atributo+" VARCHAR(255) NOT NULL ,"  # Lo agrego como una columna en la tabla principal
    else:  
        # Si el atributo es una lista, se trata de una relación con otra tabla
        peticion2 = "DROP TABLE IF EXISTS "+atributo+""  # Preparo la consulta para eliminar la tabla relacionada si existe
        cursor.execute(peticion2)  # Ejecuto la consulta
        peticion2 = "CREATE TABLE IF NOT EXISTS "+atributo+" (Identificador INT NOT NULL AUTO_INCREMENT,FK INT(255),"+atributo+" VARCHAR(255),PRIMARY KEY (Identificador))"  
        # Creo una tabla separada para este atributo con una clave foránea FK
        cursor.execute(peticion2)  # Ejecuto la consulta para crear la tabla relacionada

peticion += " PRIMARY KEY (Identificador))"  # Agrego la clave primaria para la tabla principal

print(peticion)  # Imprimo la consulta generada
cursor.execute(peticion)  # Ejecuto la consulta para crear la tabla principal

##################################### INSERCIÓN DINÁMICA DE REGISTROS EN LA BASE DE DATOS

for indice, profesor in enumerate(profesores):  # Itero sobre los profesores en la lista
    peticion = "INSERT INTO "+clase+" VALUES(NULL,"  # Inicio la consulta para insertar un registro en la tabla principal

    for atributo in atributos:  # Itero sobre los atributos de la clase
        if not isinstance(getattr(profesor, atributo), list):  
            # Si el atributo no es una lista, se agrega directamente
            peticion += "'"+str(getattr(profesor, atributo))+"',"  # Lo agrego a la consulta
        else:  
            # Si el atributo es una lista, inserto cada elemento en la tabla relacionada
            for elemento in getattr(profesor, atributo):
                peticion2 = "INSERT INTO "+atributo+" VALUES(NULL,"+str(indice+1)+",'"+str(elemento)+"')"  
                # Preparo la consulta para insertar en la tabla relacionada
                cursor.execute(peticion2)  # Ejecuto la consulta para la tabla relacionada
                peticion = peticion[:-1]  # Elimino la última coma en la consulta de la tabla principal
    peticion += ");"  # Cierro la consulta de inserción
    cursor.execute(peticion)  # Ejecuto la consulta para insertar en la tabla principal

conexion.commit()  # Confirmo los cambios realizados en la base de datos
















