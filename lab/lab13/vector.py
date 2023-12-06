import math
import copy


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self, x=0, y=0):
        return f"Vector(x={self.x}, y={self.y})"

    def dot(self, v=(0, 0)):
        return self.x * v.x + self.y * v.y

    def add(self, v=(0, 0)):
        return Vector(self.x + v.x, self.y + v.y)

    def subtract(self, v=(0, 0)):
        return Vector(self.x - v.x, self.y - v.y)

    def multiply(self, s=0):
        return Vector(self.x * s, self.y * s)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y))

    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y))

    def __mul__(self, other):
        new = copy.deepcopy(self)
        new.x *= other
        new.y *= other
        return new

    __rmul__ = __mul__

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, _input):
        if not isinstance(_input, (int, float)):
            raise TypeError("x must be a number")
        self._x = _input

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, _input):
        if not isinstance(_input, (int, float)):
            raise TypeError("y must be a number")
        self._y = _input
