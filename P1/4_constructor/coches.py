import os
os.system("cls")

#clase de Coches sin metodo constructor

class Coches:
#metodo constructor-- con este metodo se inicializan un objeto cuando es creado con valores iniciales

  def __init__(self):
    self.__marca=""
    self.__color=""
    self.__modelo=""
    self.__velocidad=0
    self.__caballaje=0
    self.__plazas=0
    #Metodos del objeto 
    def acelerar(self):
        pass
    def frenar(self):
        pass
    
#Crear los metodos setters y getters -estos son importantes y necesarios en todas las clases para que el programador
# interactue con los valores de los atributos a traves de estos metodos..... digamos que es la manera mas adecuada
# y recomendada para solocitar un valor(get) y /o para ingresar o cambiar un valor(set) a un atributo en particular de la clase se 

#1ra forma 
def getMarca(self):
    return self.__marca

def setMarca(self,marca):
    self.__marca=marca
#segunda forma

@property
def marca(self):
    return self.__marca
@marca.setter
def marca(self,marca):
    self.__marca=marca
    

def getColor(self):
    return self.__color

def setColor(self,color):
    self.__color=color

def getModelo(self):
    return self.__modelo

def setModelo(self,modelo):
    self.__modelo=modelo

def getVelocidad(self):
    return self.__velocidad

def setVelocidad(self,velocidad):
    self.__velocidad=velocidad

def getCaballaje(self):
    return self.__caballaje

def setCaballaje(self,caballaje):
    self.__caballaje=caballaje

def getPlazas(self):
    return self.__plazas

def setPlazas(self,plazas):
    self.__plazas=plazas

# Crear un objeto o instanciar la clase

#Multiples objetos
coche1=Coches("VW","Blanco","2022",220,150,5, "HSGDG")
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda")


print(f"Los valores del objeto 1 son: {coche1.getMarca},{coche1.getColor}, {coche1.getModelo}, {coche1.getVelocidad}, {coche1.getCaballaje}, {coche1.plazas}")


print(f"coche 3 marca: {coche3.marca}")
print(f"Los valores del objeto 2 son: {coche2.marca},{coche2.color}, {coche2.modelo}, {coche2.velocidad}, {coche1.caballaje}, {coche2.plazas}")
