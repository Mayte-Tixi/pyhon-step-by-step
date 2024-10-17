#Errores y excepciones
s=2
n=6
suma=s+n
array=[]
#nos devuelve un typeError, error de tipo 
# si nos olvidamos colocar correctamente se producira SyntaxError
#cuando no tenemos definido un identificador nos devolvera  /nameError
#si tratamos de ingresar a un aposicion de una lista oarray cuando esta vacio nos dara un index Error
#a cintinuacion se detalla como gestionar estos typos de errores.
try:
 print(suma)
 #array[0]
except IndentationError:
 print('    Index Error')
except NameError:
 print('    Name Error')
except TypeError :
    print('    Type Error')   
else: 
   print('No existe errores ')  
finally:
     print('igualmente me ejecuto')  
          