"""
Wprowadzanie danych od usera z uzyciem while
"""

# sposob 1
"""
while True:
    plec = input("Podaj plec [K/M]: ").upper()
    if plec in ["K","M"]:
        break
print(f"Wprowadzono plec = {plec}")
"""

# sposob 2
plec = None
# mozna rowniez taki warunek
# plec != "K" and plec != "M":
#
while not plec in ["K","M"]:
    plec = input("Podaj plec [K/M]: ").upper()
    pass
print(f"Wprowadzono plec = {plec}")
