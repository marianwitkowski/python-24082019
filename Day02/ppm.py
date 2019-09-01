
"""
Liczenie podstawowej przemiany materii

Wzor dla kobiet:
PPM (kobiety) [kbal] =  655,1 + (9,563 x masa ciała [kg]) + (1,85 x wzrost [cm]) – (4,676 x [wiek])

PPM (mężczyźni) = 66,5 + (13,75 x masa ciała [kg]) + (5,003 x wzrost [cm]) – (6,775 x [wiek])
"""
plec = input("Podaj płeć K/M:").upper()
if plec in ["K","M"]:

    masa = float(input("Podaj masę ciała w kg: "))
    wzrost = float(input("Podaj wzrost w cm: "))
    wiek = float(input("Podaj wiek w latach: "))
    wsp_aktywnosci = float(input("Podaj wsp. aktywności [od 1 do 2]: "))


    if plec=="K":
        ppm = 655.1 + 9.563*masa + 1.85*wzrost - 4.676*wiek
    else:
        ppm = 66.5 + 13.75*masa + 5.003*wzrost - 6.775*wiek

    cpm = ppm * wsp_aktywnosci

    text_ppm = "Twoje PPM to " + str(ppm) + " kcal"
    text_cpm = "Twoje CPM to " + str(cpm) + " kcal"
    text = text_ppm + "\n" + text_cpm              # "\n" to jest znak nowej linii
    print(text)

else:
    print("Nie znam takiej płci")

