#moduloRandom
import random
#proporciona metodos para obtener valores aleatorios
numero=random.randint(1,10)#proporciona valores aleatorio entre dos numeros
objeto=random.choice(['perro','gallina',1,2,3])#selecciona de manera aleatoria los valores de una lista
lista=[1,2,3,4,5,6,7,8,9,10]
lista1=['hola','yo','puedo','soy','inteligente']
random.shuffle(lista1)#cambia de orden de manera aleatoria
retorna=random.sample(lista,4)#devuelve # de valores de una lista
print(retorna)