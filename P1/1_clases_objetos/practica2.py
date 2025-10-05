"Ejercicio Practico #2  Modelar y diagramar en POO"

import os
os.system("cls")

#clase de Coches
class Coches:
    #metodo constructor que inicializa los valores cuando se instancia un objeto de la calse coches
    def __init__(self, color, marca, velocidad):   
        self.__color=color  #atributos del objeto
        self.__marca=marca
        self.__velocidad=velocidad
    #Metodos del objeto
    def acelerar(self, incremento):
        self.__velocidad=self.__velocidad + incremento
        return self.__velocidad
    
    def frenar(self, decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad
    def tocar_claxon(self):
        print ("Piiiii")

#Instanciar o crear objetos de la clase coches

coche1=Coches("Blanco", "Toyota", 220)
coche2=Coches("Amarillo", "Nissan", 180)


print(f"Los valores del objeto 1 son: {coche1.marca},{coche1.__color}, {coche1.__velocidad}")
#acelerar 
print(f"El coche 1 acelera de {coche1._velocidad} a {coche1.acelerar(50)}")
print(f"El coche 2 frena de {coche2.velocidad} a {coche2.frenar(30)}")