#* TUPLAS, no son modificables 
tupla=2,3,5,1,2,2
w,x,y,z,a,b=tupla
print(tupla[0:4]) 
# las tuplas no son modificables por lo tanto a continuacion veremos algunas funciones de consultas
print("el tamano de la tupla es= ",len(tupla))
print('Posicion que ocupa del objeto dentro de la tupla=',tupla.index(5))
#la funcion count contabiliza cunatas veces esta repetido un valor dentro de la tupla
print(tupla.count(2))

#* Diccionario son dinamicos, se pueden modificar los datos
diccionario={'clave':"si puedo",
             'clave1': "puedo inciar de 0",
             1:"Amor"}

#ingresar mas valores dentro del diccionario
diccionario[2]='mi corazon solo sabe amar'
diccionario['clave2']=5

print('el tamano del diccionario es =',len(diccionario)) 
# modificar el valor del dato dentro del diccionario
diccionario['clave']='puedo por mi y para mi'
#eliminar elementos del diccionario
del diccionario['clave1']
print(diccionario)
print('hola' in diccionario)
#* CONJUNTOS 
#Los conjuntos son dinamicos al igual que las listas pero, con la diferencia que no permite almacenar valores repetidos dentro del conjunto
conjuto={'hola','hola2',1,2,3}
conjuto2={1,2,3,4}
print(conjuto2)
#funciones para trabajar con los conjuntos
print(conjuto.union(conjuto2))
#interseccion para verificar que elementos estan repetidos
print(conjuto.intersection(conjuto2))
#inferencia
print(conjuto.difference(conjuto2))
#para verificar si existe el valor dentro del conjunto
print(2 in conjuto2)
#verificar el tamano del conjunto
print(len(conjuto))