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



