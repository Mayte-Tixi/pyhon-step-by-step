#Modulos y paquetes
#Los modulos basicamente son los ficheros que se crean exclusivamente como contenedores de n funciones 
#paquetes son contenedores de n Modulos.
#El presente modulo sera llamado y calculado en el fichero init.py
import math
def circulo_perimetro(radio):
    a=((2*math.pi)*radio)
    return a

def area_circulo(radio):
    area=((math.pi*radio)**2)
    return area