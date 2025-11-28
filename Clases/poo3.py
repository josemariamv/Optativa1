# herencia simple
class Animal:
    def __init__(self, especie, extinto=False):
        self.especie = especie
        self.extinto = extinto

    def sonido(self):
        print("Pssssssst")

    def patas(self):
        self.patas = 4


class Mamifero(Animal):
    # si sobrescribimos un método sustituye al de la clase padre
    # si no lo hacemos la clase hija hereda al método de la clase padre
    def sonido(self):
        print("Brrrrrr")

class Reptil(Animal):
    #si queremos sobreescribir un método pero reutilizar también el de la clase padre
    # usamos super()
    def __init__(self, especie, domestico, extinto="False"):
        super().__init__(especie, extinto)
        self.domestico = domestico

    def patas(self, patas):
        if patas!=4:
            self.patas = patas
        else:
            super().patas()


mamifero1 = Mamifero("Mamut", True)
reptil1 = Reptil("Anaconda", False)
reptil2 = Reptil("Gecko Leopardo", True)
reptil1.sonido()
mamifero1.sonido()
reptil1.patas(0)
reptil2.patas(4)

print(reptil1.patas)
print(reptil2.patas)


# herencia multiple
class Persona:
    def queSoy(self):
        print("soy una persona")

    def queSoy2(self):
        print("soy una persona")

class Funcionario():
    def queSoy(self):
        print("soy un funcionario")

    def queSoy2(self):
        print("soy un funcionario")

class Profesor(Persona, Funcionario):
    def queSoy2(self):
        super().queSoy2()
        Funcionario.queSoy2(self)

    def queSoy3(self):
        Persona.queSoy2(self)
        print("y además")
        Funcionario.queSoy2(self)

profesor1 = Profesor()
# se llama al primer método definido, si no en la clase en las clases de las que hereda
# empezando por la izquierda. Cambia el orden de las clases padre y lo comprobaras
profesor1.queSoy()
# si quiero otra cosa tengo que redefinir el método
profesor1.queSoy2()

profesor1.queSoy3()

class Loquesea:
    # Pycharm no genera automaticamente getters y setters pero tiene los siguientes atajos:
    # prop e Intro genera la plantilla del getter
    # props e Intro genera la plantilla del getter y el setter
    '''
    @property
    def (self):
        return

    @.setter
    def (self, value):
        pass
    '''

# clases abstractas, aquellas que tienen algún método abstracto
from abc import ABCMeta
from abc import abstractmethod

class Abstracta(metaclass=ABCMeta):
    def metodoNormal(self, dato):
        print(dato)

    @abstractmethod
    def metodoAbstracto(self):
        pass
#esto da error
# nuevo = Abstracta()
# nuevo.metodoNormal("Esto no funciona")

class Hija(Abstracta):
    def metodoAbstracto(self):
        print("funciona")

nuevo2 = Hija()
nuevo2.metodoNormal("Esto si funciona")

# El decorador @abstracmethod puede combinarse con cualquier de los otros vistos. Se ponen uno bajo el otro:

# @staticmethod
# @abstractmethod
# def ladra():
#     return ("Guau")
