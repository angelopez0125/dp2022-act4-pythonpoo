class Salarios:
    #Atributos
    
    sueldobase= 0
    ventas = 0
    igss = 0
    ahorro = 0
    datos = 0
    datos2= 0
    tganado = 0
    descuentos = 0
    sueldoliquido = 0
    
    #Métodos
    
    def calcularComisiones(self):
        self.datos = (self.ventas * 0.10)
        return self.datos
    
    def calcularIgss(self):
        self.igss = (self.sueldobase * 0.0483)
        return self.igss
    
    def calcularAhorro(self):
        self.ahorro = (self.datos + self.sueldobase) 
        self.datos2 = (self.ahorro * 0.07)
        return self.datos2
    
    def calcularTganado(self):
        self.tganado = (self.datos + self.sueldobase + 250)
        return self.tganado
    
    def calcularDescuentos(self):
        self.descuentos = (self.datos2 + self.igss)
        return self.descuentos
    
    def calcularSliquido(self):
        self.sueldoliquido = (self.tganado - self.descuentos)
        return self.sueldoliquido
