"""
Prosty przyklad dzialania petli "while"
"""
licznik = 6
while licznik>0:
    print(f"Wartosc licznika to {licznik}")
    licznik -= 2 # licznik = licznik - 1
    if licznik==2:
        break

print("Poza pętlą while")