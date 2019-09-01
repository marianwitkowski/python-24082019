"""
Co to sa krotki
"""
krotka = (1, "OK", 10.05)
#krotka[0] = 10 - to powoduje wyjatek
#
print(type(krotka))
print(krotka)

for element in krotka:
    print(element)

print("element 1 krotki to {}".format(krotka[1]))
print("elementow w krotce jest {}".format(len(krotka)))
print("czy NOK wystepuje w krotce {}".format("NOK" in krotka))

krop_z_1_elementem = (3,10) * 3

print(krop_z_1_elementem)