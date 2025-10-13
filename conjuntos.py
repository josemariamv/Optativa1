# Los conjuntos en python están formados por elementos "sin orden"
# y por tanto no se pueden referenciar # sus elementos por la posición que ocupan.
# Tampoco pueden tener elementos duplicados

# creando conjuntos
profesPrimero={"Ana", "Roberto", "Eva", "Juan", "María"}
profesSegundo={"Eva", "Luis", "Víctor", "Carlos"}

# lo mas importante de los conjuntos son las operaciones especiales
# que se pueden hacer:

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

