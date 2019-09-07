"""
 Klasa Product
 - zaimplementować konstruktor przyjmujący id produktu, nazwę i cenę jednostkową
 - napisać metodę do pobierania ceny
 - napisać metodę do ustawiania nowej ceny
 - napisać metodę zwracającą informacje o produkcie
"""
class Product:

    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price

    def get_info(self):
        # proszę aby zwróciło string
        return f"ID={self._id}, name={self._name}, price={self._price}"

    def __str__(self):
        return f"ID={self._id}, name={self._name}, price={self._price}"

    def set_price(self, new_price):
        self._price = new_price

    def get_price(self):
        return self._price

# przyklad uzycia
woda = Product(1, 'Woda', 2.99)
print(woda)

kabanos = Product(2, 'Kabanosy', 7.95)
print(kabanos)

hotdog = Product(3, 'Hotdog XXL', 6.99)
print(hotdog)
