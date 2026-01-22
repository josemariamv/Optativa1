# seek nos permite acceso aleatorio
# seek (offset, origen)
# seek(0) va al inicio del archivo
# seek(0,2) va al final
# seek(n) se posiciona en el lugar indicado (contando siempre desde el principio en ficheros de texto)
# El metodo tell devuelve la posicion actual del cursor
# Combinando seek y tell podemos movernos a una posición concreta contando desde el final.
# Por ejemplo, si queremos movernos a 10 caracteres del final usamos f.seek(f.tell()-10)
# seek tiene un tercer método que nos permite movernos a una posición relativa al sitio donde se situa el cursor
# pero no funciona con ficheros de texto. Solo con ficheros binarios

try:
     # Creamos un fichero para el ejemplo
     with open("ejemplo.txt", "w") as f:
          f.write("Hola Mundo Python")

     # Probamos como funciona seek
     with open("ejemplo.txt", "r") as f:
          print(f"Posición inicial: {f.tell()}")  # debería de ser cero

          # Leemos los primeros 4 caracteres y volvemos a ver la posición
          print("Contenido:", f.read(4))
          print(f"Posición después de leer: {f.tell()}")

          # Movemos el cursor al inicio y leemos el fichero completo.
          f.seek(0)
          print(f"Posición tras seek(0): {f.tell()}")
          print("Lectura completa:", f.read())
          # El cursor ahora se siturará al final:
          print(f"Posición tras leer el fichero entero: {f.tell()}")

     # Abrimos ahora en lectura y escritura. El cursor se situa al inicio
     with open("ejemplo.txt", "r+") as f:
          # Movemos el cursor a la posición 5 (donde empieza "Mundo")
          f.seek(5)
          # Sobrescribimos "Mundo" con "Todos"
          f.write("Todos")
          # Volvemos al inicio y leemos el fichero entero para ver el resultado
          f.seek(0)
          print("Archivo modificado 1:", f.read())

          # Movemos ahora el cursor al final
          f.seek(0,2)
          # Nos posicionamos donde empieza la palabra "Python"
          f.seek(f.tell()-6)
          # Sobrescribimos "Python" con "Java!!!"
          f.write("Java!!!")
          # Volvemos al inicio para ver el resultado
          f.seek(0)
          print("Archivo modificado 2:", f.read())
except:
     print("Error")
