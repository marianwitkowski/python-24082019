"""
 Dyrektywa warunkowa IF
"""
a = int(input("Podaj liczbę: "))
if a>10:
    print("Liczba większa od 10")
else:
    print("Liczba nie wieksza od 10")

print("=============")

"""
 sprawdzanie czy liczba w przedzialach:
 <0 , 0-9, >=10
"""
a = int(input("Podaj liczbę: "))
if a<0:
    print("Liczba <0")
elif 0<=a<=9:
    print("Liczba >=0 i <10")
else:
    print("Liczba >=10")

