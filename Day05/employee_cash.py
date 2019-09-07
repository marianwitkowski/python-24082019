"""

    Klasa Pracownik rejestruje ile czasu pracował i oblicza naleznosc
    Jesli pracował do 8h, to rozliczany jest wg. stawki godzinowej
    Jesli przepracował więcej niż 8h, to pierwsze 8h zaliczane jest wg. normalnej stawki
    a reszta godzin wg. 150% stawki godzinowej

"""

class Employee:
    def __init__(self, fname, lname, rate):
        pass

    def register_time(self, hours):
        pass

    def pay_salary(self):
        pass


mirek = Employee("Mirek", "Kowalski", 100)
mirek.register_time(10)
mirek.register_time(7)
mirek.pay_salary()
mirek.register_time(3)