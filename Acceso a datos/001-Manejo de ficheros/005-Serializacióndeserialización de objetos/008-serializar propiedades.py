import random
import math
# Declaro una clase Npc y le pongo dos sencillas propiedades x e y ademas de un angulo
class Npc:
    def __init__(self):
        self.x = random.randint(0,512)
        self.y = random.randint(0,512)
        self.angulo = random.random()*math.pi*2
# Creo una lista de 45 npcs
npcs = []
numero = 45
# Recorro la lista y a cada elemento le meto una instancia de la clase Npc
for i in range(0,numero):
    npcs.append(Npc())

cadena = ""
# Recorro la lista y por cada elementro muestro su respectivo valor en X, Y e angulo
for i in range(0,numero):
    cadena += str(npcs[i].x)+","+str(npcs[i].y)+","+str(npcs[i].angulo)+"|"

print(cadena) #Mostramos la cadena de valores
mibasededatos = open("basededatos.txt",'w') #Creamos un archivo txt
mibasededatos.write(cadena) #Escrbimos el contenido de la cadena dentro del archivo
mibasededatos.close()


