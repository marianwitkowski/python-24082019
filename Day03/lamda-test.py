"""
obliczanie rownania kwadratowego w postaci funkcji lambda
"""
# a = wsp. przy x2
# b = wsp. przy x
# c = wyraz wolny
def rownanie_kwadratowe(a, b, c):
    return lambda x: a*x**2 + b*x + c

def rownanie_kwadratowe_typowe(a, b, c, x):
    return a*x**2 + b*x + c

f = rownanie_kwadratowe(3, 0, 1)
print(type(f))

rownanie_kwadratowe_typowe(3, 0, 1, -2)
rownanie_kwadratowe_typowe(3, 0, 1, 5)
rownanie_kwadratowe_typowe(3, 0, 1, 10)

#wynika dla x = 5
print("wynik to: ", f(5))
print("wynik to: ", f(10))
print("wynik to: ", f(15))