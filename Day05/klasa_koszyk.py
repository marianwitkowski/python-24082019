class Product:

    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def get_info(self):
        return f"id={self.__id}, name={self.__name}, price={self.__price}"

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def __str__(self):
        return f"id={self.__id}, name={self.__name}, price={self.__price}"

"""
Klasa implementujac koszyk
Mozna dodac tylko raz jeden produkt, w przypadku wielokrotnego wkladania tego samego produktu aktualizujemy ilość
Napisać metode pokazujaca zawartosc koszyka
Napisac metode obliczajac wartosc koszyka (wartosc wszystkich produktow)
"""
class Basket:
    def __init__(self):
        self._items = dict()
        self._price = 0

    def add_product(self, product, qnty):
        if product not in self._items.keys():
            self._items[product] = qnty
        else:
            self._items[product] += qnty
        #aktualizuj kwote total za produkty w koszyku
        self._price += product.get_price()*qnty

    def get_total_price(self):
        return self._price

    def show_basket(self):
        for key in self._items.keys():
            qnty = self._items[key]
            print(f"{str(key)} - ilość {qnty}")


woda = Product(1, 'Woda mineralna', 2.99)
zupka = Product(2, 'Zupka Knorr', 3.99)
lech = Product(3, 'Piwo Lech', 2.5)
hotdog = Product(4, 'Hotdog XXL', 7.99)

basket=Basket()
basket.add_product(woda, 10)
basket.add_product(zupka, 5)
basket.add_product(hotdog,2)
basket.add_product(woda,5)
basket.add_product(lech, 6)
basket.add_product(zupka,1)
basket.add_product(lech, 2)

basket.show_basket()
print(f"Towarów w koszyku za {basket.get_total_price():.2f} zł")
