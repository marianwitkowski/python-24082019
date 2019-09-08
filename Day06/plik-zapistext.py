
with open("plik-zapis.txt", "wt") as fd:
    fd.write("To jest nowa linia w pliku\n")
    fd.writelines(["Linia 2\n", "Linia 3\n", "Linia 4\n"])

bytes = bytearray()
bytes.append(10)
bytes.append(10)
for i in range(48, 58):
    bytes.append(i)

with open("plik.bin", "wb") as fd:
    fd.write(bytes)
