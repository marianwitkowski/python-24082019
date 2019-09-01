"""
Prosty kalkulator
- Wprowadz 2 liczby
- podaj operacje + , - , * , /
- wyswietl wynik
"""
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))
operacja = input("Podaj działanie (+,-,*,/): ")

wynik = 0
if operacja in ['*','/','+','-']:
    if operacja=="+":
        wynik = liczba1 + liczba2
    elif operacja=="-":
        wynik = liczba1 - liczba2
    elif operacja=="*":
        wynik = liczba1 * liczba2
    elif operacja=="/":
        if liczba2==0:
            wynik = "Nie moge wykonac tego dzialania"
        else:
            wynik = liczba1 / liczba2
    else:
        pass
    print(f"Oto wynik = {wynik} ")
else:
    print("Działanie spoza zbioru")
