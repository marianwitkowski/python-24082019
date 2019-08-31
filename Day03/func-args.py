"""
Deklaracja funkcji z parametrami domyslnymi
"""
def wypisz_imie(imie='Marian'):
    print("Twoje imie to",imie)

#wypisz_imie()

def nowy_uzytkownik(imie, nazwisko, obywatelstwo="PL", prepaid=False ):
    print("-"*30)
    print("imie :", imie)
    print("nazwisko :", nazwisko)
    print("obywatelstwo :",obywatelstwo)
    print("prepaid: ",prepaid)

#nowy_uzytkownik("Marian", "Witkowski")
#nowy_uzytkownik("Gunther", "Meyer", "DE", True)
#nowy_uzytkownik("Vladimir", "Putin", prepaid=True)

def funkcja_wiele_parametrow(param1, *mojeargs, param_opcja='*'):
    print("Listuje argumenty przekazane do funkcji")
    print("Parametr obowiazkowy param1=", param1)
    for arg in mojeargs:
        print("argument=",arg, "opcja=",param_opcja)

funkcja_wiele_parametrow(0.007, "jabłko", "banan", 123, "Ala ma kota", True, param_opcja="$")



