#practicas de los tipos de datos
#entero
n=10
n1=True
n2=6.4
mensaje="Si puedo soy excelente profesional y programadora amo aprender la IA"
# tipos de datos
print(type(n))
print(type(n1))
print(type(n2))
print(type(mensaje))
#transformar los tipos de datos
print(str(n))
print(int(n2))
#funciones que se puede utilizar con el tipo de datos String 
#transformar a mayuscula
mayuscula=mensaje.upper()
minuscula=mensaje.lower()
print(mayuscula)
print(minuscula)
transformar=mensaje.replace("profesional", " persona")
print(transformar)
#PRACTICAS DE ESTRUCTURAS DE DATOS(lISTAS, TUPLAS, DICCIONARIOS, CONJUNTOS )
#**LISTAS 
# en las listas pueden agregar todo tipo de datos 
lista=[3,5.5,4,'soy muy inteligente yo puedo',True]
# recuerden que la lista recorre desde la posicion 0 : hasta n datos dentro de la lista 
print('la posicion impresa de la lista es=',lista[3])
print('imprimir desde hasta=',lista[0:3])
print(len(lista))
#la funcion iundex indica  la posicion que ocupa un objeto dentro de una lista
print(lista.index('soy muy inteligente yo puedo'))
# la funcion inset agrega datos a la lista seleccuionando la posicion al lado izquierdo
#append ingresa valores a la lista al final, tambien se puede agregar sub listas dentro de la lista que tenemos creado.
lista.insert(1,"soy muy inteligente")
lista.append([2,1,3,"somos 2"])
print(lista[6])
#funcion extend agreda elementos dentro de la lista elemento x elemento
lista.extend(['zorro','zorro','zorro','zorro','leon','jirafa'])

#funcion para eliminar elementos de una lista
lista.remove('leon')
#funcion para contabilizar los elementos que se encuentran repetidos dentro de una lista
print(lista)
print('la palabra zorro dentro de la lista se repite=',lista.count('zorro'))
#funcion que ordena los elementos de una lista del final hacia adelante
lista1=[1,3,4,5,9,2,6]
#lista de menor a meyor
lista1.sort()
#lista de mayor a menor
lista1.sort(reverse=True)

#funcion que eliminar un dato de la lista 
lista1.pop(0)
print(lista1)






