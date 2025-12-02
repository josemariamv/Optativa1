import random

class Pokemon:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__evolucion = None
        self.__pv = random.randint(50,100)

    def mostrar(self):
        print(self.__nombre, "-", self.__pv)

    def setEvolucion(self, pokemon):
        self.__evolucion = pokemon

    def evoluciona(self):
        if self.__evolucion == None:
            print("Este pokemon no tiene evolucion")
            devolver = self
        else:
            devolver = self.__evolucion
            devolver.__pv += self.__pv
        return devolver

    def combateContra(self, pokemon):
        danno = random.randint(25,75)
        pokemon.__pv -=danno;
        if pokemon.__pv <=0:
            print(pokemon.__nombre, "ha sido derrotado")
        else:
            danno = random.randint(25,75)
            self.__pv -=danno;
            if self.__pv <=0:
                print(self.__nombre, "ha sido derrotado")
            else:
                print("El combate no ha concluido con la victoria de ninguno")

p1 = Pokemon("Bulbasaur")
p2 = Pokemon("Venasaur")
p3 = Pokemon("Ivysaur")
p4 = Pokemon("Pikachu")

p1.setEvolucion(p2)
p2.setEvolucion(p3)

p1.mostrar()

p1 = p1.evoluciona()
p1.mostrar()

p1=p1.evoluciona()
p1.mostrar()

p1=p1.evoluciona()
p1.mostrar()

p4.combateContra(p1)
p4.mostrar()
p1.mostrar()
p4.combateContra(p1)