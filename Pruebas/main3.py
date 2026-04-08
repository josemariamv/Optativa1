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

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def peso(self):
        return self.__peso

    @property
    def altura(self):
        return self.__altura

    @property
    def tipos(self):
        return self.__tipos

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

# ejercicio 3
import mysql.connector

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()
    for pokemon in listaPokemons:
        sql = "SELECT * from pokemon WHERE numero_pokedex = " + str(pokemon.codigo)
        cursor.execute(sql)
        fila = cursor.fetchall()
        if len(fila) == 1:
            print("Ya existe un pokemon con codigo ", pokemon.codigo, "en la pokedex")
        else:
            sql = "INSERT INTO pokemon VALUES (" + str(pokemon.codigo) + ", '" + pokemon.nombre + "', " + str(pokemon.peso) + ", " + str(pokemon.altura) + ")"
            #print(sql)
            cursor.execute(sql)
            tipos = pokemon.tipos
            for tipo in tipos:
                #print(tipo)
                sql="SELECT id_tipo FROM tipo WHERE nombre = '" + tipo + "'"
                cursor.execute(sql)
                codigoTipo = cursor.fetchall()[0][0]
                #print(codigoTipo)
                sql ="INSERT INTO pokemon_tipo VALUES (" + str(pokemon.codigo) + ", " + str(codigoTipo) +  ")"
                #print(sql)
                cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)
