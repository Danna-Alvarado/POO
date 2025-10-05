import os
os.system("cls")

#clase de Coches sin metodo constructor

class Coches:
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0
    #Metodos del objeto 
    def acelerar(self):
        pass
    def frenar(self):
        pass
    

#objetos de la clase coches
coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo=2022
coche1.velocidad=230
coche1.caballaje=150
coche1.plazas=5
print(f"Los valores del objeto 1 son: {coche1.marca},{coche1.color}, {coche1.modelo}, {coche1.velocidad}, {coche1.caballaje}, {coche1.plazas}")
coche2=Coches()
coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo=2020
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(f"Los valores del objeto 2 son: {coche2.marca},{coche2.color}, {coche2.modelo}, {coche2.velocidad}, {coche1.caballaje}, {coche2.plazas}")