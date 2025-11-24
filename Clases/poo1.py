''' Repasamos conceptos:
Una clase es una forma de empaquetar datos y funcionalidad
Cada instancia de una clase recibe el nombre de objeto
Cada objeto tiene sus propios atributos que sirven para guardar su estado.
Los métodos son comunes a todos los objetos y sirven para modifica los atributos (el estado de los objetos)

En python todos los atributos son públicos. No existen atributos privados aunque si una "convención" para
tratar un atributo como privado
'''

# La clase mas simple: un atributo y un método
# self debe de aparecer siempre como primer parámetro en todos
# los métodos que creemos pero luego no lo usamos en las invocaciones
class Perro:
    nombre = "Bobby"

    # Internamente, self es equivalente a this
    def llamar(self):
        return("Ey " + self.nombre + " ¡Ven aquí!")

mascota1 = Perro()
print(mascota1.llamar())

# Añadimos un constructor (con un parámetro por defecto)
class Perro:
    # constructor
    def __init__(self, n="Bobby"):
        self.nombre = n

    def llamar(self):
        return("Ey " + self.nombre + " ¡Ven aquí!")

mascota1 = Perro()
print(mascota1.llamar())

mascota2 = Perro("Sultán")
print(mascota2.llamar())

# como vemos, los atributos son del todo públicos
mascota1.nombre = "Belcebú"
print(mascota1.nombre)
print(mascota2.nombre)

# Añadimos un atributo de clase
class Perro:
    #Los definimos fuera de los métodos
    numPerros = 0

    def __init__(self, n="Bobby"):
        self.nombre = n
        # y los usamos con el nombre de la clase en lugar de self
        Perro.numPerros +=1

    def llamar(self):
        return("Ey " + self.nombre + " ¡Ven aquí!")

    def cuantosPerros(self):
        return(Perro.numPerros)

mascota1 = Perro("Cuchi cuchi")
mascota2 = Perro("Sultán")

print("Tenemos", mascota1.cuantosPerros(), "perros")
print("Tenemos", mascota2.cuantosPerros(), "perros")

# Y también son públicos
print(Perro.numPerros)

# También podemos definir métodos de clase
class Perro:
    numPerros = 0

    def __init__(self, n="Bobby"):
        self.nombre = n
        Perro.numPerros +=1

    def llamar(self):
        return("Ey " + self.nombre + " ¡Ven aquí!")

    # Anteponemos el decorador de clase classmethod
    # y usamos cls en lugar de self o el nomre de la clase
    # desde un método de clase no podemos acceder a los atributos de instancia
    @classmethod
    def cuantosPerros(cls):
        return(cls.numPerros)

mascota1 = Perro("Cuchi cuchi")
mascota2 = Perro("Sultán")

print("Tenemos", mascota1.cuantosPerros(), "perros")
print("Tenemos", mascota2.cuantosPerros(), "perros")
# también podemos llamar al método con el nombre de la clase
print("Tenemos", Perro.cuantosPerros(), "perros")

# Por último, tenemos también la posibilidad de usar métodos estáticos
class Perro:
    numPerros = 0

    def __init__(self, n="Bobby"):
        self.nombre = n
        Perro.numPerros +=1

    def llamar(self):
        return("Ey " + self.nombre + " ¡Ven aquí!")

    @classmethod
    def cuantosPerros(cls):
        return(cls.numPerros)
    # Anteponemos el decorador staticmethod
    # No usamos ni self ni cls
    # No podemos modificar ni atributos de instancia ni de clase
    @staticmethod
    def ladra():
        return("Guau")

mascota1 = Perro("Satanas")
mascota2 = Perro("Sultán")

print(mascota1.ladra())
print(mascota2.ladra())
# también se pueden usar con el nombre de la clase
print(Perro.ladra())

# Por convención, podemos usar un guión bajo para indicar que el atributo o método es protegido
# y dos guiones para indicar que es privado. En este caso se activa una característica
# llamada name mangling (desfiguración de nombres) que sirve para dificultar el acceso
# pero no lo impide
class Perro:
    numPerros = 0

    def __init__(self, sec1, sec2, n="Bobby"):
        self.nombre = n
        Perro.numPerros +=1
        self._secreto = sec1
        self.__secretisimo = sec2

    def llamar(self):
        return("Ey " + self.nombre + " ¡Ven aquí!")

    @classmethod
    def cuantosPerros(cls):
        return(cls.numPerros)

    @staticmethod
    def ladra():
        return("Guau")

mascota1 = Perro("cuchi cuchi", "cariñito")
print(mascota1.nombre)
# este atributo sigue accesible
print(mascota1._secreto)
# esto ya no. Da error
#print(mascota1.__secretisimo)
# pero se puede acceder igualmente así
print(mascota1._Perro__secretisimo)

# Si hacemos esto no da error pero no nos cambia el valor
mascota1.__secretisimo = "Boniterrimo"
print(mascota1._Perro__secretisimo)
# Y nos crea otra variable diferente
print(mascota1.__secretisimo)



# Esta convención sirve igualmente para los métodos y no solo para los atributos

# En python la sobrecargar de funciones no es necesaria por razones obvias
class Perro:
    numPerros = 0

    def __init__(self, n="Bobby"):
        self.nombre = n

    def llamar(self):
        return("Ey " + self.nombre + " ¡Ven aquí!")

    def funcionChorra(self, parametro):
        if isinstance(parametro,int):
            print("Hago algo con un entero")
        elif isinstance(parametro,float):
            print("Hago algo con un número con decimales")
        elif isinstance(parametro,str):
            print("Hago algo con un string")
        else:
            print("Hago algo con otra cosa")

    def funcionChorra2(self, *parametros):
        if len(parametros)==1:
            print("Haz algo con 1 parametro")
        elif len(parametros)==2:
            print("Haz algo con dos parametros")
        else:
            print("Haz algo con", len(parametros), "parametros")

mascota1 = Perro("Leo")
mascota1.funcionChorra(3)
mascota1.funcionChorra(3.3)
mascota1.funcionChorra("Hola")
mascota1.funcionChorra([1,2,3])

mascota1.funcionChorra2(1)
mascota1.funcionChorra2(1, "Hola")
mascota1.funcionChorra2(1, "Hola", [1,2,3])

