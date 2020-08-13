# tee ratkaisu tänne
def poista_isot(lista:list):
    i = 0
    isot = []
    while i < len(lista):
        value = lista[i]
        if value.isupper() == True:
            isot.append(value)
        i+=1
    for i in isot:
        lista.remove(i)

lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni"]
poista_isot(lista)
print(lista)
