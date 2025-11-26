class CuentaCorriente:
    def __init__(self, iban, propietario, saldoInicial=0):
        self.iban = iban
        self.propietario = propietario
        self.__saldo = saldoInicial
    # el decorador property nos permite definir un método que se comporta como un atributo
    @property
    def saldo(self):
        return self.__saldo
    # para modificar una propiedad definida de esta forma definimos método con el decorador setter
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

cuenta1 = CuentaCorriente("ES3212345678901234567890", "José María Morales", 1200.00)
print(cuenta1.saldo)
# esto da error
#print(cuenta1.saldo())

# parece que no tiene mucho sentido? Pues es una de las pocas formas que
# tenemos de proteger de modificaciones directas un atributo. Esto también da error
# salvo que definamos un setter
# cuenta1.saldo = 10000000.00
# print(cuenta1.saldo)

# Una ventaja de esta falta de protección es que podemos usar una clase como un registro o record
# un tipo de dato existente en Pascal o en C y que es muy útil. Y ni siquiera necesitamos un
# constructor si no lo queremos

class Empleado:
    pass

empleado1 = Empleado()
empleado1.nombre = "José María"
empleado1.apellidos = "Morales Vázquez"
empleado1.edad = 57
empleado1.activo = True

print(empleado1.nombre)
del empleado1.nombre
# Con del podemos borrar un atributo. Las referencias sucesivas darán error
#print(empleado1.nombre)

# Y también, por supuesto un objeto. del llama al destructor de la clase
#del empleado1
#print(empleado1.apellidos)

# por cierto: del se puede usar con cualquier dato también
# num1 = 5
# del num1
# print(num1)

# Los métodos mágicos o métodos dunder (double underscore) nos permiten redefinir en nuestras clases algunos de los métodos comunes
# de python que funcionan con todos los tipos de datos comunes vistos

class Prueba():
    def __len__(self):
        return 20

    def __count__(self):
        return 1

prueba1 = Prueba()
print(len(prueba1))

''' Los métodos mágicos mas comunes que puedo definir son
__init__(self, ...): Se ejecuta al crear una nueva instancia de la clase para inicializar sus atributos.
__del__(self): El destructor. Se llama cuando la instancia está a punto de ser destruida (eliminada de la memoria).

__str__(self): Devuelve una representación legible de la instancia para el usuario, utilizada por print().
__len__(self): Permite que la función len() funcione con tus objetos.

__add__(self, other): Implementa el comportamiento para el operador + (suma).
__sub__(self, other): Implementa el comportamiento para el operador - (resta).
__mul__(self, other): Implementa el comportamiento para el operador * (multiplicación).
__truediv__(self, other): Implementa el comportamiento para el operador / (división real). 

__eq__(self, other): Implementa el comportamiento para el operador == (igualdad).
__ne__(self, other): Implementa el comportamiento para el operador != (desigualdad).
__lt__(self, other): Implementa el comportamiento para el operador < (menor que).
__gt__(self, other): Implementa el comportamiento para el operador > (mayor que).

__iter__(self) y __next__(self): Permiten crear un iterador para el objeto, permitiendo su uso en bucles for
'''
class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return self.apellidos+", "+ self.nombre

persona1 = Persona("José María", "Morales Vázquez")
print(str(persona1))

class Cuentas:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular =[]
        self.titular.append(titular)

    def __add__ (self, c2):
        self.saldo = self.saldo + c2.saldo
        self.titular = self.titular + c2.titular
        return self

    def __gt__ (self, c2):
        mayor = True
        if self.saldo <= c2.saldo:
            mayor = False
        return mayor

libreta1 = Cuentas(1234.55, "José María Morales")
libreta2 = Cuentas(345.66, "María Rodríguez")

print(libreta1.titular)
libreta1 = libreta1 + libreta2
print(libreta1.saldo)
print(libreta1.titular)

if libreta1 > libreta2:
    print("El saldo de libreta1 es mayor")

