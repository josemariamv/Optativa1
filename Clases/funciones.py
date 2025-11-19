
# La siguiente llamada da error porque la función no está aún definida
# La declaración de la función siempre tiene que ir antes de la primera llamada
# ambitos("Pepe Potamo")

# En los bloques no hay ámbitos, pero en las funciones si
# Todas las variables definidas fuera de la función se comportan como globales
def ambitos(nombre):
    apellidos = "Gómez Pérez"
    print(nombre)
    # name si existe dentro de la función porque es global
    # Pero no puedo modificarla
    # salvo que la defina como global
    global name
    print(name)
    name = "Marco Aurelio"
    # La variable apellidos definida dentro tiene preferencia sobre la global
    print(apellidos)
    print(otrosApellidos)

name = "José María"
apellidos = "Morales Vázquez"
otrosApellidos = "Soriano Rodríguez"
ambitos(name)
print(name)
# nombre no existe fuera de la función ni ninguna otra variable definida en ella
# print(nombre)

# Las funciones devuelven un valor con la palabra reservada return
# Es recomendable que las funciones tengan un sólo return. Un único punto de salida

def devuelveSaludo():
    return "Hola mundo"

print(devuelveSaludo())

#Podemos devolver mas de un valor separándolo por comas

def devuelveTresEnteros():
    return 1, 2, 3

num1, num2, num3 = devuelveTresEnteros()
print(num1, num2, num3)

# Los parámetros de las funciones se  pasan por valor cuando son variables simples.
# Los cambios hechos en la función no se transmiten fuera

numero = 10
texto = "Hola mundo"

def porValor(n, t):
    n = 100;
    t = "Adios, adios"

porValor(numero, texto)
print(numero, "-", texto)

# Cuando se pasa una lista como parámetro, sin embargo, se pasa por referencia.
lista = [1,2,3]

def porReferencia(l):
    l[1] = 100

porReferencia(lista)
print(lista)

# se le pueden asignar valores por defecto a los parámetros de una función
# los parámetros con valores por defecto siempre tienen que ir al final
def saluda(nombre, mensaje="Hola", ):
    print(mensaje, nombre)

saluda("José María", "Qué tal estás")
saluda("Margarita")

# Podemos tener mas de un parámetro por defecto. O incluso todos
# Si usamos el nombre del paŕametro podemos incluso modificar el orden
# Si no, tenemos que respetar el orden de la definción

def otroSaludo(nombre, mensaje="Hola", despedida="Hasta la vista"):
    print(mensaje, nombre, despedida)

otroSaludo("José María", mensaje="Qué tal estás")
otroSaludo("Pablo", "Bienvenido")
otroSaludo("Elise", "Bonjour", "")
otroSaludo("Margarita", despedida="Vuelve pronto")
otroSaludo("Enrique", despedida="Espero que estés bien", mensaje="Cuanto tiempo")

# Podemos definir funciones con un número variable de argumentos.
# Definimos el último parámetro de la función poniendo un * delante del nombre
# Y la función recibe los datos como una tupla. La tupla puede estar vacía si no se envía ningún argumento

def imprimeFicha(tipo, *datos):
    print(tipo)
    for elemento in datos:
        print(elemento)

imprimeFicha("Profesor", "José María", 57, "Informática", "jmoralesvazquez@educa.madrid.org")
imprimeFicha("Alumno", "Rodrigo", "2DAW")
imprimeFicha("Alumno", "López")

# También podemos enviar los parámetros a una función "empaquetados" en una lista o en una tupla
# En este caso ponemos el * en la llamada a la función, delante de la lista o tupla

datos = ["José María", 57]

def muestraDatos(nombre, edad):
    print("Nombre:", nombre, "Edad: ", edad)

muestraDatos(*datos)

# Si ponemos dos asteriscos en el paso de parámetro enviamos el valor del parámetro y su nombre
# como una pareja de clave y valor
def parejas(**argumentos):
    for clave, valor in argumentos.items():
        print(clave, valor)

parejas(a=5, b=20, c=23)

# Idem si pasamos un diccionario
def diccionario(**argumentos):
    for clave, valor in argumentos.items():
        print(clave, valor)

d = {'a': 10, 'b':20}
diccionario(**d) # 30

# En python se puede inidicar, a título informativo, los valores
# que recibe y devuelve una función, pero no es mandatorio
def prueba(numero: int) -> str:
    #return str(numero)
    return int(numero)

print(prueba(5))
print(prueba(5.5))




