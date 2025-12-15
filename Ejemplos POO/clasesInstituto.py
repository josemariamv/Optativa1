from abc import ABCMeta

class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, apellidos):
        self._nombre = nombre
        self._apellidos = apellidos

class Profesor(Persona):
    def __init__(self, nombre, apellidos, departamento):
        super().__init__(nombre, apellidos)
        self.__departamento = departamento

class Alumno(Persona):
    def __init__(self, nombre, apellidos, edad):
        super().__init__(nombre, apellidos)
        self.__edad = edad
        if edad < 18:
            self.__menordeEdad = True
        else:
            self.__menordeEdad = False

class Modulo:
    def __init__(self, nombre, curso, horasSemana, optativa):
        self.__nombre = nombre
        self.__curso = curso
        self.__horasSemana = horasSemana
        self.__optativa = optativa

class Ciclo:
    def __init__(self, nombre, grado):
        self.__nombre = nombre
        self.__grado = grado
        self.__modulosPrimero = []
        self.__modulosSegundo = []

class Grupo:
    pass