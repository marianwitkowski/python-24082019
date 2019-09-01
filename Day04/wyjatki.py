"""
Kwestie związane z wyjątkami
https://docs.python.org/3/library/exceptions.html
"""
import sys
import traceback

lista = [1, 2, 4, 5, 6, 7, 10]
print(lista)

try:
    #raise Exception("to jest mój symulowany wyjątek")
    i = 0
    y = 3 / i
    #print(lista[11])
except IndexError as e:
    print("Wystapił wyjątek IndexError:",e)
except ZeroDivisionError as e:
    tb = sys.exc_info()
    print(tb)
    traceback.print_exc()
    print("Dzielenie przez zero:", e)
except Exception as e:
    print("Inny wyjatek:", e)
finally:
    lista.append(True)
    print("To sie wykona zawsze")

print(lista)