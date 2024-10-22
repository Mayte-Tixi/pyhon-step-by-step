#compresion de listas
list=[]
for i in range(1,11):
    list.append(i**2)
print(list)    
#realizando la misma operacion con comprension de listas
list2=[]
list2=[i**2 for i in range(1,11) if i>5]
print(list2)

lista3={"clave"+str(i):i**2 for i in range(1,11) if i>2}
print(lista3)

conjunto={i**2 for i in range(1,11) if i>5}
print(conjunto)
