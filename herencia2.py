#herencia2 practica 2
class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    def Imprimirpersona(self):
        print("Nombre=",self.nombre,"Apellido=",self.apellido,"Edad=",self.edad)    
a=Persona("May","Tixilema",12)
a.Imprimirpersona()
#herencia
class Profesor:
    def __init__(self,nombre,apellido,edad,universidad,titulo) :
        Persona.__init__(self,nombre,apellido,edad)
        self.universidad=universidad
        self.titulo=titulo
        self.nota=None
    def Ingresanota(self,nota):
        self.nota=nota
    def ImprimirProfe(self):
        print("Nombre=",self.nombre,"Apellido=",self.apellido,"Edad=",self.edad,"Universidad=",self.universidad,"Titulo=",self.titulo,"Nota=",self.nota)        
e=Profesor("Johan","Galarraga",27,"Ups","Ing.Sistemas")  
e.Ingresanota(95) 
e.ImprimirProfe()     