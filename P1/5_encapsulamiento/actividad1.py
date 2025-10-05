import os
os.system("cls")

class Alumnos:
    nombre = ""
    edad = 0
    matricula = ""

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad

    def getMatricula(self):
        return self.matricula
    def setMatricula(self, matricula):
        self.matricula = matricula

    def inscribirse(self):
        print(f"El alumno {self.nombre} se ha inscrito.")

    def estudiar(self):
        print(f"El alumno {self.nombre} está estudiando.")

class Profesores:
    nombre = ""
    experiencia = 0
    num_profesor = 0

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getExperiencia(self):
        return self.experiencia
    def setExperiencia(self, experiencia):
        self.experiencia = experiencia

    def getNumProfesor(self):
        return self.num_profesor
    def setNumProfesor(self, num_profesor):
        self.num_profesor = num_profesor

    def impartir(self):
        print(f"El profesor {self.nombre} está impartiendo clase.")

    def evaluar(self):
        print(f"El profesor {self.nombre} está evaluando.")

class Cursos:
    nombre = ""
    codigo = 0
    creditos = 0

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getCodigo(self):
        return self.codigo
    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCreditos(self):
        return self.creditos
    def setCreditos(self, creditos):
        self.creditos = creditos

    def asignar(self):
        print(f"El curso {self.nombre} fue asignado.")


# Alumnos
alumno1 = Alumnos()
alumno1.setNombre("Juan Correa")
alumno1.setEdad(25)
alumno1.setMatricula("100123")

alumno2 = Alumnos()
alumno2.setNombre("Maria")
alumno2.setEdad(22)
alumno2.setMatricula("1001234")

print(f"Datos del Alumno:\n Nombre: {alumno1.getNombre()} \n Edad: {alumno1.getEdad()} \n Matrícula: {alumno1.getMatricula()}")
print(f"Datos del Alumno:\n Nombre: {alumno2.getNombre()} \n Edad: {alumno2.getEdad()} \n Matrícula: {alumno2.getMatricula()}")

# Profesores
profesor1 = Profesores()
profesor1.setNombre("Ana Torres Guzman")
profesor1.setExperiencia(40)
profesor1.setNumProfesor(123)

profesor2 = Profesores()
profesor2.setNombre("Daniel Contreras")
profesor2.setExperiencia(35)
profesor2.setNumProfesor(456)

print(f"Datos del Profesor:\n Nombre: {profesor1.getNombre()} \n Experiencia: {profesor1.getExperiencia()} \n Número: {profesor1.getNumProfesor()}")
print(f"Datos del Profesor:\n Nombre: {profesor2.getNombre()} \n Experiencia: {profesor2.getExperiencia()} \n Número: {profesor2.getNumProfesor()}")

# Cursos
curso1 = Cursos()
curso1.setNombre("POO")
curso1.setCodigo(100)
curso1.setCreditos(6)

curso2 = Cursos()
curso2.setNombre("FOSO")
curso2.setCodigo(101)
curso2.setCreditos(4)

print(f"Datos del Curso:\n Nombre: {curso1.getNombre()} \n Código: {curso1.getCodigo()} \n Créditos: {curso1.getCreditos()}")
print(f"Datos del Curso:\n Nombre: {curso2.getNombre()} \n Código: {curso2.getCodigo()} \n Créditos: {curso2.getCreditos()}")

# Probar métodos
alumno1.estudiar()
profesor1.impartir()
curso1.asignar()