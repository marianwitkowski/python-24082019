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
        pass


    #
    # wkładam komunikat do kolejki
    #
    def enqueue(self, message):
        pass


    #
    # pobieram komunikat z kolejki - metoda zwraca komunikat
    #
    def dequeue(self):
        return None


    #
    # metoda zwraca informacje o wielkości kolejki (ile elementów jest w kolejce)
    #
    def get_size(self):
        pass



#
# Przykład użycia:
#
clients_queue = PriorityQueue()
clients_queue.enqueue(("Nie działa internet", 1))
clients_queue.enqueue(("Nie działa telefon", 1))
clients_queue.enqueue(("Blokada usług", 4))

message = clients_queue.dequeue()
print(message)

message = clients_queue.dequeue()
print(message)

clients_queue.enqueue(("Problem z FV", 1))
message = clients_queue.dequeue()
print(message)