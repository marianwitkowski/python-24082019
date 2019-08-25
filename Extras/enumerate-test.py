"""

Enumerate - przyklad
Opis funkcji - https://www.programiz.com/python-programming/methods/built-in/enumerate

"""

# zadanie - wypisać zawartość listy wraz z informacją o indeksie (numeracja od 1)
lista = ["A", "B", "C", "D"]

# wersja bez Enumerate
index = 1
print("\nWersja bez Enumerate")
for element in lista:
    print(f"Element nr {index} to {element}")
    index+=1

# wersja z Enumerate
print("\nWersja z Enumerate")
for index, element in enumerate(lista, 1):
    print(f"Element nr {index} to {element}")


