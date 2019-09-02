"""
 Kolejki i stosy
"""

from collections import deque

# przykład użycia stosu
# tworzenie
print("**** STOS (pierwszy wchodzi, ostatni wychodzi) ******")
wyrazy = deque()
tekst = "Ala ma kota i kot jest rudy"
for slowo in tekst.split(" "):
    wyrazy.append(slowo)

# zdejmowanie ostatniego elementow
print(wyrazy)
while len(wyrazy)>0:
    ostatni = wyrazy.pop()
    print(f"pobrany wyraz to: '{ostatni}', a pozostałe: {wyrazy}")

print("="*30)


# kolejka
# tworzenie danych
print("**** KOLEJKA (pierwszy wchodzi, pierwszy wychodzi) ******")

wyrazy = deque()
tekst = "Ala ma kota i kot jest rudy"
for slowo in tekst.split(" "):
    wyrazy.append(slowo)

# zdejmowanie pierwszego elementu
print(wyrazy)
while len(wyrazy)>0:
    pierwszy = wyrazy.popleft()
    print(f"pobrany wyraz z kolejki: '{pierwszy}', a pozostałe: {wyrazy}")

print("="*30)