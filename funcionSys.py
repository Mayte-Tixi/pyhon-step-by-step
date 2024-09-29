#funcion Sys que viene incluido in python
import sys
# la funcion Sys proporcina variables y metodos relacionados con el interprete de pyhton
a=sys.argv#permite realizar una lista de los documentos que ha pasado por la linea de comandos.

e=sys.executable
vr=sys.version
plt=sys.platform

#Funcion OS, perimite el acceso a variables y funciones que interactuan directamente con el sistema operativo.
import os
os.getcwd # devuelve  el directorio de la ruta en que nos encontramos
os.mkdir("C:/Users/maykf/Documents/Unir/os/nuevo2")# crea una nueva carpeta en el directorio seleccionado

elimina=os.rmdir("C:/Users/maykf/Documents/Unir/os/nuevo")# elimina la carpeta seleccionada o creada
renombrar=os.rename("C:/Users/maykf/Documents/Unir/os/nuevo1","C:/Users/maykf/Documents/Unir/os/amor")

remove=os.remove("C:/Users/maykf/Documents/Unir/os/amor")#remove elimina los ficheros 


#\ sub modulo de la funcion os 
import os.path
#indica la ruta absoluta donde se encuntra el fichero
ruta=os.path.abspath('./hola.txt')
retorna=os.path.basename('./amor')#retorna el nombre de la carpeta o fichero
existe=os.path.exists('C:/Users/maykf/Documents/Unir/os')# verifica si existe una carpeta
esfichero=os.path.isfile()#indica si existe un fichero
esdir=os.path.isdir()#indica si existe un directorio


print("imprimir",existe)