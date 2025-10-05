import os
os.system("cls")

#clase de Coches sin metodo constructor

class Coches:
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0
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

# objetos de la clase coches

coche1=Coches()
coche2=Coches()

coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
print(f"Los valores del objeto 1 son: {coche1.getMarca},{coche1.getColor}, {coche1.getModelo}, {coche1.getVelocidad}, {coche1.getCaballaje}, {coche1.plazas}")

coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

print(f"Los valores del objeto 2 son: {coche2.marca},{coche2.color}, {coche2.modelo}, {coche2.velocidad}, {coche1.caballaje}, {coche2.plazas}")
