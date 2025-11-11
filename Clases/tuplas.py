# Tuplas: muy similares a las listas
# También admiten elementos duplicados y heterogeneos
# Sus elementos guardan un orden, pero no se pueden modificar. Son inmutables
# Similares en esto a las cadenas de texto

# crea una tupla
tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = ("rojo", "verde", "azul")
tupla3 = ("José María", "Morales", "Vazquez", 8, 10, 1968, "Informática", [1,2,3], True)
print(tupla3)
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

# Y una tupla en una lista o en una cadena
lista = list(tupla8)
print(lista)
texto = str(tupla8)
print(texto)

# Puedo anidar tuplas de forma jerárquica así:
tupla10 = 13,14,tupla8,tupla4, 33
print(tupla10)

# si intentamos modificarla de cualquier forma nos dará una excepción
#tupla8[0] = 5

# pero si puedo modificar una lista dentro de una tupla.
print(tupla3)
print(tupla3[7])
tupla3[7][1] = 333
print(tupla3)

# Todos los métodos y opciones que funcionan en las listas y que no las
# modifican funcionan también en las tuplas
# (recorridos, emparedados, len, count, index, etc.)

# devuelve la posición en la que se encuentra el elemento del argumento
# si hay mas de uno devuelve la posición del primero
tupla11 = (6, 7, 1, 4, 2, 4, 5, 6, 1)
print(tupla11.index(1))
# Si no está en la tupla da error
# print(tupla11.index(3))

if 7 in tupla11:
    print("Está en la tupla")

if 33 not in tupla11:
    print("No está en la tupla")

# recorridos
#Sin obtener la posición
for elemento in tupla11:
    print(elemento)

# Con la posición del elemento
for i in range(len(tupla11)):
    print(i, "-", tupla11[i])

# Devuelve cuantas veces aparece el elelento del argumento
print(tupla11.count(1))
print(tupla11.count(3))

# Podemos usar la sintaxis del emparedado:
tupla12 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tupla12[3])
print(tupla12[3:6])
print(tupla12[:3])
print(tupla12[:6])
print(tupla12[::-1])

#Podemos asignar a n variables los elementos de una tupla de n elementos
profesor = ("José María", "Morales Vázquez", 57)
nombre, apellidos, edad = profesor
print(apellidos, ",", nombre, "-", edad, "años")

# Los métodos de random también funcionan con tuplas
import random
alumnos = ("María", "Pepe", "Juan", "Antonio")
#elige un elemento al azar
print(random.choice(alumnos))
#elige tres elementos al azar sin repetición
print(random.sample(alumnos, 3))
# salvo shuffle que la modifica!
#random.shuffle(alumnos)











