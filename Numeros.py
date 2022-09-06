from math import factorial


class Numeros:
    
    #Atributos
    
    numero = 0
    x = 1
    c = 0
    suma = 0
    total = 0
    bin = 0
    bina = 0

    
    
    #Métodos 
    def calcularFactorial(self):
     if (self.numero==0):
        return 1
     else:
        return self.numero * factorial(self.numero - 1)
    
    def calcularPrimo(self):
        while self.x <= self.numero:
            if self.numero % self.x == 0:
                self.c = self.c + 1
            self.x = self.x + 1
        if self.c == 2:
            print("El número es primo")
        else:
            print("El numero no es primo")
            
    def calcularPerfecto(self):
       for self.total in range(1,self.numero):
           if (self.numero % (self.total) == 0):
               self.suma += (self.total)
               
           if self.numero == self.suma:
               return "Es perfecto"
           else:
            return "No es perfecto"
        
    def calcularBinario(self):
        self.bin= self.numero
        self.bina= int(bin(25)[2:])
        return self.bina
        
        
            
            

           
           
           
           