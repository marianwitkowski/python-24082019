"""
Sprawdzanie czy plik jest plikiem PNG
"""
lista = [137, 80, 78, 71, 13, 10, 26, 10]
lista_binarna = bytearray(lista)

with open("plik.png", "rb") as fd:
    signature = fd.read(8)
    if signature == lista_binarna:
        print("To jest plik PNG")
    else:
        print("To nie jest PNG z kotkami")
