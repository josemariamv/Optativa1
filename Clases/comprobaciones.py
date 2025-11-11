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