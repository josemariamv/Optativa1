import pickle
class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellidos = ape

    def mostrarPersona(self):
        print("Esta persona se llama", self.nombre, self.apellidos)

p1 = Persona("José María", "Morales")
p1.mostrarPersona()

fichero = open("fichero6.txt", "bw")
pickle.dump(p1,fichero)
fichero.close()

fichero = open("fichero6.txt", "rb")
p2 = pickle.load(fichero)
fichero.close()

p2.mostrarPersona()

# para escribir varios objetos y recuperarlos sin saber cuantos son
lista = [p1,p1]
pickle.dump(lista,fichero)

lista2 = pickle.load(fichero)
for p in lista2:
    p.mostrarPersona()