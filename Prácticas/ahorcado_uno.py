textoOriginal = input("Introduce una frase: ")
# convertimos a minúsculas por si acaso aunque el enunciado no lo pide
textoOriginal = textoOriginal.lower()
letra = input("Letra a mantener: ")
textoAhorcado="" # En esta string construiremos la frase a mostrar en pantalla
for caracter in textoOriginal:
    if caracter==letra or caracter == " ": #si es igual a la letra a conservar o espacio lo copiamos igual
        textoAhorcado += caracter
    else: # y, si no, ponemos un asterisco
        textoAhorcado += "*"
print("Resultado: ", textoAhorcado)


