textoOriginal = input("Introduce una frase: ")
textoOriginal = textoOriginal.lower()
letra = input("Letra a mantener: ")
textoAhorcado=""
for caracter in textoOriginal:
    if caracter==letra or caracter == " ":
        textoAhorcado += caracter
    else:
        textoAhorcado += "*"
print("Resultado: ", textoAhorcado)
# turno del jugador. Le pedimos una letra
letra = input("Introduce una letra: ")
# contamos cuantas veces aparece
veces = textoOriginal.count(letra)
print("La letra", letra, "aparece en", veces, "ocasiones")
if veces!=0: # si la letra que hemos elegido no aparece no hacemos nada
    # textoNuevo será la nueva string a mostrar
    textoNuevo = ""
    for i  in range(0,len(textoOriginal)):
        if textoOriginal[i] == letra: # si la letra nueva aparece la metemos en textoNuevo
            textoNuevo += letra
        else:
            textoNuevo+= textoAhorcado[i] # y, si no, metemos el texto modificado que tendrá un asterisco o la letra a mantener
    print("Resultado:", textoNuevo)