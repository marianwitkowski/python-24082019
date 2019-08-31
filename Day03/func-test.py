import random
import math

def foo():
    return

def oblicz_pole_trojkata(a, h):

    def foo1():
        return 1

    wynik = 1/2*a*h
    return wynik

for x in range(0, 10):
    podstawa = random.randint(10, 21)
    wysokosc = random.randint(5, 11)
    pole_trojkata = oblicz_pole_trojkata(podstawa, wysokosc)
    print(f"Pole trojkata dla a={podstawa} i h={wysokosc} wynosi {pole_trojkata}")


def oblicz_pole_kola(r):
    return math.pi*r**2 #pow(r,2)

def oblicz_obwod_kola(r):
    return 2*math.pi*r

def oblicz_pole_i_obwod_kola(r):
    return oblicz_pole_kola(r), oblicz_obwod_kola(r)


promien = 25
pole_kola = oblicz_pole_kola(promien)
obwod_kola = oblicz_obwod_kola(promien)
print(f"Dla promienia r={promien}, pole to {pole_kola:.5f}, a obwod to {obwod_kola:.5f}")

pole_obwod = oblicz_pole_i_obwod_kola(promien)
print(f"Dla promienia r={promien}, pole to {pole_obwod[0]:.5f}, a obwod to {pole_obwod[1]:.5f}")

