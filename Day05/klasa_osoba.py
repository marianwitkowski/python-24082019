"""
 Prosta klasa definująca osobę
"""
class Osoba:

    def __init__(self, imie, nazwisko, plec):
        self._imie = imie
        self._nazwisko = nazwisko
        self._plec = plec

    def wyswietl(self):
        print(self._imie,self._nazwisko)

    def zmien_imie_nazwisko(self, imie, nazwisko):
        self._imie = imie
        self._nazwisko = nazwisko

    def pobierz_plec(self):
        return self._plec

osoba1 = Osoba("Jan", "Kowalski", "M")
osoba1._imie = "Mirek"
osoba1.wyswietl()
osoba1.zmien_imie_nazwisko("Zenon", "Martyniuk")
osoba1.wyswietl()
print(f"Plec: {osoba1.pobierz_plec()}")