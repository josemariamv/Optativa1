textoOriginal = input("Introduce una frase: ")
# convertimos a minúsculas por si acaso
textoOriginal = textoOriginal.lower()
letra = input("Letra a mantener: ")
textoAhorcado=""
for caracter in textoOriginal:
    if caracter==letra or caracter == " ":
        textoAhorcado += caracter
    else:
        textoAhorcado += "*"
print("Resultado: ", textoAhorcado)
intentos=0
# Necesitamos un bucle para repetir intentos y una variable booleana que nos dirá cuando hemos terminado
acertado=False
while acertado==False:
    letra = input("Introduce una letra: ")
    veces = textoOriginal.count(letra)
    intentos+=1
    print("La letra", letra, "aparece en", veces, "ocasiones")
    if veces!=0:
        textoNuevo = ""
        for i in range(0,len(textoOriginal)):
            if textoOriginal[i] == letra:
                textoNuevo += letra
            else:
                textoNuevo+= textoAhorcado[i]
        asteriscos = 0
        # podríamos haberlo hecho antes, pero lo ponemos en un segundo recorrido para que quede mas claro
        # si quedan asteriscos en el texto es que no hemos terminado
        for c in textoNuevo:
            if c == "*":
                asteriscos+=1
        if asteriscos==0:
            acertado = True
        textoAhorcado = textoNuevo
        print("Resultado:", textoNuevo)
print("Haz ganado. Haz necesitado", intentos, "intentos para completar la frase")