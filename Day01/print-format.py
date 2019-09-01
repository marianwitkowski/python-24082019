
"""
Formatowanie danych w funkcji print()
"""
tekst = "ma kota"
print("Ala", tekst)

y = 10/8
#print("10/3=",y)

# funkcja .format - uzycie
print("wynik 10/8={:.5f}".format(y))
print("wynik 10/8={:10.5f}".format(y))
print("wynik 10/8={:010.5f}".format(y))

y = 12.356776
z = round( y , 3)
print("{} = {}".format(y, z))

a = 10
b = 15
print("a={0} - a={0}".format(a))
print("b={1}  a={0}".format(a, b))



