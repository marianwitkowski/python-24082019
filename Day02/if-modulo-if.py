"""
sprawdz czy liczba:
- jest podzielna bez reszty dla 5 i 3
- jest podzielna bez reszty tylko dla 3
- jest podzielna bez reszty tylko dla 5
"""

liczba = int(input("Podaj liczbę: "))
if liczba%5==0 or liczba%3==0:
    if liczba%5==0 and liczba%3==0:
        print("przez 5 i 3")
    elif liczba%5==0:
        print("przez 5")
    else:
        print("przez 3")
else:
    pass

