"""
 Klasa Product
 - zaimplementować konstruktor przyjmujący id produktu, nazwę i cenę jednostkową
 - napisać metodę do pobierania ceny
 - napisać metodę do ustawiania nowej ceny
 - napisać metodę zwracającą informacje o produkcie
"""
class Product:

    def __init__(self):
        pass

    def get_info(self):
        # proszę aby zwróciło string
        pass

    def set_price(self, new_price):
        pass

    def get_price(self):
        pass

# przyklad uzycia
woda = Product(1, 'Woda', 2.99)
print(woda.get_info())

kabanos = Product(2, 'Kabanosy', 7.95)
print(kabanos.get_info())

hotdog = Product(3, 'Hotdog XXL', 6.99)
print(hotdog.get_info())
