import os
os.system("cls")

class Profesores:
    def __int__(self,nombre,experiencia,num_profesor):
        self._nombre=nombre
        self._experiencia=experiencia
        self._num_profesor=num_profesor

    #metodos
    def impartir(self):
        pass
    def evaluar(self):
        pass

class Alumnos:
    def __init__(self,nombre,edad,matricula):
        self._nombre=nombre
        self._edad=edad
        self._matricula=matricula


    #metodos
    def inscribirse(self):
        pass
    def estudiar(self):
        pass

class Cursos:
    def __init__(self,nombre,codigo,creditos):
        self._nombre=nombre
        self._codigo=codigo
        self._creditos=creditos
    
    #metodods
    def asignar(self):
        pass
#objetos
profesor1=Profesores("Ana Torres guzman", 40, 123)
profesor2=Profesores("Daniel Contreras", 35, 456)

alumnno1=Alumnos("Juan Correa Simental",25, 100123)
alumno2=Alumnos("Maria Serrano Mata", 22, 100124)

curso1=Cursos("POO", 100, 6)
curso2=Cursos("FOSO", 101, 4)

print(f"Alumno 1: {alumnno1._nombre}, edad: {alumnno1._edad}, matricula: {alumnno1._matricula}")