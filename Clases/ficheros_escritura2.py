# seek nos permite acceso aleatorio
# seek (offset, origen)
# offset indica el desplazamiento en bytes
# origen indica desde donde se cuenta el desplazamiento y es opcional
# 0 desde el inicio del archivo, 2 desde el final del archivo y 1 desde la posición actual del cursor
# seek(0) va al inicio
# seek(0,2) va al final
# En archivos abiertos en modo texto no se permiten algunos tipos de desplazamientos
# El metodo tell devuelve la posicion actual del cursor

# Abrir el archivo en modo lectura/escritura (r+)
with open("quijote.txt", "a+", encoding="utf-8") as fichero:
     # 1. Leer el contenido actual
     fichero.seek(0)
     contenido = fichero.read()
     print(f"Contenido original: {contenido}")

     # 2. Mover el puntero al final si se desea añadir texto
     # O al principio (0) para sobrescribir
     fichero.seek(0,2)

     # 3. Escribir nuevos datos
     fichero.write("\nNueva línea añadida.")

     print(f"Posicion: {fichero.tell()}")

     # 4. Volver al inicio para leer todo de nuevo
     fichero.seek(0)
     print(f"Contenido actualizado:\n{fichero.read()}")