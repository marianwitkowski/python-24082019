import math

"""
Rzut ukośny
Obliczanie zasiegu: v(pocz)^2 / g * sin(2*alfa)

Wysokosc max: v(pocz)^2 * sin(alfa)^2 / (2*g)

predkosc - m/s
g = stala grawitacyjna 9.81m/s2
alfa = kat wyrzutu
"""
STALA_GRAWITACYJNA = 9.81
PI = 3.14159

predkosc_pocz = float(input("Podaj prędkość początkową w m/s: "))
kat_alfa = float(input("Podaj kąt wyrzutu w stopniach: "))

#kat_w_radianch = (2*kat_alfa)*(math.pi/180)
zasieg_rzutu = predkosc_pocz**2 / STALA_GRAWITACYJNA * math.sin(math.radians(2*kat_alfa))
wysokosc_max = predkosc_pocz**2 * math.sin(math.radians(kat_alfa))**2 / (2*STALA_GRAWITACYJNA)

print("Zasieg = ",zasieg_rzutu)
print("Wys. maks. = ", wysokosc_max)



