# un decorador en python es una función que "envuelve" a otra función proporcionándole una funcionalidad extra
# se definen poniendo una arroba y luego el nombre del decorador

def mi_decorador(funcion):
    def envoltorio():
        print("Antes del saludo")
        funcion()
        print("Después del saludo")
    return envoltorio

@mi_decorador
def saludar():
    print("¡Hola, mundo!")

saludar()

# python tiene de serie muchos decoradores muy útiles. Algunos de ellos los hemos visto en este tema:
# @property, @classmethod, @staticmethod, etc.

# Un ejemplo con herencia múltiple y un decorador en un método de clase
class Persona():
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

class Funcionario():
    def __init__(self, cuerpo):
        self._cuerpo = cuerpo

class Profesor(Persona, Funcionario):
    def __init__(self, nombre, apellido, cuerpo):
        super().__init__(nombre, apellido)
        Funcionario.__init__(self, cuerpo)

    def __str__(self):
        return self._apellido + ", " + self._nombre + "(" + self._cuerpo + ")"

    def mi_decorador(funcion):
        def envoltorio(self):
            print("Buenos días al cuerpo de", self._cuerpo)
            funcion(self)
            print("Qué tengas un buen día")
        return envoltorio

    @mi_decorador
    def saludo(self):
        print("Hola ", self._nombre)

profe = Profesor("José María", "Morales", "Educación")
print(profe)
profe.saludo()