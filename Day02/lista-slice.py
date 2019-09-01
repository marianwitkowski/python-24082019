"""
Porcjowanie danych z listy
"""
lista = []
for i in range(1,11):
    lista.append(i**2)
print(lista)

print(lista[2:5]) # od indeksu 2 do indeksu 4 wlacznie
print(lista[5:]) #od indeksu 5 do konca
print(lista[5:-1]) #od indeksu 5 do przedostatniego
print(lista[3::2]) #od indeksu 3 do konca z krokiem=2
print(lista[::-1])

s = "Ala ma kota"
print(s[4:])