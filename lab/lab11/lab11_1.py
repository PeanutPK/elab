import math


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


u = Vector(2, 5)
v = Vector(3, 8)
w = u.add(v)
print(u, v, w)
x = u.subtract(v)
print(u, v, x)
y = v.multiply(3)
print(v, y)
z = v.add(u.multiply(2))
print(u, v, z)
