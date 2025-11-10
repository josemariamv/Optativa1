opcion = input("Escribe P para jugar, C para configurar o X para salir: ")
match opcion:
    case "P":
        print("Has elegido jugar")
    case "C":
        print("Has elegido configurar")
    case "X":
        print("Has elegido salir. Adios, hasta la próxima")

opcion = input("Escribe P para jugar, C para configurar o X para salir: ")
match opcion:
    case "P":
        print("Has elegido jugar")
    case "C":
        print("Has elegido configurar")
    case "X":
        print("Has elegido salir. Adios, hasta la próxima")
    case _:
        print("Opción incorrecta")

opcion = input("Escribe P para jugar, C para configurar o X para salir: ")
match opcion:
    case "P" | "p":
        print("Has elegido jugar")
    case "C" | "c":
        print("Has elegido configurar")
    case "X" | "x":
        print("Has elegido salir. Adios, hasta la próxima")
    case _:
        print("Opción incorrecta")