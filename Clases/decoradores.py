# un decorador en python es una función que "envuelve" a otra función proporcionándole una funcionalidad extra
# se definen poniendo una arroba y luego el nombre del decorador

def mi_decorador(funcion):
    def envoltorio():
        print("Antes del saludo")
        funcion()
        print("Después del saludo")
    return envoltorio

@mi_decorador
def saludar():
    print("¡Hola, mundo!")

saludar()

# python tiene de serie muchos decoradores muy útiles. Algunos de ellos los hemos visto en este tema:
# @property, @classmethod, @staticmethod, etc.