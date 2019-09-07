"""
 Klasa Product
 - zaimplementować konstruktor przyjmujący nazwę i cenę jednostkową
 - zaimplementować mechanizm autonumerowania ID produktu (od 1)
 - napisać metodę do pobierania ceny
 - napisać metodę do ustawiania nowej ceny
 - napisać metodę zwracającą informacje o produkcie
"""
class Product:

    auto_id = 1

    def __init__(self,  name, price):
        self._name = name
        self._price = price
        self._id = Product.auto_id
        Product.auto_id += 1

    def __str__(self):
        return f"ID={self._id}, name={self._name}, price={self._price}"

    def set_price(self, new_price):
        self._price = new_price

    def get_price(self):
        return self._price

# przyklad uzycia
woda = Product('Woda', 2.99)
print(woda)

kabanos = Product('Kabanosy', 7.95)
print(kabanos)

hotdog = Product('Hotdog XXL', 6.99)
print(hotdog)
