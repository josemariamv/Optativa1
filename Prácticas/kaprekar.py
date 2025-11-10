entrada = input("Introduce un número de cuatro cifras que no tenga todas sus cifras iguales: ")
# No tenemos constantes, pero las simbolizamos con variables en mayúsculas
KAPREKAR = 6174
# Primero hacemos comprobaciones: que no sea un número entero positivo
if entrada.isdigit() == False:
    print("No has introducido un número entero")
# que no tenga cuatro cifras
elif len(entrada)!=4:
    print("Tú número no tiene exactamente 4 cifras")
else:
    # que no sean todas iguales
    hayDiferencias = False;
    for i in range(1,4):
        if entrada[0]!=entrada[i]:
            hayDiferencias = True
    if hayDiferencias == False:
        print("No puedo obtener la constante de kaprekar si las cuatro cifras del número son iguales")
    else:
        numero = int(entrada)
        texto = entrada
        # o que el número ya sea la constante de kaprekar
        if numero == KAPREKAR:
            print("El número que has introducido ya es la constante de kaprekar")
        else:
            # en caso contrario empezamos el proceso descrito en el enunciado
            contador = 0
            while numero!=KAPREKAR:
                contador += 1
                # En listaAscendente guardo los cuatro dígitos del número ordenados de menor a mayor
                listaAscendente = list(texto)
                listaAscendente.sort();
                txtAscendente = ""
                txtDescendente = ""
                # Ahora recorro la lista y compongo los dos números en formato string
                for i in range(0,4):
                    txtAscendente = txtAscendente + listaAscendente[i];
                    txtDescendente = listaAscendente[i] + txtDescendente;
                # los resto y obtengo la diferencia
                numero = int(txtDescendente) - int(txtAscendente)
                texto = str(numero)
                # Si el número resultante tiene menos de cuatro cifras completo con ceros a la izquierda
                for i in range(len(texto),4):
                    texto = "0" + texto
                print(txtDescendente, "-", txtAscendente, "=", numero)
            print("Constante de kaprekar obtenida con ", contador, " operaciones")



