# seek nos permite acceso aleatorio
# seek (offset, origen)
# offset indica el desplazamiento en bytes
# origen indica desde donde se cuenta el desplazamiento y es opcional
# 0 desde el inicio del archivo, 2 desde el final del archivo y 1 desde la posición actual del cursor
# el modo 1 sólo funciona con archivos binarios
# seek(0) va al inicio
# seek(0,2) va al final
# seek(n) se posiciona


# El metodo tell devuelve la posicion actual del cursor

with open("ejemplo.txt", "w") as f:
    f.write("Hola Mundo Python")

# Usar seek en modo lectura
with open("ejemplo.txt", "r") as f:
     print(f"Posición inicial: {f.tell()}")  # tell() devuelve la posición actual

     # Leer los primeros 4 caracteres
     print("Contenido:", f.read(4))
     print(f"Posición después de leer: {f.tell()}")

     # Mover el puntero al inicio (posición 0)
     f.seek(0)
     print(f"Posición tras seek(0): {f.tell()}")
     print("Lectura completa:", f.read())

# Modificar una palabra específica
with open("ejemplo.txt", "r+") as f:
     # Mover el puntero a la posición 5 (donde empieza "Mundo")
     f.seek(5)
     # Sobrescribir "Mundo" con "Todos"
     f.write("Todos")

     # Volver al inicio para ver el resultado
     f.seek(0)
     print("Archivo modificado:", f.read())

# Modificar una palabra al final
with open("ejemplo.txt", "r+") as f:
     # Mover el puntero al final
     f.seek(0,2)
     f.seek(f.tell()-6)

     # Sobrescribir "Python" con "Java!!!"
     f.write("Java!!!")

     # Volver al inicio para ver el resultado
     f.seek(0)
     print("Archivo modificado:", f.read())

