import pickle
class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellidos = ape

    def mostrarPersona(self):
        print("Esta persona se llama", self.nombre, self.apellidos)

p1 = Persona("José María", "Morales")
p2 = Persona("Pepe", "Potamo")

try:
    fichero = open("fichero6.bin", "bw")
    pickle.dump(p2,fichero)
    pickle.dump(p1,fichero)
    fichero.close()

    # problema: si no se cuantos objetos se han grabado y leo de mas provoca una excepción
    # puedo capturarla para detectar el final, pero existe un método mas cómodo
    fichero = open("fichero6.bin", "rb")
    p3 = pickle.load(fichero)
    p4 = pickle.load(fichero)
    fichero.close()
    p3.mostrarPersona()
    p4.mostrarPersona()

    # para escribir varios objetos y recuperarlos sin saber cuantos son
    fichero = open("fichero7.bin", "wb")
    lista = [p1,p2]
    pickle.dump(lista,fichero)
    fichero.close()

    fichero = open("fichero7.bin", "rb")
    lista2 = pickle.load(fichero)
    for p in lista2:
        p.mostrarPersona()
    fichero.close()
except:
    print("Error")