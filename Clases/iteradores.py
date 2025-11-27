# python define iteradores de forma automática para algunas de sus clases
# y también nos permite crear iteradores para las creadas por nosotros redefiniendo
# los métodos mágicos __iter__ y __next__

# Veamos primero como funcionan los iteradores en python:
profesores = ["Javier", "Natalia", "Agustín", "Eduardo", "José María"]
iterador = iter(profesores)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
# print(next(iterador, "STOP"))
print(next(iterador, "STOP"))
# cuando llegamos al final salta la excepción StopIteration salvo que especifiquemos un segundo parámetro que será lo que se devolverá al traspasar el último elemento

# Implementemos ahora una clase que defina su propio iterador
class DiasSemana:
    def __init__(self, dia):
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.indice = dia

    def __iter__(self):
        return self

    def __next__(self):
        #if self.indice >= len(self.dias):
        #    raise StopIteration
        # dia_actual = self.dias[self.indice]
        # self.indice += 1

        dia_actual = self.dias[self.indice]
        if self.indice ==6:
            self.indice = 0
        else:
            self.indice += 1

        return dia_actual

semana = DiasSemana(0)
iterador = iter(semana)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
