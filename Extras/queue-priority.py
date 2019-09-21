"""
Zaimplementować klasę realizującą obsługę kolejki priorytetowej
Komunikaty do kolejki możemy wkładać i pobierać.
Priorytet wiadomości (od 1 - najniższy do 5 - najwyższy) wpływa na kolejność obsługi komunikatu
Obsłużyć podanie komunikatu z zakresem priorytetu spoza zakresu
Obsłużyc pobieranie danych z kolejki w przypadku braku danych w kolejce
Co to jest kolejka? -> https://pl.wikipedia.org/wiki/Kolejka_(informatyka)
"""

class PriorityQueue:

    def __init__(self):
        self._kolejka = []

    # wkładam komunikat do kolejki
    def enqueue(self, message):
        if 0 < message[1] < 6:
            self._kolejka.append(message)
        else:
            raise Exception("Błędny priorytet")

    # pobieram komunikat z kolejki - metoda zwraca komunikat
    def dequeue(self):
        first = 0
        if len(self._kolejka) == 0:
            raise Exception("Wszystkie zgłoszenia zrealizowane")
        else:
            for i in range(0, len(self._kolejka)):
                if self._kolejka[i][1] > self._kolejka[first][1]:
                    first = i
            return self._kolejka.pop(first)

    # metoda zwraca informacje o wielkości kolejki (ile elementów jest w kolejce)
    def get_size(self):
        return len(self._kolejka)


#
# Przykład użycia:
#
clients_queue = PriorityQueue()
clients_queue.enqueue(("Nie działa internet", 1))
clients_queue.enqueue(("Nie działa telefon", 1))
clients_queue.enqueue(("Blokada usług", 4))
clients_queue.enqueue(("Zawiesza się", 2))

print(f"Aktualna liczba oczekujących: {clients_queue.get_size()}")

message = clients_queue.dequeue()
print(message)

message = clients_queue.dequeue()
print(message)

clients_queue.enqueue(("Problem z FV", 1))
message = clients_queue.dequeue()
print(message)
