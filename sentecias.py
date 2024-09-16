#sentecnias while
#para utilizar la sentencia debemos crear un contador 
numero=5
contador=0
while(contador<5):
    contador+=1
    print('contador',contador)
else:
    print('fin')
    
    #For
    lista=['gato','perro','conejo']
    for var in lista:
        print(var)
    else:
        print('fin')  
          
    #funcion rang
    cadena='hola mundo'
    #imprime cadena de texto desde posicion 0 cada pisicion 2
    for caracter in range(0,len(cadena),2):
            print(cadena[caracter])
            
#sentencia break, rompe el ciclo de un bucle
            
    cadena='hola mundo'
    for var1 in cadena:
        print("break",var1)
        if var1==" ":
            break
#sentecnia continue
    cadena1='hola mundo'
    for var2 in cadena1:
        if var2==" ":
            continue   
        print("continue",var2)
  #iterador
    cadena2='hola mundo'
    iterador=iter(cadena2)
    for  car in range(0,len(cadena2)): 
        print(cadena2[car])   
#crear un bucle dentro del bucle

cade='soy inteligente'
for i in range(0,3): # repite 3 veces 
   for vr in cade:
     print(vr)
     
        