
# obsluga otwarcia pliku - wersja old-fashion
fh = None
try:
    #otwarcie
    fh = open("plik1.txt")   #'c:/folder/plik.txt'
except Exception as e:
    print(e)
finally:
    #zamkniecie - koniecznie
    if fh:
        fh.close()

# new-fashion
try:
    with open("plik1.txt") as fh:
        pass
except Exception as e:
    print(e)