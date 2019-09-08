"""
Piklowanie danych
"""
import pickle

lista = [ "Jan", "Maria", "Agnieszka", "Zygmunt"]
x = 42
y = 1.23456
text = "Hello world!"

with open("dump.bin", "wb") as fd:
    pickle.dump(lista, fd)
    pickle.dump(x, fd)
    pickle.dump(y, fd)
    pickle.dump(text, fd)

lista.append("Jarosław")
x = 24
y = 99.1234
text = "Ala ma kota"

with open("dump.bin", "rb") as fd:
    lista = pickle.load(fd)
    x = pickle.load(fd)
    y = pickle.load(fd)
    text = pickle.load(fd)


print(lista,x,y,text, sep='\n')







