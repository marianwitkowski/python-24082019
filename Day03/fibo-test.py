"""
2 warianty obliczania n-tego wyrazu ciagu Fibbonaciego
"""
import time

def fibo_rek(n):
    if n<=1:
        return n
    else:
        return fibo_rek(n-1) + fibo_rek(n-2)

def fibo_loop(n):
    a = 0
    b = 1
    for _ in range(0, n):
        a, b = b, a+b
    return a

#fib_loop(10)
ktory_znak = 30

print("Rekurencja:")
t1 = time.time()
for x in range(0,ktory_znak+1):
    print(fibo_rek(x), end=',')
t2 = time.time()
print(f"\nWykonalem sie w {(t2-t1)*1000} ms")

print("-"*30)

print("\nPetla loop:")
t1 = time.time()
for x in range(0,ktory_znak+1):
    print(fibo_loop(x), end=',')
t2 = time.time()
print(f"\nWykonalem sie w {(t2-t1)*1000} ms")


