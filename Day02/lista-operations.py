"""
operacje na lista cd.
"""
import statistics

lista = [1,3,5,6,7,-10,20,100,-12]
lista.sort()
print(lista)

wynik = 0
for x in lista:
    wynik += x
print(f"suma = {wynik}")

print("suma = {}".format(sum(lista)))
print("max = {}".format(max(lista)))
print("min = {}".format(min(lista)))
print("srednia arytm. = {}".format(wynik/len(lista)))
print("srednia arytm. = {}".format(statistics.mean(lista)))
print("mediana = {}".format(statistics.median(lista)))
print(sorted(lista, reverse=True))
print(lista[::-1])

