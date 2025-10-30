
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

# si tenemos mas de un parámetro por defecto tenemos que indicar cual es cual
# si decidimos no usar el valor por defecto

def otroSaludo(nombre, mensaje="Hola", despedida="Hasta la vista"):
    print(mensaje, nombre, despedida)

otroSaludo("José María", mensaje="Qué tal estás")
otroSaludo("Margarita", despedida="Vuelve pronto")
otroSaludo("Enrique", despedida="Espero que estés bien", mensaje="Cuanto tiempo")

# Podemos definir funciones con un número variable de argumentos.
# Definimos el último parámetro de la función poniendo un * delante del nombre
# Y la función recibe los datos como una tupla

def imprimeFicha(tipo, *datos):
    print(tipo)
    for elemento in datos:
        print(elemento)

imprimeFicha("Profesor", "José María", 57, "Informática", "jmoralesvazquez@educa.madrid.org")
imprimeFicha("Alumno", "Rodrigo", "2DAW")

# También podemos enviar los parámetros a una función "empaquetados" en una lista o en una tupla
# En este caso ponemos el * en la llamada a la función, delante de la lista o tupla

datos = ["José María", 57]

def muestraDatos(nombre, edad):
    print("Nombre:", nombre, "Edad: ", edad)

muestraDatos(*datos)



