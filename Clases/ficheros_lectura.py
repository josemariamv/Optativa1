#!/usr/bin/python3

#Se abre el fichero con el que queremos trabajar. Por defecto en modo lectura
#Modos: r, t (por defecto), w (lo elimina si existe), x (falla si existe), a (añade si existe y lo crea si no), b, + (lectura y escritura)
quijote = open('quijote.txt', 'rt')
piratas = open('/mnt/temp/piratas.txt')
#El método read() lee el fichero completo
print(quijote.read())
texto = piratas.read()
print(texto)
#No olvidar nunca cerrar el fichero después de su uso
quijote.close()
piratas.close()

quijote = open('quijote.txt')
linea=quijote.readline()
while linea !="":
    print(linea)
    linea = quijote.readline()
quijote.close()

quijote = open('quijote.txt')
linea=quijote.readline()
while linea !="":
    print(linea, end="")
    linea = quijote.readline()
quijote.close()

quijote = open('quijote.txt')
caracter=quijote.readline(1)
while caracter !="":
    print(caracter)
    caracter=quijote.readline(1)
quijote.close()

quijote = open('quijote.txt')
caracter=quijote.readline(1)
while caracter !="":
    print(caracter, end="")
    caracter=quijote.readline(1)
quijote.close()

quijote = open('quijote.txt')
lista_lineas=quijote.readlines()
print(lista_lineas)
quijote.close()

try:
    quijote = open('quijotemalescrito.txt')
except:
    print("No puedo abrir el fichero")
else:
    quijote.close();