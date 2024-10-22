#Practicas con numpy
import numpy as np
import sys
import time 
array=np.array([1,2,3,4,5,6])
print(array[2])

#se puede crear un array con datos de diferentes tipos
array2=np.array(["hola",1,2,3,True])
print(array2[0])
#crear matriz  de arrays
array3=np.array([[1,2,3,4,5],[6,7,8,9,8]])
print(array3)

#calculamos el espacio que ocupa una lista vs array
lista=range(1000)
array4=np.array(range(1000))
print(sys.getsizeof(1)*len(lista))
print(array.size*array.itemsize)
# ejemplo de array con un millos de elelmentos
listaa=range(1000000)
listab=range(1000000)

array1=np.array(range(1000000))
array2=np.array(range(1000000))

comienzo1=time.time()
resultado=[x-y for x,y in zip(listaa,listab)]
final1=time.time()

comienzo3=time.time()
resultado2=array1-array2
final3=time.time()
print("tiempo con lista:"+str(final1-comienzo1))
print("tiempo con array:"+str(final3-comienzo3))
#funciones de numpy
resta=np.subtract(array1,array2)
print("resta de arrays=",resta)
suma=np.add(array1, array2) 
print("suma de arrays=",suma)

#Multiplicacion de array
ar1=np.array([4,2,64,81]) 
ar2=np.array([4,5,6, 6])
multi=np.multiply(ar1,ar2)
print(multi)
# division de array
division=np.divide(ar1,ar2)
print(division)
#potencia de los arrays
potencia=np.power(ar1,ar2)
print("potencia de array=", potencia)

#la raiz cuadrada de arrays
raizc=np.sqrt(ar1)
print(raizc)
#maximo comun divisor 
mcd=np.gcd(ar1,ar2)
print(mcd)
#minimo comun multiplo
mcm=np.lcm(ar1,ar2)
print("minimo comun multiplo=",mcm)
#elemento por elemento compara si es mayor que el otro
mayor=np.greater(ar1,ar2)
print(mayor)
#elemnto mayor e igual que 

mayorigual=np.greater_equal(ar1,ar2)
print(mayorigual)
#comprueba si el elemento del array uno es menor que el elemento del array 2
menor=np.less(ar1,ar2)
print(menor)
menor_igual=np.less_equal(ar1,ar2)
print(menor_igual)
igual=np.equal(ar1,ar2)
print("igual=",igual)
#compara si los elementos no son iguales 
no_igual=np.not_equal(ar1,ar2)
print(no_igual)
#Funciones boleanas 
arrayboolena=np.array([False,  True,  True,  True])
arrayboolena1=np.array([True,  True, False, False])

res=np.logical_and(arrayboolena,arrayboolena1)  
print(res)

# or
res1=np.logical_or(arrayboolena,arrayboolena1) 
print(res1)
#xor 
xoor=np.logical_xor(arrayboolena,arrayboolena1) 
print(xoor)
#not
bnot=np.logical_not(arrayboolena,arrayboolena1)
print(bnot) 
#funciones estadisticas de numpy
#amin devuelve los valores estadisticos minimos de un array o una matriz
minimo=np.amin(ar1)
print(minimo)

maximo=np.max(ar1)
print(maximo)
arrayPer=[1,2,3,4,5,6,7,8,9,10]
per=np.percentile(arrayPer,23)
print(per)
#mediana
mediana=np.median(arrayPer)
media=np.mean(arrayPer)
print(mediana)
print(media)
pesos=np.array([1,2,3,4,5,6,7,8,9,10])
pro=np.average(arrayPer,weights=pesos)
print(pro)
desviacionS=np.std(arrayPer)
print(desviacionS)
#varianza
var=np.var(ar1)
print(var)