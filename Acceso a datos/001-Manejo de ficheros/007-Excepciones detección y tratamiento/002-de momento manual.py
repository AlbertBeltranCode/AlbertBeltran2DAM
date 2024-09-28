class Cliente: #Creamos una clase cliente con sus valores
    def __init__(self):
        self.nombre = None
        self.apellidos = None
        self.emails = {"personal":[],"profesional":[]}

class Producto: #Creamos una clase producto con sus valores
    def __init__(self):
        self.nombre = None
        self.precio = None
        self.peso = None
        self.dimensiones = {"x":None,"y":None,"z":None}

clientes = []
clientes.append(Cliente())

clientes[-1].nombre = "Albert"
clientes[-1].apellidos = "Beltran Carbonell"
clientes[-1].emails['profesional'].append("albertbeltrancode@gmail.com")
clientes[-1].emails['profesional'].append("albert@programacion.com")
clientes[-1].emails['personal'].append("albert2@programacion.com")

print(clientes[-1].emails)
        


