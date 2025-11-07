import re

# Una expresión regular no es mas que un patrón que usamos para buscar
# coincidencias en cadenas de texto para identificar si cumplen con lo que
# esperamos: un dni, un número de teléfono, una matrícula de coche, etc.

patron = r"ola"
if re.match(patron, "ola"):
    print("Coincide")
else:
    print("No coincide")

# podemos usar indistintamente variables o literales
# Las expresiones regulares son strings encabezadas por la letra r
texto = "lola"
if re.match(r"lola", texto):
    print("Coincide")
else:
    print("No coincide")

# match no devuelve True, cuidado. Si lo hacemos igualando a True no funciona!
print(re.match(r"ola", "ola"))
print(re.match(r"ola", "caracola"))

# el metodo search funciona de forma similar a match

if re.search(r"ola", "caracola"):
    print("Coincide")
else:
    print("No coincide")

# match solo da por bueno si la coincidencia está al comienzo de la cadena
# search da por bueno si la coincidencia está en cualquier lugar de la cadena

# si queremos que la cadena coincida exactamente con el patrón usamos fullmatch

if re.fullmatch(r"ola", "olarrr"):
    print("Coincide")
else:
    print("No coincide")

# Las expresiones regulares siguen las mismas reglas que en cualquier otro
# lenguaje. Veamos algunos ejemplos

if re.fullmatch(r"[0-9]{8}[A-Z]", "28999777X"):
    print("Es un DNI válido")
else:
    print("No es un DNI válido")

if re.fullmatch(r"[a-z]+", "abc"):
    print("Cualquier secuencia de números sin letras. Uno mínimo")
else:
    print("No es válido")

if re.fullmatch(r"[^5]", "5"):
    print("Cualquier cosa que no sea un 5")
else:
    print("No es válido")

if re.fullmatch(r"[1-9]|1[0-2]", "22"):
    print("Es un mes")
else:
    print("No es válido")

if re.fullmatch(r"[0-9]{4} [A-Z]{3}", "6311 MXP"):
    print("Es una matrícula válida")
else:
    print("No es válido")

if re.fullmatch(r"(\w+)", "ban_derola9"):
    print("Es válida caracteres alfanuméricos. el único símbolo permitido es el _")
else:
    print("No es válido")
