#
# przykład generowania 2 wątków
#
import threading
import time

stop = 30

def print_time(thread_name, counter):
    while counter>0:
        print(f"{thread_name} - {int(time.time())}")
        time.sleep(2)
        counter -= 1
    print(f"end of thread {thread_name}")

#print_time("Wątek 1", 3)
#print_time("Wątek 2", 5)

# inicjalizacja watkow
thread1 = threading.Thread(target=print_time, args=("Wątek1", 6))
thread2 = threading.Thread(target=print_time, args=("Wątek2", 10))

# uruchomienie watkow
thread1.start()
thread2.start()
print("start loop....")
while stop>0:
    time.sleep(1)
    print(f"stop ={stop}")
    stop -= 1