"""
 Prosta klasa definująca osobę
"""
class Osoba:
    liczba_obiektow = 0

    def __init__(self, imie, nazwisko, plec):
        self._imie = imie
        self._nazwisko = nazwisko
        self._plec = plec
        Osoba.liczba_obiektow += 1

    def wyswietl(self):
        print(self._imie,self._nazwisko)

    def zmien_imie_nazwisko(self, imie, nazwisko):
        self._imie = imie
        self._nazwisko = nazwisko

    def pobierz_plec(self):
        return self._plec

    def odczytaj_nazwisko(self):
        return self._nazwisko

    def ustaw_nazwisko(self, nazwisko):
        self._nazwisko = nazwisko

    nazwisko = property(odczytaj_nazwisko, ustaw_nazwisko)

    @staticmethod
    def pobierz_licznik(self):
        return Osoba.liczba_obiektow

class Kobieta(Osoba):

    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko, "K")

    def wyswietl(self):
        print("Wielce Szanowna Pani",self._imie,self._nazwisko)


osoba1 = Osoba("Jan", "Kowalski", "M")
#osoba1._imie = "Mirek" #mozliwosc modyfikacji wprost (spoza klasy) pola obiektu (nie zalecane)

obecne_nazwisko = osoba1.nazwisko
print(obecne_nazwisko)
osoba1.nazwisko = "Nowak"

osoba1.wyswietl()
osoba1.zmien_imie_nazwisko("Zenon", "Martyniuk")
osoba1.wyswietl()
print(f"Plec: {osoba1.pobierz_plec()}")

kobieta1 = Kobieta("Anna", "Nowak")
kobieta1.zmien_imie_nazwisko("Ana", "Kowalska")
kobieta1.wyswietl()
print(f"Plec: {kobieta1.pobierz_plec()}")

kobieta2 = Kobieta("Agnieszka", "Kowalska")

print(f"Liczba obiektow: {Osoba.liczba_obiektow}")
