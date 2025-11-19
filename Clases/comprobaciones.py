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

# type me devuelve el tipo de dato de un objeto
print(type("HOLA"))

# isinstance es un método que me permite comprobar si un dato pertenece a un determinado tipo de dato
if isinstance(5,int):
    print("Es un entero")
else:
    print("No es un entero")

nota = 5.5
if not isinstance(nota,float):
    print("No es un número con decimales")
else:
    print("Es un número con decimales")

if isinstance("hola",str):
    print("Es un texto")
else:
    print("No es un texto")

if isinstance([1,2,"Pepe"],list):
    print("Es una lista")
else:
    print("No es una lista")