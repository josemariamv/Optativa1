import random

veces = int(input("Cuantos dados vamos a tirar: "))
contador = 0
todosIguales = False
estadistica =[0,0,0,0,0,0]
while todosIguales==False:
    tirada = []
    contador = contador + 1
    for i in range (veces):
        # Para simular que el dado está trucado imagino un dado de 8 caras pero siempre que sale un 7 o un 8
        # lo contabilizo como si fuese un 6. Así este número tiene el triple de posibilidades de salir
        dado = random.randint(1,8)
        if dado == 7 or dado == 8:
            dado = 6
        tirada.append(dado)
        estadistica[dado - 1] += 1
    salida = str(tirada)
    salida = salida.replace("[","")
    salida = salida.replace("]", "")
    salida = salida.replace(", ", " - ")
    print(salida)
    if(tirada.count(tirada[0]) == veces):
        todosIguales = True;
totalDados = contador * veces
for i in range (len(estadistica)):
    print("El número", i+1, "ha salido el ", round(estadistica[i]*100/totalDados,2), "% de las veces")
print("He tenido que tirar los dados", contador, "veces para que salgan todos iguales")