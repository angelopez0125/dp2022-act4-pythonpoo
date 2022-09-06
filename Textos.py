class Textos:
    
    #Atributos
    texto1= "" 
    texto2= ""
    texto3= ""
    suma= 0
    concatenar= 0 
    cantidad = 0


    def asignarTexto1(self, txt1):
        self.texto1 = txt1

    def asignarTexto2(self, txt2):
        self.texto2 = txt2

    def asignarTexto3(self,txt3):
        self.texto3 = txt3
      
    def calcularPromedio(self):
        self.suma= self.texto1 + self.texto2 + self.texto3
        self.promedio= len(self.suma)/3
        return self.promedio
        return self.suma
        
    def indicarRango(self):
        self.concatenar = len(self.texto1 + self.texto2 + self.texto3)
        if self.concatenar < 15:
           print (self.concatenar, "es menor a 15")
        elif self.concatenar > 15:
           print (self.concatenar, "es mayor a 15")
        else:
           print (self.concatenar, "Es igual a 15")

    def indicarCantidad(self):
        if self.texto1 > self.texto2 and self.texto1 > self.texto3:
            print("El primer texto tiene más caracteres: ")
        elif  self.texto2 >  self.texto1 and  self.texto2 >  self.texto3:
            print("El segundo texto tiene más caracteres: ")
        elif  self.texto3 >  self.texto1 and  self.texto3 >  self.texto2:
            print("El tercer texto tiene más caracteres: ")


    def indicarNumeros(self):
        self.suma =(self.texto1 + self.texto2 + self.texto3)
        print(self.suma)


        

        
