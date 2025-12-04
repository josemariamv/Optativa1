# Así importamos la clase Pokemon del archivo pokemon.py.
# Atento: es sensible a minúsculas y minúsculas en cuanto al nombre del fichero y de la clase
# No hay que poner la extensión al nombre del archivo
from pokemon import Pokemon, Equipo

# Otras opciones
# from pokemon import *
# import pokemon
# en este caso cuando creemos un objeto nuevo tenemos que añadirle el prefijo:
# p1 = pokemon.Pokemon("Bulbasaur")

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

equipo1 = Equipo("José María Morales", p4, p1)
equipo2 = Equipo("José María Morales", p3)