"""

 Napisać w formie klasy
 generator pseudolosowy liczb pierwszych

 użyć pakietu random
 do losowania liczb mozba uzyć: random.randint(0, max)

"""

import random


class PrimeGenerator:

    #
    # maks wartosc dla generowanej liczby
    #
    def __init__(self, max):
        pass



    #
    # generujemy liczbe z przedzialu 1, max - przy czym musi to byc liczba pierwsza
    # zapamietujemy wylosowana liczbę, bo generator ma dawać liczby pierwsze bez powtórzeń
    # obsłużyć rzuceniem wyjątku sytuację, gdy nie można już znaleźć "wolnej" liczby pierwszej w zakresie
    #
    def generate(self):
        pass


    #
    # "resetuje" generator - wywalamy informacje o liczbach, które były wczęsniej generowane
    #
    def reset(self):
        pass


### przykład użycia ###
primes_gen = PrimeGenerator(10000)

# losujemy 100 liczb pierwszych z zakresu 1-10000
for _ in range(100):
    print("Losowa liczba pierwsza = ",primes_gen.generate())

primes_gen.reset()
