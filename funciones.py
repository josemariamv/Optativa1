
# La declaración de la función siempre tiene que ir antes de la primera llamada a esta
# ambitos("Pepe Potamo")

def ambitos(nombre):
    print(nombre)
    # name si existe dentro de la función
    print(name)

name = "José María"
ambitos(name)
# nombre no existe fuera de la función
# print(nombre)

# En las funciones las variables si tienen ámbito
# Todas las variables definidas fuera de la función se comportan como globales