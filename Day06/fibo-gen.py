"""
 Ciąg Fibonacciego jako generator
"""
import time

def fibo_loop(n):
    a = 0
    b = 1
    for _ in range(0, n):
        a, b = b, a+b
    return a

def fibo_generator(n):
    a,b = 0,1
    for _ in range(0, n):
        yield a
        a, b = b, a+b

ktory_znak = 40

generator = fibo_generator(ktory_znak)
print(generator)

"""
print(next(generator))
print(next(generator))
"""
licznik = 1000

print("\nPetla loop:")
t1 = time.time()
for _ in range(0, licznik+1):
    for x in range(0,ktory_znak+1):
        fibo_loop(x)

t2 = time.time()
print(f"\nWykonalem sie w {(t2-t1)*1000} ms")

print("\nGenerator:")
t1 = time.time()
for _ in range(0, licznik+1):
    generator = fibo_generator(ktory_znak)
    list(generator)
t2 = time.time()
print(f"\nWykonalem sie w {(t2-t1)*1000} ms")