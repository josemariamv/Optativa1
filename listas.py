import random

# Listas: secuencia de datos ordenada y mutable
# Admiten elementos duplicados
# Heterogenea: podemos mezclar datos de cualquier tipo
# Lo mas parecido a un vector o a un array

# creando listas
vector = []
vector2 = list()
vector3 = [1, 2, 3, 4, 5, 6, 7]
vector4 = [5, 3.5, "Antonio", "ASIR", False]
vector5 = list([5, 3.5, "Antonio", "ASIR", False])
vector6 = ["María", 5, [2, "ASIR", False], 56, "Calle del Pez, 5"]

# mostrándolas en consola
print(vector3)
print(vector5)
print(vector6)

# puedo modificar directamente cualquier elemento
vector6[0] = "María Dolores"
print(vector6)

# recorriendo listas.
#Sin obtener la posición
for elemento in vector3:
    print(elemento)

# Con la posición del elemento
for i in range(len(vector4)):
    print(i, "-", vector4[i])

# esto provoca una excepción por fuera de rango
# for i in range(len(vector4)+1):
#    print(i, "-", vector4[i])

# Añade un elemento al final de la lista
vector4.append("Calle del Suspiro Verde, 3")
print(vector4)

# Concatenando el contenido de dos listas
vector3 = vector3 + vector6
print(vector3)

# equivalente a:
# vector3.extend(vector6)
# print(vector3)

# Inserta un elemento delante de la posición 2
vector3.insert(2, "777")
print(vector3)
# Y en el penúltimo elemento
vector3.insert(-1, "777")
print(vector3)

# Si ponemos un elemento que no existe lo inserta al final
vector3.insert(999, "10")
print(vector3)

# Extrae el elemento de la posición 1 y lo elimina de la lista
elemento = vector3.pop(1)
print(vector3)
print(elemento)
# Extrae el último elemento
elemento = vector3.pop(-1)
print(vector3)
print(elemento)
# Esto provoca una excepcion ya que el elemento en la posicion 50 no existe
# vector3.pop(50)

# Elimina el elemento del argumento si existe
vector3.remove("María Dolores")
print(vector3)
# Elimina el elemento si existe. No es posicion.
# Al usar remove si hay mas de un elemento solo elimina el primero
vector3.remove(5)
print(vector3)
# Esto provoca una excepción porque el elemento no existe
#vector3.remove("Paquita la del barrio")

# ordena el vector de forma ascendente
# cuidado: no es que devuelva un vector ordenado como haría si fuese un string
# ordena el vector original. No devuelve nada
vector7 = [7.5, 44, 32.1, 569, 43, 12, 3.5, 25]
vector7.sort()
print(vector7)

# idem
vector8 = ["Rodríguez", "Heredia", "Giménez", "Alonso", "Vargas"]
vector8.sort()
print(vector8)

# ordena en orden descendente
vector8 = ["Rodríguez", "Heredia", "Giménez", "Alonso", "Vargas"]
vector8.sort(reverse=True)
print(vector8)

# cuidado: las minúsculas van después que las mayúsculas. No es orden alfabético real...
vector9 = ["Rodríguez", "Heredia", "giménez", "Alonso", "Vargas"]
vector9.sort()
print(vector9)

# Esto da error porque no puede ordenar números y strings
# vector4.sort()
# print(vector4)

# devuelve la posición en la que se encuentra el elemento del argumento
# si hay mas de uno devuelve la posición del primero
vector10 = [6, 7, 1, 4, 2, 4, 5, 6, 1, 1, 2, 8]
print(vector10.index(1))
# Si no está en la lista da error
# print(vector10.index(3))

# Otra forma de comprobar si un elemento está o no en la lista
# No obtenemos directamente la posicion (podemos preguntar después)
# pero tampoco provoca excepciones si no está
if 7 in vector10:
    print("Está en la lista")

if 33 not in vector10:
    print("No está en la lista")

# Devuelve cuantas veces aparece el elelento del argumento
print(vector10.count(1))
print(vector10.count(3))

# convierte una cadena en una lista. Cada caracter es un elemento
cadenaConvertida = list("Hola mundo")
print(cadenaConvertida)

# Convierte una lista en una cadena
listaConvertida = str(["Hola", "Mundo", "Cruel"])
print(listaConvertida)

# Podemos usar la sintaxis del emparedado con las listas
vector11 = [1, 2, 3, 4, 5, 6, 7, 8]
print(vector11[3])
print(vector11[3:6])
print(vector11[:3])
print(vector11[:6])
print(vector11[::-1])

# Si necesitamos una matriz podemos hacer una lista de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2])

# Random y listas
alumnos = ["María", "Pepe", "Juan", "Antonio"]
#elige un elemento al azar
print(random.choice(alumnos))
#elige tres elementos al azar sin repetición
print(random.sample(alumnos, 3))
#ordena los elementos de la lista al azar
random.shuffle(alumnos)
print(alumnos)
