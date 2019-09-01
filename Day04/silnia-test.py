"""

2 funkcje obliczajace silnie n! = (1*2*3*.....*n)

"""

import time

def silnia(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if n<=1:
        return 1
    else:
        return n*silnia_rek(n-1)


MAX_N = 100
LICZNIK = 100000

t1 = time.time()
for _ in range(0, LICZNIK):
    silnia(MAX_N)
t2 = time.time()
print(f"Czas wykonania silni (loop) : {(t2-t1)*1000} ")

t1 = time.time()
for _ in range(0, LICZNIK):
    silnia_rek(MAX_N)
t2 = time.time()
print(f"Czas wykonania silni (rekurencja) : {(t2-t1)*1000} ")

