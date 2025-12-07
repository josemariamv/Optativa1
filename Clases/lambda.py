'''
Las funciones lambda o anónimas son funciones sin nombre y de una sola línea
que se usan para operaciones sencillas y rápidas.
En python se definen con la palabra clave lambda, seguida de los argumentos, dos puntos,
y una única expresión (no puden tener múltiples sentencias) que se evalúa y retorna automáticamente.
Permiten escribir funciones pequeñas de forma compacta en una sola línea.
Pueden aceptar cualquier número de argumentos.
Son útiles para tareas temporales y se usan frecuentemente como argumentos en funciones de orden superior
'''

def cuadrado(x):
    return x**2

print(cuadrado(5))

# puesto que una función lambda no tiene nombre la única forma de usarla es asignarla a una variable
# la siguiente función lambda recibe x como argumento y devuelve su cuadrado.
# Una vez definida, la invocamos como si fuese una función común
cuadradoLambda = lambda x: x**2

print(cuadradoLambda(5))

cuadradoMayorQue10 = lambda x: True if x**2 >= 10 else False

print(cuadradoMayorQue10(3))
print(cuadradoMayorQue10(4))

# Las funciones lambda comparten casi las mismas funcionalidades que las normales
# Pueden recibir parámetros por defecto, un número de parámetros variables, reordenar los parámetros mencionando
# su nombre, etc.

media = lambda *lista: sum(lista) / len(lista)

print(media(3,5,1,7))

