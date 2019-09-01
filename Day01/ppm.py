
"""
Liczenie podstawowej przemiany materii

Wzor dla kobiet:
PPM (kobiety) [kbal] =  655,1 + (9,563 x masa ciała [kg]) + (1,85 x wzrost [cm]) – (4,676 x [wiek])

"""
masa = float(input("Podaj masę ciała w kg: "))
wzrost = float(input("Podaj wzrost w cm: "))
wiek = float(input("Podaj wiek w latach: "))
wsp_aktywnosci = float(input("Podaj wsp. aktywności [od 1 do 2]: "))

ppm = 655.1 + 9.563*masa + 1.85*wzrost - 4.676*wiek
cpm = ppm * wsp_aktywnosci

text_ppm = "Twoje PPM to " + str(ppm) + " kcal"
text_cpm = "Twoje CPM to " + str(cpm) + " kcal"
text = text_ppm + "\n" + text_cpm              # "\n" to jest znak nowej linii
print(text)

