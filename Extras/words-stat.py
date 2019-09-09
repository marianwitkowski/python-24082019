"""
Napisać klasę, która dokonuje statystyki tekstu
Szablony metod poniżej
"""

class TextParser:

    #
    #  file_name - nazwa pliku do parsowania
    #
    def __init__(self, file_name):
        pass

    #
    #    parsowanie danych tekstowych, liczenie statystyki znaków, w tym:
    #    - ile jest wyrazów o danej długości czyli ile jest 1-znakowych, 2-znakowych, 3-znakowych........ N-znakowych
    #    - ile jest słów w tekście
    #    - ile jest zdań w tekście
    #    - ile jest znaków interpunkcyjnych (przecinek, kropka, średnik)
    #
    def parse(self):
        pass


    #
    # zwraca wszystkie obliczone dane (format do wyboru)
    #
    def get_stat(self):
        pass


    #
    # metoda ładuje nowy plik tekstowy do parsowania (ale go nie parsuje)
    #
    def load_file(self, file_name):
        pass

    #
    # zdefiniować property (tylko w zakresie do odczytu), które zwróci poszczególne elementy statystyki znaków
    # https://www.programiz.com/python-programming/methods/built-in/property
    #
    total_words = property()            # liczba wyrazów
    total_sentences = property()        # liczba zdań
    words_stat = property()             # statystyka długości wyrazów
    punctuation_marks = property()      # liczba znaków interpunkcyjnych


#
# Przykład uzycia
#

parser = TextParser("file.txt")
parser.parse()
result = parser.get_stat()

parser.load_file("other_file.txt")
parser.parse()
text = parser.total_words


