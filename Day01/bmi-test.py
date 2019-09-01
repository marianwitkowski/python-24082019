
"""
 Obliczam BMI
 User podaje wage w kg i wzrost w cm
 Wynik wyswietlam na ekranie

 Wzor: BMI = waga/(wzrost_w_metrach)2
 
"""

print("===== Obliczanie BMI =====")
waga = input("Podaj wagę w kg: ")
wzrost = input("Podaj wzrost w cm: ")

# konwersja typów zmiennych
waga = float(waga)
wzrost = float(wzrost)

# obliczam BMI
#bmi = waga / pow(wzrost/100, 2)
bmi = waga / (wzrost/100)**2
print("Twoje BMI to: ",  str(bmi))




