#!/usr/bin/python3
fichero = open("fichero2.txt", 'w')
fichero.write("Contenido a escribir\n")
fichero.write("Otra linea")
fichero.close()

fichero = open("fichero3.txt", 'a')
fichero.write("Contenido a escribir\n")
fichero.close()

# con esta forma se realiza el autocerrado del fichero
with open("fichero5.txt", 'w') as fichero:
     fichero.write("En un lugar de La Mancha\n")
     fichero.write("de cuyo nombre no quiero acordarme...")

fichero = open("fichero4.txt", "w")
lista = ["Rodrigo", "Nadia", "Óscar", "David", "Rubén"]
fichero.writelines(lista)
fichero.close()

# seek nos permite acceso aleatorio
# seek (offset, origen)
# offset indica el desplazamiento en bytes
# origen indica desde donde se cuenta el desplazamiento y es opcional
# 0 desde el inicio del archivo, 2 desde el final del archivo y 1 desde la posición actual del cursor
# seek(0) va al inicio
# seek(0,2) va al final
# En archvios abiertos en modo texto no se permiten algunos tipos de desplazamientos
# El metodo tell devuelve la posicion actual del cursor

# Abrir el archivo en modo lectura/escritura (r+)
with open("quijote.txt", "r+", encoding="utf-8") as fichero:
     # 1. Leer el contenido actual
     contenido = fichero.read()
     print(f"Contenido original: {contenido}")

     # 2. Mover el puntero al final si se desea añadir texto
     # O al principio (0) para sobrescribir
     fichero.seek(0,2)

     # 3. Escribir nuevos datos
     fichero.write("\nNueva línea añadida.")

     print(fichero.tell())

     # 4. Volver al inicio para leer todo de nuevo
     fichero.seek(0)
     print(f"Contenido actualizado:\n{fichero.read()}")

