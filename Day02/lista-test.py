"""
Zabawy z listami
"""
lista = []
print(type(lista))

# dodawanie elementow
lista.append("Ala ma kota")
lista.append(True)
lista.append(-12.34567)
lista.append(True)
lista.append(-12.34567)
print(lista)

# obliczanie dlugosci listy
print("Dlugosc list = {}".format(len(lista)))
# ilosc wystapien elementu
print("Ile razy jest True w liscie = {}".format( lista.count(True) ))
print("Ile jest a w pierwszym elemencie listy - {}".format( lista[0].count("a")))
# wyszukiwanie w liscie
print("Pierwsze wystapienie wartosc to index = {}".format( lista.index(-12.34567) ))
# rozszerzanie listy
lista.extend([-1,-1]); print(lista)
# usuwanie z listy
lista.pop(1); print(lista)
# wstawianie do listy
lista.insert(2, 100); print(lista)
# czyszczenie listy
lista.clear(); print(lista)

