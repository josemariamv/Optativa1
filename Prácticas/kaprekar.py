entrada = input("Introduce un número de cuatro cifras que no tenga todas sus cifras iguales: ")
KAPREKAR = 6174
if entrada.isdigit() == False:
    print("No has introducido un número entero")
elif len(entrada)!=4:
    print("Tú número no tiene exactamente 4 cifras")
else:
    hayDiferencias = False;
    for i in range(1,4):
        if entrada[0]!=entrada[i]:
            hayDiferencias = True
    if hayDiferencias == False:
        print("No puedo obtener la constante de kaprekar si las cuatro cifras del número son iguales")
    else:
        numero = int(entrada)
        texto = entrada
        if numero == KAPREKAR:
            print("El número que has introducido ya es la constante de kaprekar")
        else:
            contador = 0
            while numero!=KAPREKAR:
                contador += 1
                listaAscendente = list(texto)
                listaAscendente.sort();
                txtAscendente = ""
                txtDescendente = ""
                for i in range(0,4):
                    txtAscendente = txtAscendente + listaAscendente[i];
                    txtDescendente = listaAscendente[i] + txtDescendente;
                numero = int(txtDescendente) - int(txtAscendente)
                texto = str(numero)
                # Si el número resultante tiene menos de cuatro cifras completo con ceros a la izquierda
                for i in range(len(texto),4):
                    texto = "0" + texto
                print(txtDescendente, "-", txtAscendente, "=", numero)
            print("Constante de kaprekar obtenida con ", contador, " operaciones")



