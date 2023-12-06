import math


class Cylinder:
    def __init__(self, radius, height):
        self.r = radius
        self.h = height

    def get_radius(self):
        return self.r

    def get_height(self):
        return self.h

    def set_radius(self, radius):
        self.r = radius

    def set_height(self, height):
        self.h = height

    def get_base_area(self):
        return math.pi * (self.r ** 2)

    def get_volume(self):
        return math.pi * self.h * (self.r ** 2)

    def __str__(self):
        return f"Radius: {self.r:.3f}, Height: {self.h:.3f}"
