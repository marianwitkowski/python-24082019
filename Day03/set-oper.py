
zbiorA = set()
for x in range(1, 11):
    zbiorA.add(x)

zbiorB = set()
for x in range(8, 16):
    zbiorB.add(x)

print("zbior A=",zbiorA)
print("zbior B=",zbiorB)

print("Polaczenie zbiorow:", zbiorA.union(zbiorB))
print("Czesc wspolna: ", zbiorA.intersection(zbiorB))
print("Roznica symetryczna: ", zbiorA.symmetric_difference(zbiorB))
print("zbiorA - zbiorB: ",zbiorA.difference(zbiorB))
print("zbiorB - zbiorA: ",zbiorB.difference(zbiorA))