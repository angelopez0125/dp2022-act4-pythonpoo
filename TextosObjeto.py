from Textos import Textos

#Instanciar la clase Ejemplo: 
objeto = Textos()


objeto.texto1= input("Ingrese el primer texto: ")
objeto.texto2= input("Ingrese el segundo texto: ")
objeto.texto3= input("Ingrese el tercer texto: ")
print("El promedio de los textos es: ")
print(objeto.calcularPromedio())
print("Los textos concatenados son: ")
objeto.indicarRango()
print("El texto con mas caracteres: ")
objeto.indicarCantidad()
objeto.indicarNumeros()
