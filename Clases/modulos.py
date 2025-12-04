# Puedo importar uno o varios módulos completos
import random
import random, sys
# En este caso tengo que poner como prefijo el nombre del módulo a la función
print(random.randint(1,6))

# O sólo una o varias funciónes de un módulo
from random import randint
from random import randint, shuffle, choice
# En este caso prescindo del prefijo
print(randint(1,6))

# Podemos personalizar el nombre del módulo
import math as mates
print(mates.pi)

# O personalizar el nombre de la función
from random import randint as azar
print(azar(1,6))

# Pero cuidado con los errores. No es lo mismo esto:
import math
print(math.sin(math.pi/2))
pi=3.1416
print(pi)
print(math.pi)

# que esto
from math import *
print(pi)
pi=3.14
print(pi)

#Algunos módulos precisan de instalación previa
# Módulos interesantes para administradores de sistemas
# sys, os, shutil, subprocess, platform

# Modulos interesantes para manejo de datos:
# pandas, pynum, pyspark, powerbi

# Módulo para trabajar con entornos gráficos
# tkinter

