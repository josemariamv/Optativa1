#/usr/bin/python
def devuelveLinea(n):
    n = n - 1
    if n==-1:
        n=9
    linea=""
    for posicion in range(10):
        if posicion == n:
            linea += "O"
        else:
            linea += "X"
    return linea

def cifradoPin(pin):
    pinTxt = str(pin)
    for _ in range(len(pinTxt),4):
        pinTxt = "0"+ pinTxt
    lista = []
    for c in pinTxt:
        lista.append(devuelveLinea(int(c)))
    return tuple(lista)

tuplaCifrada = cifradoPin(0)
for linea in tuplaCifrada:
    print(linea)