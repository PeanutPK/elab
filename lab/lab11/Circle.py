from math import pi


class Circle:
    def __init__(self, center_x=0.0, center_y=0.0, radius=0):
        self.x = center_x
        self.y = center_y
        self.r = radius

    def get_perimeter(self):
        return 2 * pi * self.r

    def get_area(self):
        return pi * (self.r ** 2)

    def __str__(self):
        return f"Center: ({self.x:.1f}, {self.y:.1f}), Radius: {self.r:.1f}"

    def get_center_x(self):
        return self.x

    def get_center_y(self):
        return self.y

    def get_radius(self):
        return self.r

    def set_center_x(self, center_x):
        self.x = center_x

    def set_center_y(self, center_y):
        self.y = center_y

    def set_radius(self, radius):
        self.r = radius
