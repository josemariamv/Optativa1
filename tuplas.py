# Tuplas: muy similares a las listas
# También admiten elementos duplicados y heterogeneos
# Sus elementos guardan un orden, pero no se pueden modificar. Son inmutables
# Similares en esto a las cadenas de texto

# crea una tupla
tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = ("rojo", "verde", "azul")
tupla3 = ("José María", "Morales", "Vazquez", 8, 10, 1968, "Informática", True)
# así también
tupla4 = 4,5,6
print(tupla4)
# creamos una tupla vacía. Recuerda que no la puedes modificar luego...
tupla5=()
print(tupla5)
# importante: una tupla de un único elemento se define así, con la coma final
tupla6 = ("Sevilla",)
print(tupla6)
# si no, no es una tupla
tupla7 = ("Madrid")
print(tupla7)

# convierte una lista en una tupla
tupla8 = tuple([4,5,6])
print(tupla8)
# o una cadena
tupla9 = tuple("Hola Mundo")
print(tupla9)

# Puedo anidar tuplas de forma jerárquica así:
tupla10 = 13,14,tupla8,tupla4, 33
print(tupla10)

# si intentamos modificarla de cualquier forma nos dará una excepción
#tupla8[0] = 5

# Todos los métodos y opciones que funcionan en las listas y que no las
# modifican funcionan también en las tuplas
# (recorridos, emparedados, len, count, index, etc.)







