#* IF
#Nos permite ejecutar un bloque de instrucciones y evaluar el valor boleano que nos devuelve (True or False)
edad=int(input())

if (edad >18 and edad <50):
    if (edad>18 and edad<25):
        print(' hola menor')
    else:
        print('hola mayores')
elif(edad>40 and edad>75):
    if(edad>40 and edad<25):
        print('hola adulto')
    else:
     print('hola muy mayores')              
else:
    print('la edad ingresada es esta fuera del rango')