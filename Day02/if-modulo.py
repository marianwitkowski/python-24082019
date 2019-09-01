"""
sprawdz czy liczba:
- jest podzielna bez reszty dla 5 i 3
- jest podzielna bez reszty tylko dla 3
- jest podzielna bez reszty tylko dla 5
"""

liczba = int(input("Podaj liczbę: "))
if liczba%5==0 and liczba%3==0:
    print("Podzielna przez 5 i 3 bez reszty")
elif liczba%5==0:
    print("Podzielna przez 5")
elif liczba%3==0:
    print("Podzielna przez 3")
else:
    print("Jakas inna liczba")
