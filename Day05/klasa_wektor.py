"""
Klasa wektor i kilka operacji na nich
"""

class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Wektor [{self._x},{self._y}]"

    def add_vector(self, other_vector):
        return Vector(self._x + other_vector._x, self._y + other_vector._y)

    def __add__(self, other_vector):
        if type(other_vector) is not Vector:
            raise TypeError("You are not a vector")
        return Vector(self._x + other_vector._x, self._y + other_vector._y)

    def __sub__(self, other_vector):
        if type(other_vector) is not Vector:
            raise TypeError("You are not a vector")
        return Vector(self._x - other_vector._x, self._y - other_vector._y)

    def __eq__(self, other_vector):
        if type(other_vector) is not Vector:
            raise TypeError("You are not a vector")
        len1 = (self._x**2 + self._y**2)**1/2
        len2 = (other_vector._x**2 + other_vector._y**2)**1/2
        return len1==len2

    def __mul__(self, other):
        if type(other) not in [int, float]:
            raise TypeError("You are not scalar value")
        return Vector(self._x*other, self._y*other)

vector1 = Vector(2,2)
vector2 = Vector(1,-3)

try:
    vector3 = vector1.add_vector(vector2)
    print(vector3)

    vector3 = vector1 + vector2
    print("suma",vector3)
    vector3 = vector1 - vector2
    print("różnica",vector3)
    print("czy wektory są rowne?", vector1==vector2)
    print("mnoze wektor1 przez 3", vector1*3)

except Exception as e:
    print(e)



