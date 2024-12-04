import mysql.connector
###################################### CREO UNA CLASE QUE ES EL MODELO DE DATOS
class Producto:
    def __init__(self,
                    nuevonombre,  # Nombre del producto
                    nuevadescripcion,  # Descripción del producto
                    nuevoprecio,  # Precio del producto
                    nuevascategorias):  # Categorías asociadas al producto
        self.nombre = nuevonombre  # Asigno el nombre al atributo de la clase
        self.descripcion = nuevadescripcion  # Asigno la descripción al atributo de la clase
        self.precio = nuevoprecio  # Asigno el precio al atributo de la clase
        self.categorias =  nuevascategorias  # Asigno las categorías al atributo de la clase
clase = "Producto"  # Nombre de la clase que se utilizará como nombre de la tabla en la base de datos

##################################### PREPARO UNA CONEXIÓN CON EL SERVIDOR

conexion = mysql.connector.connect(
            host='localhost',  # Dirección del servidor de la base de datos
            database='accesoadatos',  # Nombre de la base de datos
            user='accesoadatos',  # Usuario de la base de datos
            password='accesoadatos'  # Contraseña del usuario de la base de datos
        )

cursor = conexion.cursor()  # Creo el cursor para ejecutar consultas en la base de datos

##################################### CREO UNA LISTA DE PRODUCTOS

personas = []  # Creo una lista vacía para almacenar los productos

# Agrego algunos productos a la lista
personas.append(Producto("Camiseta","Camiseta fenomenal para el dia a dia",34.56,['ropa','caballero']))
personas.append(Producto("Pantalon","Pantalon para vestir de noche",56.43,['ropa','señora']))

##################################### BORRAMOS LA TABLA ANTERIOR POR SI ACASO HAY DATOS ANTERIOR

peticion = "DROP TABLE IF EXISTS "+clase  # Preparo la petición para eliminar la tabla si existe
cursor.execute(peticion)  # Ejecuto la petición para eliminar la tabla

##################################### CREACIÓN DINÁMICA DE LA TABLA EN LA BASE DE DATOS

peticion = "CREATE TABLE IF NOT EXISTS "+clase+" (Identificador INT NOT NULL AUTO_INCREMENT,"  # Empiezo a preparar la creación de la tabla

# Listo los atributos de la clase Producto
atributos = [attr for attr in dir(personas[0]) if not callable(getattr(personas[0], attr)) and not attr.startswith("__")]

for atributo in atributos:  # Itero sobre cada uno de los atributos de la clase Producto
    if not isinstance(getattr(personas[0], atributo), list):  # Si el atributo no es una lista
        peticion += atributo+" VARCHAR(255) NOT NULL ,"  # Lo agrego a la creación de la tabla como columna de tipo VARCHAR
    else:  # Si el atributo es una lista
        peticion2 = "DROP TABLE IF EXISTS "+atributo+""  # Elimino la tabla relacionada si existe
        cursor.execute(peticion2)  # Ejecuto la eliminación de la tabla
        peticion2 = "CREATE TABLE IF NOT EXISTS "+atributo+" (Identificador INT NOT NULL AUTO_INCREMENT,FK INT(255),"+atributo+" VARCHAR(255),PRIMARY KEY (Identificador))"  
        # Creo la tabla para almacenar los valores de la lista relacionada
        cursor.execute(peticion2)  # Ejecuto la creación de la tabla relacionada

peticion += " PRIMARY KEY (Identificador))"  # Defino la clave primaria en la tabla

print(peticion)  # Imprimo la petición SQL generada para la creación de la tabla
cursor.execute(peticion)  # Ejecuto la creación de la tabla en la base de datos

##################################### INSERCIÓN DINÁMICA DE REGISTROS EN LA BASE DE DATOS

# Para cada uno de los productos en la lista, realizo una inserción en la base de datos
for indice, persona in enumerate(personas):
    peticion = "INSERT INTO "+clase+" VALUES(NULL,"  # Empiezo a preparar la consulta de inserción

    for atributo in atributos:  # Itero sobre cada atributo del producto
        if not isinstance(getattr(persona, atributo), list):  # Si el atributo no es una lista
            peticion += "'"+str(getattr(persona, atributo))+"',"  # Agrego el atributo a la consulta de inserción
        else:  # Si el atributo es una lista
            for elemento in getattr(persona, atributo):  # Itero sobre los elementos de la lista
                peticion2 = "INSERT INTO "+atributo+" VALUES(NULL,"+str(indice+1)+",'"+str(elemento)+"')"  
                # Preparo la inserción de cada elemento de la lista en su tabla correspondiente
                cursor.execute(peticion2)  # Ejecuto la inserción

    peticion = peticion[:-1]  # Elimino la última coma de la consulta de inserción
    peticion += ");"  # Cierro la consulta de inserción
    cursor.execute(peticion)  # Ejecuto la inserción en la tabla principal

conexion.commit()  # Confirmo las operaciones realizadas en la base de datos
















