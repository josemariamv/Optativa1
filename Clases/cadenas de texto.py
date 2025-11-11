print(len("Hola mundo!"))

#Precaución con:
cadena1 = "Estoy concatenando" + "cadenas" + "una detrás de otra"
#cadena1 = "Estoy concatenando" , "cadenas" , "una detrás de otra"
#cadena1 = "Estoy concatenando" + 3 + "cadenas" + "una detrás de otra"
#cadena1 = "Estoy concatenando" + str(3) + "cadenas" + "una detrás de otra"
##cadena1 = "Estoy concatenando" ,3, "cadenas" , "una detrás de otra"
print(cadena1)

print("Estoy concatenando" + "cadenas" + "una detrás de otra")
print("Estoy concatenando" , "cadenas" , "una detrás de otra")
print("Estoy concatenando" , 3, "cadenas" , "una detrás de otra")

#bocadillos, rebanados o slicing
print("Hola mundo!"[0])
print("Hola mundo!"[-1])
print("Hola mundo!"[2:6])
print("Hola mundo!"[2:6])
print("Hola mundo!"[:6])
print("Hola mundo!"[2:])
#hay un tercer parámentro
print("Hola mundo!"[::2])

cadena = "Hola mundo!"
print(cadena)
#dar la vuelta a una cadena con los rebanados
print(cadena[::-1])

texto = "Hola mundo cruel"
#texto[0] = "X"

# Dos formas de recorrer una cadena
for caracter in texto:
    print(caracter)

for i in range(0,len(texto)):
    print(i, " - ", texto[i])

# La segunda es mas versatil porque me permite recorrerla al revés, a saltos, etc.
for i in range(len(texto)-1, -1, -1):
    print(i, " - ", texto[i])


# convertir un número en string
textoNumerico = str(55)
print(textoNumerico + "€")
textoNumerico2 = str(135.69)
print(textoNumerico2 + "€")

# Algunos métodos interesantes
print(texto.upper())
print(texto.lower())
print(texto.swapcase())

print(texto.find("m"))
print(texto.find("M"))
# dos parámetros start y end, aunque puede usarse con bocadillos como cualquier otro método
print(texto.find("o"))
print(texto.find("o", 8, 11))
# pero cuidado que la posición que devuelve así es diferente!
print(texto[8:11].find("o"))

print(texto.count("o"))

# el tercer parámetro indica el número de reemplazos máximo
print(texto.replace("o", "x"))
print(texto.replace("o", "x", 1))

#La cadena original no se ha alterado
print(texto)

