try:
    fichero = open("binario.bin", "wb+")
    fichero.write(b"HOLA MUNDO")
    fichero.seek(0)
    texto = fichero.readline()
    print(texto)
    fichero.close();
except:
    print("Error")
