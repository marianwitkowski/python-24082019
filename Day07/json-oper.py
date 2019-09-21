#
# operacje z wykorzystaniem formatu JSON
#
import json

slownik = { "imie": "Jan", "nazwisko":"Kowalski",
            "wiek":47,
            "dostepy": ['A01', 'C11', 'B07'], "kierownik" : False }

#print(type(slownik))
txt = json.dumps(slownik)
fh = open("json.txt", "wt")
fh.write(txt)
fh.close()

slownik = dict()
fh = open("json.txt", "rt")
txt = fh.read()
fh.close()

slownik = json.loads(txt)
print(slownik)