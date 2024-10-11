    #herencia
    # para crear el ejemplo de la herencia, crearemos una clase llamada persona que seria como la clase padre
    #las clases profesor y alumno seran las clases hijas que eredaran los atributos de la clase padre""persona"
class Persona:
        def __init__(self, nombre, fecha_nacimiento,direccion):
            self.nombre=nombre
            self.fecha_nacimiento=fecha_nacimiento
            self.direccion=direccion
            
        def cambiar_domicilio(self,nuevo_domicilio):
            self.nuevo_domicilio=nuevo_domicilio
        def Imprimir(self):
            print("Nombre=",self.nombre,"Fecha de nacimiento=",self.fecha_nacimiento,"Direccion=",self.direccion)    

class Profesor:
    def __init__(self,nombre,fecha_nacimiento,direccion,especialidad):
        Persona.__init__(self,nombre, fecha_nacimiento,direccion)# estamos herdando los atributos de la clase Persona                              
        self.especialidad=especialidad#agregando nuevos atributos
        self.asignaturas_impartidas=[]
                    
    def Asignar_asignatura(self,asignatura):
        self.asignaturas_impartidas.append(asignatura)
    def ImprimirProfesor(self):
        print("Nombre=",self.nombre,"fecha=",self.fecha_nacimiento,"Direccion=",self.direccion,"especialidad=",self.especialidad,"Asignaturas",self.asignaturas_impartidas)
                
            
class Alumno:
    def __init__(self, nombre ,fecha_nacimiento,direccion,asignatura_matriculada):          
            Persona.__init__(self,nombre,fecha_nacimiento,direccion)
            self.asignatura_matriculada=asignatura_matriculada
            self.calificacion=None
            
    def calificar(self,nota):
        self.calificacion=nota
        
    def ImprimirAlumno(self):
        print("Datos del Alumno"+"\n","Nombre=",self.nombre,"Fecha de Naciemiento=",self.fecha_nacimiento,"Asignatura=",self.asignatura_matriculada,"Calificacion=",self.calificacion )  
          
#imprimir los datos de la clase persona 
a=Persona("mayte","01/02/2017","Ambato")
a.Imprimir()


e=Profesor("Johan","01/02/207","Quito","Artificial Inteligence")
e.Asignar_asignatura("Matematicas,Fisica")
e.ImprimirProfesor()

i=Alumno("Naty","01/02/2015","Guayaquil","Machine Learnig")
i.calificar(15)
i.ImprimirAlumno()


    
            
            
                
         
         

        
                