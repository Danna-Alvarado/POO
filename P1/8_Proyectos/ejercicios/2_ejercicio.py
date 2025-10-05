"Realizar u  programa en el cual se declaren dos valores enteros por teclado utilizando el metodo __init__ Calcular"
"despúes la suma, resta, multiplicación y división. Utilizar un metodo para cada una e imprimir los resultados"

'''numero1= int(input("Ingrese el primer numero"))
numero2= int(input("Ingrese el primer numero"))

class Calculadora:
    def __init__ (self, numero1, numero2):

    def suma(self, numero1, numero2):
        suma=numero1+numero2
        return suma
    
    def resta(self, numero1, numero2):
        resta=numero1-numero2
        return resta
    def multiplicacion(self, numero1, numero2):
        multiplicacion=numero1*numero2
        return multiplicacion
    
    def dividion(self, numero1, numero2):
        division=numero1/numero2
        return division


print(f"Los resultados son : {suma}, {resta}, {multiplicacion}, {divison}")'''


class Calculadora:
    def __init__(self ):
        self._numero1= int(input("Numero1:"))
        self._numero2= int(input("Numero2:"))

    @property
    def numero1(self):
        return self._numero1
    @numero1.setter
    def numero1(self):
        self._numero1
    @property
    def numero2(self):
        return self._numero2
    @numero2.setter
    def numero2(self):
        self._numero2

    
        
    
    def suma(self):
        return self._numero1+self._numero2
    
    def resta(self):
        return self._numero1-self._numero2
    
    def multiplicacion(self):
        return self._numero1*self._numero2
    
    def division(self):
        return self._numero1/self._numero2

operacion=Calculadora()
print(f" {operacion._numero1}+ {operacion._numero2}={operacion.suma()}")
print(f" {operacion._numero1}- {operacion._numero2}={operacion.resta()}")
print(f" {operacion._numero1}* {operacion._numero2}={operacion.multiplicacion()}")
print(f" {operacion._numero1}/ {operacion._numero2}={operacion.division()}")