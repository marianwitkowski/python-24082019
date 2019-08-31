"""
Zbiory i operacje na nich
"""

# jak uzyskac unikalne wartosci w liscie
#lista = [1, 1, 2, 2, 3, 3]
#print(list(set(lista)))

# deklaracja zbioru (set)
zbior = { 1, True, 999.99, "Pies Ali to As", 1, 2, True }  #zbior = set()
print(zbior)

zbior.add(3) # dodanie do zbioru
print("Po dodaniu:",zbior)

zbior.update(["a", 12345]) # aktualizacja wartosc
print("Po aktualizacji:",zbior)

zbior.remove("a") #usuwam element ze zbioru
print("Po usunięciu litery 'a':",zbior)

zbior.discard("b") # usuwam, jesli nie ma, to nie sypie wyjatkiem
print("Po usunięciu litery 'b':",zbior)

zbior.pop() #usuniecie losowego elementu
print("Po operacji 'pop':",zbior)

print("Liczba elementow zbioru:",len(zbior))
zbior.clear() # zbior = {}


