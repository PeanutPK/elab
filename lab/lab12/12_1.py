import copy
from vector import Vector


class Ball:
    """Maintains ball objects which can calculate their own movements."""

    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def __repr__(self):
        return f"Ball(pos={self.pos}, vel={self.vel}, acc={self.acc})"


ball1 = Ball(pos=Vector(1, 2), vel=Vector(3, 4), acc=Vector(5, 6))

ball2 = copy.deepcopy(ball1)

ball3 = copy.copy(ball1)

ball4 = ball1

print("-------------")
print("Before update")
print("-------------")
print(f"ball1 = {ball1}")
print(f"ball2 = {ball2}")
print(f"ball3 = {ball3}")
print(f"ball4 = {ball4}")

ball2.pos.x = 80
ball3.vel.x = 999
ball4.acc = Vector(0, 0)

print("------------")
print("After update")
print("------------")
print(f"ball1 = {ball1}")
print(f"ball2 = {ball2}")
print(f"ball3 = {ball3}")
print(f"ball4 = {ball4}")


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def is_on_x_axis(self):
        return self.y == 0

    def is_on_y_axis(self):
        return self.x == 0

    def translate(self, distX, distY):
        self.x += distX
        self.y += distY

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_x(self):
        return self.x

    def set_x(self, x=0):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y=0):
        self.y = y


p1 = Point(20, 100)
p2 = Point(-40, 50)
print(p1.is_on_x_axis())
print(p2.is_on_y_axis())
p1.translate(-60, -50)
print(p1 == p2)
print(p1)
print(p2)

