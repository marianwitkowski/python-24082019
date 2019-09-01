import urllib3
import sys

"""

Analiza danych archiwalnych dla spółek GPW
- obliczanie maks. dla miesiecy
- zapis do XLSX

"""

spolka = "pge"
data_start = "2019-01-01"
data_stop = "2019-01-10"

def pobierz_dane(spolka, start, stop):
    url = "https://stooq.pl/q/d/l/?s={}&d1={}&d2={}&i=d".format(
        spolka, start.replace("-", ""), stop.replace("-", ""))
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    s = r.data.decode("utf-8")
    if "Brak danych" in s:
        return None
    else:
        return s

dane = pobierz_dane(spolka, data_start, data_stop)
if dane is None:
    print("Brak danych z serwera")
    sys.exit(-1)
linie = dane.split("\n")
print(linie)


