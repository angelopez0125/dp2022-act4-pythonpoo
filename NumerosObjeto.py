from Numeros import Numeros

#Instanciar la clase:

objeto = Numeros()

objeto.numero = int(input("Ingrese un número para calcular un factorial: "))
print(objeto.calcularFactorial())
print(objeto.calcularPrimo())
print(objeto.calcularPerfecto())
print(objeto.calcularBinario())