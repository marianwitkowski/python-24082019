"""
Wyrażenia listowe, funkcje lambda, callback
"""
import random
from functools import reduce

lista = list()
for i in range(0, 10):
    lista.append(random.randint(-100,100))

lista = [-10, -4, 1, 4, 5, 10, 11]
print("oryginal: ",lista)
lista_wy = list()
for elem in lista:
    lista_wy.append(elem*2)
print("po mnozeniu: ",lista_wy)

def mnoz_razy_2(x):
    return x*2
print("mnożę x 2 w map: ", list(map(mnoz_razy_2, lista)))
print("mnożę x 2 w map z lambda: ", list(map( lambda x:x*2, lista)))

def tylko_dodatnie(x):
    return x>0

print("tylko dodatnie z listy: ", list(filter(tylko_dodatnie, lista)))
print("tylko dodatnie z lambda: ", list(filter(lambda x: x>0, lista)))


def czy_wieksze(x1, x2):
    print(f"x1={x1}, x2={x2}")
    if x1>x2:
        return x1
    else:
        return x2

print("Maks z listy :",reduce(czy_wieksze, lista))
reduce(lambda x1,x2: x1 if x1>x2 else x2 , lista)