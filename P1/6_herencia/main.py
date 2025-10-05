#Instanciar objetos para posterior implementarlos
#from coches import Coches

from coches import Coches, Camionetas, Camiones

coche=Coches("WV", "Blanco", "2022", 220, 150, 5)
camioneta=Camionetas("Ford", "Rojo", "2021", 200, 180, 5, "1000kg", "4x4", False)
camion=Camiones("Volvo", "Azul", "2020", 160, 300, 2, 4, "5000kg")
print(coche._marca)
print(camioneta._marca)
print(camion._marca)

num_coches=int(input("¿Cuántos coches deseas?"))

for i in range (0, num_coches):
    print(f"\n\t ....datos del coche.... "(i+1))
marca=input("Ingresa la marca").upper()
color=input("Ingresa el color").upper()
modelo=input("Ingresa el modelo").upper()
velocidad=int(input("Ingresa la velocidad")).upper()
potencia=int(input("Ingresa la potencia")).upper()
plazas=int(input("Ingresa las plazas")).upper()

coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)



'''coche1=Coches("VW","Blanco","2022",220,150,5, "HSGDG")
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda")


print(f"Los valores del objeto 1 son: {coche1.getMarca},{coche1.getColor}, {coche1.getModelo}, {coche1.getVelocidad}, {coche1.getCaballaje}, {coche1.plazas}")
print(f"coche 3 marca: {coche3.marca}")
print(f"Los valores del objeto 2 son: {coche2.marca},{coche2.color}, {coche2.modelo}, {coche2.velocidad}, {coche1.caballaje}, {coche2.plazas}")'''