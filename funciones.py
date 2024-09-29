#funciones
#Creando funciones sin parametros
def funcion():
    return("hola mucndo")
    
print(funcion())

#creando funciones con parametros 
def cuadrado(numero,cuad):
    return(numero**cuad) 
#main
print(cuadrado(5,2))

def funciion2(*args):# para indicar que la funcion tiene varios argumentos
 resultado=0
 for i in args:
        resultado+=i
 return(resultado)
        
print(funciion2(1,8,3,4,5))        

def funcion2(**args):# para indicar que la funcion va ingresar varios argumentos
 for argumentos in args:
    print(argumentos,"->",args[argumentos])    
    
     
print(funcion2(args1=1,args2=20,args3=40))      