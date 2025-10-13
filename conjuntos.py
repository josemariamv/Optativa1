# Los conjuntos en python están formados por elementos "sin orden"
# y por tanto no se pueden referenciar # sus elementos por la posición que ocupan.
# Tampoco pueden tener elementos duplicados. Si podemos modificar su contenido (mutables)
# Pero sus elementos no pueden ser modificables. Esto excluye las listas

# creando conjuntos
profesPrimero={"Ana", "Roberto", "Eva", "Juan", "María"}
# o así
profesSegundo=set(["Eva", "Luis", "Víctor", "Carlos"])

# Aquí también podemos usar casi todos los métodos que hemos visto en listas
if "Eva" in profesPrimero:
    print("Eva es profe en Primero")
else:
    print("Eva no es profe en Primero")

for profe in profesSegundo:
    print(profe)

# pero no los que tienen que ver con la posición del elemento
#for i in range(len(profesSegundo)):
#    print(i, "-", profesSegundo[i])

# profesSegundo[0] = "Arturo"

# Aunque son heterogeneos, un elemento de un conjunto no puede ser una lista
# Debido a que el conjunto no es inmutable pero sus elementos si deben de serlo
conjunto1 = {1,2,(3,4,5), "Hola mundo"}
#conjunto2 = {1,2,[3,4,5],"Hola mundo"}

# añado un elemento. no especifico el orden porque no tiene!
profesPrimero.add("Arturo")
print(profesPrimero)
# si añado un elemento que ya está no me hace caso. Tampoco da error
profesPrimero.add("Arturo")
print(profesPrimero)

# elimina un elemento. si no existe da excepción
profesPrimero.remove("Arturo")
print(profesPrimero)
#profesPrimero.remove("Arturo")

# discard hace lo mismo pero si no existe no da error
profesPrimero.discard("Ana")
print(profesPrimero)
profesPrimero.discard("Ana")

# pop recupera y elimina un elemento al azar
elemento = profesPrimero.pop()
print(elemento)
print(profesPrimero)

# clear limpia el conjunto de elementos
profesPrimero.clear()
print(profesPrimero)

# pero lo mas importante de los conjuntos son las operaciones especiales
# que se pueden hacer:
profesPrimero={"Ana", "Roberto", "Eva", "Juan", "María"}

# intersección (los elementos en ambos)
print(profesPrimero & profesSegundo)

# unión  (todos sin duplicados)
print(profesPrimero | profesSegundo)

# diferencia (los que están en el primero menos los que están en el segundo)
print(profesPrimero - profesSegundo)
# piensa que el orden importa en esta operación
print(profesSegundo - profesPrimero)

# exclusive or (los que están en uno u otro pero no en ambos)
print(profesPrimero ^ profesSegundo)

# Estas operaciones tienen métodos asociados
print(profesPrimero.intersection(profesSegundo))
print(profesPrimero.union(profesSegundo))
print(profesPrimero.difference(profesSegundo))
print(profesPrimero.symmetric_difference(profesSegundo))

# tenemos mas métodos para operar con conjuntos. investígalos por ti mismo si te hacen falta!
