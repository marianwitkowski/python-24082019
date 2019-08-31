"""
Sortowanie z wykorzystaniem klucza
"""
lista = [ (True, 1, "a"), (False, -1, "b"), (True, 10, "c"), (True, -10, "z") ]
print(lista)
lista.sort()
print(lista)


def wedlug_numeru(krotka):
    return krotka[1]

print(sorted(lista, key=lambda x:x[1], reverse=True))