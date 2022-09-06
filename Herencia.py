class Persona:
    def _init_(self,edad):
        self.edad = edad
    
    def hablar(self,mensaje):
        
        print (mensaje)
        
class Ingenieria(Persona):
    def _init_(self):
        print("Hola")
        
    def programar(self,lenguaje):
        print("Voy a programar", lenguaje)
        
class Derecho(Persona):
    def estudiarCaso(self,de):
        print("Debo estudiar el caso de:", de)

mario = Ingenieria(26)
julio = Derecho(27)

mario.programar("Python")
julio.estudiarCaso("Mario")



mario.hablar("Hola")
julio.hablar("Hola, Julio!")
