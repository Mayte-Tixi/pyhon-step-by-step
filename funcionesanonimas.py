#funciones anonimas default
#para crear funciones anonimas dentro de python se utiliza la funcion lambda
#Creando una funcion normal 
def cuadrado (numero):
    resultado=numero**2
    return resultado
res=cuadrado(5)
print('normal',res)

#funcion con el modulo Lambda
cuadrado1=lambda numero:numero**2
res1=cuadrado(6)
print('lambda',res1)

# seleccionar numeros impares de una lista con lambda
a=range(100)
esimpar=lambda numero:numero%2 !=0
print("impar con lambda",list(filter(esimpar,a)))
# seleccionar numeros impares de una lista normal 


lista1=range(100)
impar=[]
for i in lista1:
    if i%2 !=0:
        impar.append(i)
        
print("normal",impar)        
      
    

     

