import urllib3
import sys
import xlsxwriter

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

"""
Analiza danych archiwalnych dla spółek GPW
- obliczanie maks. dla miesiecy
- zapis do XLSX
"""

spolka = "pge"
data_start = "2019-01-01"
data_stop = "2019-08-31"

dane_stat = dict() # tu beda zagregowane dane statystyczne

def pobierz_dane(spolka, start, stop):
    #url = "https://stooq.pl/q/d/l/?s={}&d1={}&d2={}&i=d".format(
    #    spolka, start.replace("-", ""), stop.replace("-", ""))
    url = "https://test-python-mw.s3-eu-west-1.amazonaws.com/pge_test.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    s = r.data.decode("utf-8")
    if "Brak danych" in s:
        return None
    else:
        return s

"""
 Funkcja tworzy rekord na podstawie wiersza z pliku CSV
 Jesli nie mozna utworzyc poprawnego rekordu, zwroc None
"""
def utworz_rekord(s):
    lista = s.strip().split(",")
    if len(lista)<5:
        return None
    return lista[0], float(lista[4])

dane = pobierz_dane(spolka, data_start, data_stop)
if dane is None:
    print("Brak danych z serwera")
    sys.exit(-1)
linie = dane.split("\n")[1:]
for wiersz in linie:
    rekord = utworz_rekord(wiersz)
    if rekord is None:
        continue
    #print(rekord) # ('2019-01-03', 123.45)
    klucz = rekord[0][0:7]

    if not klucz in dane_stat:
        dane_stat[klucz] = [rekord]
    else:
        dane_stat[klucz].append(rekord)

workbook = xlsxwriter.Workbook('gpw.xlsx')
worksheet = workbook.add_worksheet()

lista_max = list()
for xls_wiersz, klucz in enumerate(dane_stat.keys(), start=5):
    dane = dane_stat[klucz]
    maks_mc = max(dane, key=lambda x:x[1])
    print(f"Najwyższa cena w {klucz} była dnia {maks_mc[0]} i wyniosła {maks_mc[1]}")

    worksheet.write(f"A{xls_wiersz}", klucz)
    worksheet.write(f"B{xls_wiersz}", maks_mc[0])
    worksheet.write(f"C{xls_wiersz}", maks_mc[1])

    lista_max.append(maks_mc[1])

workbook.close()


plt.ioff()
plt.xticks(rotation=90)
plt.plot(list(dane_stat.keys()), lista_max)
plt.show()


