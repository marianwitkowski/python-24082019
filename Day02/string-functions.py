
tekst = "Ala ma kota"
for znak in tekst:
    print(znak,end=",")

print("\n")
print("Czy palindrom?")

tekst = input("Podaj wyraz: ")
bez_spacji = tekst.replace(" ","").lower().strip()
if bez_spacji==bez_spacji[::-1]:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")
