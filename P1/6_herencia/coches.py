import os
os.system("cls")

#clase de Coches sin metodo constructor

class Coches:
#metodo constructor-- con este metodo se inicializan un objeto cuando es creado con valores iniciales

  def __init__(self):
    self._marca=""
    self._color=""
    self._modelo=""
    self._velocidad=0
    self._caballaje=0
    self._plazas=0
    #Metodos del objeto 
    

#metodo get y set

    @property
    def marca(self):
       return self._marca
    @marca.setter
    def marca(self,marca):
       self._marca=marca
    
    @property
    def color(self):
       return self._color
    @color.setter
    def color(self,color):
      self._color=color
@property
def modelo(self):
    return self._modelo
@modelo.setter
def modelo(self,modelo):
    self._modelo=modelo
@property
def velocidad(self):
    return self._velocidad
@velocidad.setter
def velocidad(self,velocidad):
    self._velocidad=velocidad
@property
def caballaje(self):
    return self._caballaje
@caballaje.setter
def caballaje(self,caballaje):
    self._caballaje=caballaje
@property
def plazas(self):
    return self._plazas
@plazas.setter
def plazas(self,plazas):
    self._plazas=plazas


coche1=Coches("VW","Blanco","2022",220,150,5, "HSGDG")
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda")


print(f"Los valores del objeto 1 son: {coche1.getMarca},{coche1.getColor}, {coche1.getModelo}, {coche1.getVelocidad}, {coche1.getCaballaje}, {coche1.plazas}")
print(f"coche 3 marca: {coche3.marca}")
print(f"Los valores del objeto 2 son: {coche2.marca},{coche2.color}, {coche2.modelo}, {coche2.velocidad}, {coche1.caballaje}, {coche2.plazas}")

   
class Camiones(Coches):
   def _init_(self,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
      super()._init_(marca,color,modelo,velocidad,caballaje,plazas)
      self.__eje=eje
      self.__capacidadCarga=capacidadCarga
      
      #metodos set y get
      @property
      def eje(self):
         return self.__eje
      
      @eje.setter
      def eje(slef,eje):
         self.__eje=eje

      @property
      def capacidadCarga(self):
         return self.__capacidadCarga
      
      @capacidadCarga.setter
      def capacidadCarga(slef,capacidadaCarga):
         self.__capacidadCarga=capacidadCarga

    #metodos
      def cargar(self,tipo_carga):
         self.__tipo_carga=tipo_carga
         return self.__tipo_carga

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,  traccion, cerrada):
      super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
      self.__traccion = traccion
      self.__cerrada = cerrada
    
    @property
    def traccion(self):
       return self.__traccion
    @traccion.setter
    def traccion(self, traccion):
       self.__traccion = traccion

    @property
    def cerrada(self):
       return self.__cerrada
    @cerrada.setter
    def cerrada(self, cerrada):
       self.__cerrada = cerrada
    
    @property
    def traccion(self):
       return self.__traccion
    @traccion.setter
    def traccion(self, traccion):
       self.__traccion = traccion
    
    @property
    def traccion(self):
       return self.__traccion
    @traccion.setter
    def traccion(self, traccion):
       self.__traccion = traccion