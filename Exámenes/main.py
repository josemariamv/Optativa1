#/usr/bin/python
def divisores(n):
    divisores = {1,n}
    for i in range(2,n):
        if n%i == 0:
            divisores.add(i)
    return divisores

def enteroPositivo(n):
    correcto = True
    if n<=0 or n - int(n)!=0:
        correcto = False
    return correcto

def divisoresComunes(n1, n2):
    if enteroPositivo(n1) and enteroPositivo(n2):
        comunes = divisores(n1) & divisores(n2)
        lista = list(comunes)
        lista.sort()
        if len(lista) == 1:
            print("El único divisor común de 33 y 17 es: 1")
        else:
            listaTxt = str(lista)
            listaTxt = listaTxt.replace("[", "")
            listaTxt = listaTxt.replace("]", "")
            print("Los divisores coumunes de", n1, "y", n2, "son: ", listaTxt)
    else:
        print("No puedo calcular los divisores comunes de esos números")

divisoresComunes(22, 16)
divisoresComunes(33, 17)
divisoresComunes(1725, 2500)
divisoresComunes(22.5, 12)