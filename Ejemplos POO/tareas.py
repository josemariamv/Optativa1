#!/usr/bin/python3
class Tarea:
    __lista = {}

    def __init__(self,id,titulo,prioridad):
        self.__id = id
        self.__titulo = titulo
        self.__prioridad = prioridad
        self.__completado = False
        Tarea.__lista[self.__id] = self


t1 = Tarea("T1", "Aprender Python", 10)
t2 = Tarea("T2", "Hacer Duolingo", 5)