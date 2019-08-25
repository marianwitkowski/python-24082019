
a = float(input("Wymiar a [cm]: "))
b = float(input("Wymiar b [cm]: "))
c = float(input("Wymiar c [cm]: "))

if a>0 and b>0 and c>0:
    wynik = a*b*c
    if wynik>100**3:
        print("Za duży")
    else:
        print(f"Bedzie OK, a jego kubatura to {wynik:.3f} cm3")
else:
    print("Niepoprawne dane")
