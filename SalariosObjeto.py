from Salarios import Salarios

#Instanciar la clase:

valores = Salarios()

valores.sueldobase = float(input("Ingrese el sueldo base: "))
valores.ventas = float(input("Ingrese la cantidad de ventas: "))
print("La comisión de las ventas es: ")
print(valores.calcularComisiones())
print("El Igss es: ")
print(valores.calcularIgss())
print("El ahorro del 7 por cierto es: ")
print(valores.calcularAhorro())
print("El total ganado es: ")
print(valores.calcularTganado())
print("El total de descuentos es: ")
print(valores.calcularDescuentos())
print("El sueldo liquido es: ")
print(valores.calcularSliquido())