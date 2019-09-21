"""

 Napisać w formie klasy
 generator pseudolosowy liczb pierwszych

 użyć pakietu random
 do losowania liczb mozba uzyć: random.randint(0, max)

"""

import random
import time
import math

class PrimeGenerator:

    #
    # maks wartosc dla generowanej liczby
    #
    def __init__(self, max):
        # inicjalizacja generatora liczb pseudolosowych
        if max<10:
            raise Exception("Are you serious ;) ?") # no trochę mało tych liczb pierwszych tu będzie
        random.seed(time.time_ns()) #inicjalizacja zalążka liczb pseudolosowych
        self._max = max
        self._primes = list()

    #
    # sprawdzanie czy liczba jest pierwsza
    #
    def is_prime_number(self, num):
        if (num < 2):
            return False
        else:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

    #
    # generujemy liczbe z przedzialu 1, max - przy czym musi to byc liczba pierwsza
    # zapamietujemy wylosowana liczbę, bo generator ma dawać liczby pierwsze bez powtórzeń
    # obsłużyć rzuceniem wyjątku sytuację, gdy nie można już znaleźć "wolnej" liczby pierwszej w zakresie
    #
    def generate(self):
        counter = 0
        while True:
            counter += 1
            if counter >= self._max:
                raise Exception("All numbers generated")

            number = random.randint(1, self._max)
            if number in self._primes:
                continue

            if not self.is_prime_number(number):
                continue

            self._primes.append(number)
            return number


    #
    # "resetuje" generator - wywalamy informacje o liczbach, które były wcześniej generowane
    #
    def reset(self):
        self._primes.clear()


### przykład użycia ###
primes_gen = PrimeGenerator(int(1000))

# losujemy 1000 liczb pierwszych z zakresu 1-10E9
for i in range(1000):
    try:
        print("Losowa liczba pierwsza = ",primes_gen.generate())
    except Exception as e:
        print("Achtung!",e)
        break
print("Total=",i+1)
primes_gen.reset()
