class Pokemon:
    def __init__(self,nombre,codigo,peso,altura,tipos):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__peso = peso
        self.__altura = altura
        self.__tipos = tipos

    def mostrar(self):
        print("#" + str(self.__codigo) + " - " + self.__nombre)
        print("Peso: ", str(self.__peso) + "kg")
        print("Altura: ", str(self.__altura) + "m")
        print("Tipo: ", end="")
        print(self.__tipos[0], end="")
        if len(self.__tipos) == 2:
            print(", " + self.__tipos[1])
        print("\n")

lineasMalas = []
listaPokemons = []
try:
    fichero = open('pokemons.txt')
    listaLineas=fichero.readlines()
    fichero.close()
except:
    print("Error")
else:
    for linea in listaLineas:
        if(linea[-1] == '\n'):
            linea = linea[:-1]
        #print(linea)
        elementos = linea.split(", ")
        #print(elementosLinea)
        if elementos[0].isdigit() == False or len(elementos)<5 or len(elementos)>6:
            lineasMalas.append(linea)
        else:
            listaTipos = elementos[4:]
            listaPokemons.append(Pokemon(elementos[1],int(elementos[0]),float(elementos[2]),float(elementos[3]),listaTipos))

# ejercicio 2
import pickle

def grabarFichero(fichero, lista):
    try:
        f = open(fichero,'wb')
        pickle.dump(lista, f)
        f.close()
    except:
        print("Error en grabación")

def leerFichero(fichero):
    lista = []
    try:
        f = open(fichero, "rb")
        lista = pickle.load(f)
        f.close()
    except:
        print("Error en lectura")
    return lista

grabarFichero("pokemons.bin", listaPokemons)
lista = leerFichero("pokemons.bin")

if len(lista)>0:
    print("\n" + str(len(lista)), "Pokemons correctos en el fichero:")
    for pokemon in lista:
        pokemon.mostrar()
else:
    print("No hay pokemons en el fichero")