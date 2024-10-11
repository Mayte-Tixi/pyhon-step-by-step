#Programacion Orientado a Objetos
#Es una paradigma de programacion en el que se encapsulan los datos en forma de objetos. se define como un conjuntos de funciones que se 
#encuentran almacenados en ese objetos.

class Libro:
     titulo="Don quijote de la mancha"
     autor="Miguel servantes"
     isbn="0987-7489"
     editorial=" El editorial"
     paginas=987
     edicion=84
     
     def editar_edicion(self,sumaedicio):
          self.edicion +=sumaedicio
          print("Ediccion=", self.edicion)
     
milibro=Libro()  #estamos formando un objaeto   

milibro.editar_edicion(5)
