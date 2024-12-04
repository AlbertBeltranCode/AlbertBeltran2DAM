import mysql.connector
###################################### CREO UNA CLASE QUE ES EL MODELO DE DATOS
class Producto:
    def __init__(self):
        self.nombre = None  # Atributo para el nombre del producto
        self.descripcion = None  # Atributo para la descripción del producto
        self.precio = None  # Atributo para el precio del producto
        self.categorias =  None  # Atributo para las categorías relacionadas con el producto
clase = "Producto"  # Defino el nombre de la tabla/clase en la base de datos

##################################### PREPARO UNA CONEXIÓN CON EL SERVIDOR

conexion = mysql.connector.connect(
            host='localhost',  # Dirección del host de la base de datos
            database='accesoadatos',  # Nombre de la base de datos
            user='accesoadatos',  # Usuario para conectarse a la base de datos
            password='accesoadatos'  # Contraseña del usuario de la base de datos
        )

cursor = conexion.cursor(dictionary=True)  # Configuro el cursor para obtener resultados como diccionarios

##################################### CREO UNA LISTA DE PRODUCTOS DE LA BASE DE DATOS

productos = []  # Creo una lista vacía para almacenar los productos recuperados

peticion = "SELECT * FROM "+clase  # Construyo la consulta para seleccionar todos los registros de la tabla
cursor.execute(peticion)  # Ejecuto la consulta en la base de datos

filas = cursor.fetchall()  # Recupero todas las filas resultantes de la consulta
for fila in filas:  # Itero sobre cada fila recuperada
    producto = Producto()  # Creo una nueva instancia de Producto
    for clave, valor in fila.items():  # Itero sobre cada clave y valor en la fila
        setattr(producto, clave, valor)  # Establezco el valor correspondiente en el producto

    # Ahora busco si hay tablas externas
    for clave, valor in vars(producto).items():  # Itero sobre los atributos de la instancia del producto
        if valor == None:  # Si el valor del atributo es None, podría indicar una relación con otra tabla
            setattr(producto, clave, [])  # Cambio el valor None por una lista vacía
            print("parece que hay una tabla externa en :", clave)  # Indico que parece haber una tabla relacionada
            peticion2 = "SELECT "+clave+" FROM "+clave+" WHERE FK = "+str(producto.Identificador)  # Construyo la consulta para la tabla relacionada
            cursor.execute(peticion2)  # Ejecuto la consulta en la tabla relacionada
            filas2 = cursor.fetchall()  # Recupero las filas de la tabla relacionada
            for fila2 in filas2:  # Itero sobre cada fila de la tabla relacionada
                print(fila2)  # Imprimo la fila recuperada
                # append to property here as a list
                getattr(producto, clave).append(fila2[clave])  # Agrego el valor recuperado a la lista correspondiente en el producto
    productos.append(producto)  # Agrego el producto a la lista de productos

print(vars(productos[0]))  # Imprimo los atributos del primer producto en la lista

personas = []  # Inicializo una lista vacía para posibles datos de personas
conexion.commit()  # Confirma las operaciones realizadas en la base de datos

















