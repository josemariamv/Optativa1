
""" Esto es un comentario de
bloque
"""

print("hola mundo") # Esto es un comentario hasta el final de la línea
# En python no se definen variables. Tampoco se indica el tipo
edad = 5
precio = 10.5
texto = "Hola mundo"
acertado = False

# Si redefines una variable a otro tipo diferente cuela

texto = 57
print(texto)

#si trato de hacer algunas operaciones con una variable no definida previamente da error
# print(iva)
# cociente = dividendo / divisor

# En python no hay constantes, pero por convención se usan variables
# escritas con mayúsculas
MESES_DEL_ANNO = 12
#Pero, ojo, es una convención, no es una constante real. ¡Sigue siendo una variable!!!
MESES_DEL_ANNO = 11

# las asignaciones siempre tienen la menor prioridad en una instrucción
# y siempre se asigna de izquierda a derecha y nunca al revés
edad = edad + 1
edad+=1
print(edad)

print(5/2)
print(5%2)
# este no lo hay en java
print(5//2)

#algunos operadores que no existen en java
potencia = 4 ** 2
print(potencia)
# también así
print(4**2)

# convirtiendo entre tipos
precio_truncado = int(precio)
print(precio_truncado)

print(type(precio))
print(type(precio_truncado))

edad_con_decimales = float(edad)
print(edad_con_decimales)

#El operador + está sobrecargado para sumar cadenas
texto = "hola" + " " + "mundo"
print(texto)

#El método print también es mas potente que en java
print("hola", "mundo", "-", potencia)

# hablaremos mas de print. Por ahora solo saber que tiene dos parámetros por defecto: end="\n" y sep=' '
print("hola", "mundo", "-", potencia, end="")
print("\nhola", "mundo", potencia, sep=" - ")
edad = input("Dime tu edad")