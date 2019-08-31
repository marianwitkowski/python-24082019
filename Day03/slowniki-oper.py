"""
Deklaracja slownika i operacje na nim
"""
osoba = {
    "imie" : "Jan",
    "nazwisko" : "Kowalski"
}
print(type(osoba))
osoba.update({ "wiek" : 22 })
print("aktualizacja slownika: ",osoba)
print("klucze slownika: ", osoba.keys())
print("tylko wartosci slownika: ", osoba.values())
print("klucze + wartosci: ", osoba.items())
print("zawartosc pojedynczego klucza: ", osoba["nazwisko"])
print("zawartosc pojedynczego klucza: ", osoba.get("imie"))

osoba["nazwisko"] = "Nowak"
print("aktualizacja istniejacej wartosc dla klucza: ", osoba)

osoba.pop("wiek") #usuniecie wartosci dla klucza "wiek"

print("iterowanie po kluczach slownika")
for key in osoba.keys():
    print(f"klucz={key}, wartosc={osoba[key]}")







