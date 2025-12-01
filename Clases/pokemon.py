import random


class Pokemon:
    def __init__(self, nombre):
        self.__nombre__ = nombre
        self.__evolucion__ = None
        self.__pv__ = random.randint(50,100)

    def mostrar(self):
        print(self.__nombre__, "-", self.__pv__)

    def setEvolucion(self, pokemon):
        self.__evolucion__ = pokemon

    def evoluciona(self):
        if self.__evolucion__ == None:
            print("Este pokemon no tiene evolucion")
            devolver = self
        else:
            devolver = self.__evolucion__
            devolver.__pv__ += self.__pv__
        return devolver

    def combateContra(self, pokemon):
        danno = random.randint(25,75)
        pokemon.__pv__ -=danno;
        if pokemon.__pv__ <=0:
            print(pokemon.__nombre__, "ha sido derrotado")
        else:
            danno = random.randint(25,75)
            self.__pv__ -=danno;
            if self.__pv__ <=0:
                print(self.__nombre__, "ha sido derrotado")
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