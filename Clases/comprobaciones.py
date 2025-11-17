cadena = "ABCdef"
if cadena.isalpha():
    print("Son letras")

cadena = "123"
if cadena.isdigit():
    print("Son numeros")

if cadena.isalpha():
    print("Son letras")

cadena = "ABC123"
if cadena.isalnum():
    print("Son letras y números")

#Existen además isdecimal, isnumeric, isspace e isprintable, etc.

if isinstance(5,int):
    print("Es un entero")
else:
    print("No es un entero")

if not isinstance(5.5,float):
    print("No es un número con decimales")
else:
    print("Es un número con decimales")

print(type("HOLA"))

if isinstance("hola",str):
    print("Es un texto")
else:
    print("No es un texto")

if isinstance([1,2,"Pepe"],list):
    print("Es una lista")
else:
    print("No es una lista")