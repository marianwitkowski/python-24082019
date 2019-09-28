#
# unit test dla pliku functions.py
import unittest
import math

from functions import *

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self._x = [1, 2, 3.0]
        self._y = [math.pi, 4*math.pi, 9*math.pi]


    def test_pole_kola(self):
        for i in range(0, len(self._x)):
            self.assertEqual(oblicz_pole(self._x[i]), self._y[i] )
