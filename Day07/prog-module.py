#
# wykorzystanie modulow
#
from math import pi
import time
import sys
import extras.statystyka.stats as st

from pracownik import Pracownik # import tylko klasy Pracownik
import utils

import matematyka.planimetria.kolo as kolo
import matematyka.algebra.kwadrat as kwadrat

print("obwod=",kolo.oblicz_obwod(5))
print("pole=",kolo.oblicz_pole(5))

print("delta=", kwadrat.oblicz_delta(1,4,3))

sekundy = time.time()
liczba_pi = pi #odwolanie wprost do zaimportowanej stałej
pracownik = Pracownik("Jan", "Kowalski")
print(utils.random_value())
utils.say_hello()
print("="*40)
#c:\python-moduly\
sys.path.append("c:/python-moduly/")
for item in sys.path:
    print(item)

st.func1()
st.get_max([1])