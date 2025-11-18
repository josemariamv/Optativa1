# Los diccionarios son matrices asociativas en las que cada elemento consta
# de una pareja clave-valor
# Las claves no se pueden modificar ni pueden estar repetidas
# Los valores si
# Accedemos a los elementos a través de su clave, no de su posición ni de su valor

# definimos un diccionario vacío
dic1 = {}
dic2 = dict()
print(dic1, dic2)

#definimos un diccionario con contenido
dic3 = {"nombre": "José María", "edad": 57, "activo": True}
dic4 = dict(color="azul", modelo="Caddy", submodelo="Outdoor", motor=2.0)
print(dic3)
print(dic4)

# Los valores pueden ser cualquier cosa (números, textos, listas, boolenaos, otro diccionario...)
# Las claves no tienen porque ser textos. También pueden ser números y hasta otras cosas pero ¿tiene sentido poner un booleano como clave?
dic5={24: "charcutería Manolo", 26: "peluquería canina Sindy"}
dic6={True: "es verdad", False: "mentira cochina"}

# para acceder a un elemento a partir de su clave tengo dos formas:
# La primera provoca una excepción si la clave no existe. La segunda no. Devuelve None
print(dic5[26])
print(dic5.get(26))

# Si quiero cambiar lo que devuelve la función get cuando no existe la clave:
print(dic5.get(30, "Ese número de calle no existe"))

#recorrer las claves de un diccionario
for elemento in dic4:
    print(elemento)

# recorrer los valores:
for elemento in dic4:
    print(dic4[elemento])

# ambos
for clave, valor in dic4.items():
    print(clave, ":", valor)

# obtener una lista con las claves, con los valores o con ambos
claves = list(dic4.keys())
valores = list(dic4.values())
items = list(dic4.items())
print(claves)
print(valores)
print(items)

# Para modificar un elemento lo hacemos a través de la clave, como si fuese un elemento de un array
# si la clave a modificar no existe la da de alta como nueva
dic5[24]="Talleres Peláez"
dic5[28]="Bazar el burrito feliz"
print(dic5)

# update permite fusionar dos diccionarios. Las claves repetidas no se duplican
# en caso de claves repetidas se actualiza el valor con el nuevo
dic6={"Lunes": "IPE1", "Martes": "BB.DD.", "Miércoles": "Python"}
dic7={"Miércoles": "Programación", "Jueves": "Sistemas de la Información", "Viernes": "Lenguajes de Marcas"}
dic6.update(dic7)
print(dic6)

# clear borra un diccionario
dic5.clear()
print(dic5)

# pop devuelve el valor de la clave que se pasa como argumento y la elimina
# tratar de hacer pop con una clave inexistente provoca una excepción
print(dic3.pop("edad"))
print(dic3)

# se puede evitar el error pasando un segundo parámetro: el valor a devolver si no existe la clave
print(dic3.pop("edad", "Clave inexistente"))
print(dic3)

# popitem devuelve y elimina el último elemento introducido en el diccionario
# cuidado: hasta la versión 3.7 de python devolvía y eliminaba un elemento al azar
print(dic4.popitem())
print(dic4)

