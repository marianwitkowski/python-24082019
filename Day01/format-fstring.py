"""
Formatowanie w stylu f-string (od Python 3.4)
"""
a = 10
b = 1.2345678
c = "Hello world!"

print(f" a={a:010}, b={b:.3f}, c={c}")
print("Nowa linia")
print(f"a={a}", end=" | ") # opcjalny parametry "end"
print(f"b={b}")
