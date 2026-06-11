# detecta los votos duplicados en la misma lista (fraudulentos)
def duplicados(lista):
    validos = set()
    repes = set()
    for voto in lista:
        if voto in validos:
            repes.add(voto)
        # el else sobra porque un conjunto no admite duplicados, pero así se entiende mejor
        else:
            validos.add(voto)
    return repes, validos

def contarVotos(votosER, votosCP):
    # El censo son los posibles pisos. Como son fijos los podemos poner en un conjunto
    # Sería fácil construirlo desde el programa si fuese variable
    # Prueba a hacerlo tú con una función
    censo = {"0A","0B","1A","1B","2A","2B","3A","3B", "4A", "4B"}

    # detectamos los posibles repes. En validos estarían los restantes
    repesER, validosER = duplicados(votosER)
    repesCP, validosCP = duplicados(votosCP)

    # Pisos inexistentes (no están en el censo)
    # la unión de los válidos menos el censo
    inexistentes = (validosER | validosCP) - censo

    # votos fraudulentos totales
    # la unión de los repes de las dos listas mas los inexistentes
    fraudulentos = repesER | repesCP | inexistentes

    # Limpiamos los fraudulentos haciendo la resta: validos - fraudes
    validosER = validosER - fraudulentos
    validosCP = validosCP - fraudulentos

    # Ahora detectamos los erroneos (votaron a ambas) así que hacemos la intersección
    erroneos = validosER & validosCP

    # y los quitamos también para obtener los finalmente válidos
    validosER = validosER - erroneos
    validosCP = validosCP - erroneos

    # Abstenciones: el censo menos los válidos, los erroneos y los fraudulentos
    abstenciones = censo - validosER - validosCP - erroneos - fraudulentos

    # contamos los votos fraudulentos y erroneos
    numFraudes = 0
    for v in votosER:
        if v in fraudulentos:
            numFraudes += 1
    for v in votosCP:
        if v in fraudulentos:
            numFraudes += 1

    numErrores   = len(erroneos) * 2  # uno por cada lista

    # como en el enunciado no está muy claro podríamos contarlos solo una vez, sin ver cuantas se repiten y estaría bien
    # numFraudes = len(fraudulentos)
    # numErrores = len(erroneos)

    # mostramos los resultados
    nER = len(validosER)
    nCP = len(validosCP)
    if nER == 0 and nCP == 0:
        resultado = "No hay ningún voto válido."
    elif nER == nCP:
        resultado = f"Escalera Republicana empata a {nER} votos con Comunidad Patriota."
    elif nER > nCP:
        resultado = (f"Escalera Republicana gana con {nER} votos válidos.\n"
                     f"Comunidad Patriota obtiene {nCP} votos válidos.")
    else:
        resultado = (f"Comunidad Patriota gana con {nCP} votos válidos.\n"
                     f"Escalera Republicana obtiene {nER} votos válidos.")

    print(f"Censo electoral: {len(censo)} viviendas")
    print(f"Abstenciones: {len(abstenciones)}")
    print(f"Votos fraudulentos: {numFraudes}")
    print(f"Votos erróneos: {numErrores}")
    print(resultado)


# Estos son los votos que aparecen en el enunciado
ER = ["0A", "0B", "3B", "1B", "4B"]
CP = ["2A", "1A", "5B", "0B", "2B", "2A", "4A", "2A", "3C"]

contarVotos(ER, CP)