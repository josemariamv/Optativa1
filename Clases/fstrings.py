# print con variables
nombre = "José María"
edad = 57
sueldo= 2400.356
# print usando el operador %
print("Mi nombre es %s, tengo %d años y cobro %f euros al mes" %(nombre, edad, sueldo))
print("Mi nombre es %s, tengo %d años y cobro %.2f euros al mes" %(nombre, edad, sueldo))

# Con f-strings
lenguaje = "Python"
escuela = "IES GOYA"
print(f"Estoy aprendiendo {lenguaje} en {escuela}.")

# cálculos y formateo de cadenas
num1 = 83.3
num2 = 9.54
print(f"El producto de {num1} y {num2} es {num1 * num2}")
print(f"El producto de {num1} y {num2} es {num1 * num2 :.3f}")

num3 = 0.83945
print(f"Porcentaje con 2 decimales: {num3:.2%}")

poblacion = 1234567890
print(f"La población del país es de: {poblacion:,} habitantes")

num4 = 45
num5 = 123
print(f"Números: {num4:04d} - {num5:04d}")

# Alineación
texto = "Python"
print(f"A la izquierda:   ***{texto:<20}***")
print(f"A la derecha:  ***{texto:>20}***")
print(f"Centrado: ***{texto:^20}***")

# debug
print(f"{num1=}, {num2=}")

# llamando a funciones
def autor():
    return "Vargas Llosa"

print(f"Hola Python, dime el autor del libro: {autor()}")

# f-string en varias líneas. Usamos las triples comillas dobles
nombre = "Alicia"
cargo = "Profesora"
experiencia = 5
ficha = f"""
Ficha de usuario/a:
-------------------
Nombre: {nombre}
Puesto: {cargo}
Experiencia: {experiencia} años
"""
print(ficha)

#Cuando necesitamos imprimir llaves en una f-string hay que duplicarlas
nombre = "Python"
print(f"{{ Estoy estudiando: {nombre} }}")

# condicionales
print(f"¿num1 es par? {True if num1 %2 == 0 else False}")

puntuacion = 85
print(f"Resultado: {'Aprobado' if puntuacion >= 50 else 'Suspenso'}")

valor = 42
print(f"Valor: {'Alto' if valor > 75 else 'Medio' if valor > 25 else 'Bajo'}")