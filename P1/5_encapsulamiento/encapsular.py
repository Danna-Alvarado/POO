#Encapsular: es un pilar de la poo que permite indicar cual es la manera de como poder utilizar los atributos y metodos
# de una clase a la hora de usar en objetos o en herencia
import os
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado= "soy un atributo privado"
    
    def __init__(self,color,tamanio,):
        self.__color=color
        self.__tamanio=tamanio
    
    @property
    def color(self):
        return self.__color
    
    color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamanio(self,tamanio):
        self.__tamanio=tamanio

    @tamanio.setter
    def tamanio(self,tamanio):
        self.__tamanio=tamanio
    
    @property
    def atributopublico(self,atributo_publico):
        return self.atributo_publico
    
    @atributopublico.setter
    def atributopublico(self,atributo_publico):
        self.atributo_publico=atributo_publico

    @property
    def atributo_privado(self,atributo_privado):
        return self.__atributo_privado
    
    @atributo_privado.setter
    def atributo_privado(self,atributo_privado):
        self.__atributo_privado=atributo_privado

    @property
    def atributo_protegido(self,_atributo_protegido):
        return self._atributo_protegido
    
    @atributo_protegido.setter
    def atributo_protegido(self,atributo_protegido):
        self._atributo_publico=atributo_protegido



    def getAtributo_Privado(self):
       return  self.__atributo_privado


#utilizar clase

objeto=Clase("Rojo","Grande")
print(objeto.atributopublico)    
print(objeto.__atributo_privado)
print(objeto.getAtributo_Privado())