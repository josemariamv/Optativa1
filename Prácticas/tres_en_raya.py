turno = "X"
numJugador = 1
while True:
    posicion = int(input("Jugador " + str(numJugador) +  " ("+turno+"): "))
    if numJugador == 1:
        turno = "O"
        numJugador = 2
    else:
        turno = "X"
        numJugador = 1

print("-------------")
for i in range(3):
    for j in range(3):
        print("|",end="")
        print("   ", end="")
    print("|\n-------------")