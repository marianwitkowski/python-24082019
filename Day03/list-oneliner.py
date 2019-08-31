"""
Kilka jednolinijkowców operujacych na listach
"""
lista = []
for x in range(-10, 11):
    lista.append(x)
print(lista)

lista = [x for x in range(-10,11)]
print(lista)

lista = [x**2 for x in range(-10,11) if x%2!=0]
print(lista)

lista = [x+y for x in [10,20,30] for y in [40,50,60]]
print(lista)

s = "Ala ma kota i kot jest rudy"
#print(s.split(" "))
lista = [slowo[0].lower() for slowo in s.split(" ") if len(slowo)>=2]
print(lista)
