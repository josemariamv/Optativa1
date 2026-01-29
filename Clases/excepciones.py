# formato comun de las excepciones.
try:
    # bloque donde pueden ocurrir las excepciones
    pass
except:
    # bloque que se ejecuta si hay una excepción
    pass
else:
    # bloque que se ejecuta si no hay una excepción
    pass
finally:
    # bloque que se ejecuta haya o no excepciones
    pass

try:
    x = int(input("Un entero please: "))
    division = 35/x
except ValueError:
    print("No puedo  convertir eso a entero")
except ZeroDivisionError:
    print("No puedo dividir por cero")
except:
    print("Otra excepción que no identifico")

# Extras
# Con raise podemos lanzar nuestras propias excepciones
n = int(input("Introduce un entero positivo: "))
if n < 0:
  raise Exception("No es un entero positivo")

# O lanzar una excepción existente aunque no se den las circunstancias
raise ZeroDivisionError("No has dividido por cero en realidad, pero ahí va eso")

# El metodo assert me permite lanzar una excepción si lo que se evalúa como argumento es falso
# Las dos líneas siguientes son equivalentes
# assert 1==3
# assert(1==3)
# El segundo parámetro, opcional, permite personalizar el mensaje de error
# assert (1==3, "1 no es igual a 3")
# assert 1==3, "1 no es igual a 3"




