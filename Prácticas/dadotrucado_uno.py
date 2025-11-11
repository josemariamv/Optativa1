import random

veces = int(input("Cuantos dados vamos a tirar: "))
contador = 0
todosIguales = False
while todosIguales==False:
    tirada = []
    # cuento el número de tiradas
    contador = contador + 1
    for i in range (veces):
        tirada.append(random.randint(1,6))
    # convierto la lista a string y hago los replaces necesarios para que sea como me la piden
    salida = str(tirada)
    salida = salida.replace("[","")
    salida = salida.replace("]", "")
    salida = salida.replace(", ", " - ")
    print(salida)
    # si lo que sale en el primer dado se repite tantas veces como dados hay es que son todos iguales
    if(tirada.count(tirada[0]) == veces):
        todosIguales = True;
print("He tenido que tirar los dados", contador, "veces para que salgan todos iguales")