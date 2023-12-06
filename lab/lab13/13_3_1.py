from math import *


class Container:
    """ This is a meta class that's supposed to NOT have an initializer.
        It's only to be extended upon.
    """

    def __init__(self):
        pass


class Box:
    """ A cuboid box, having width, depth, and height.
        When initializing the dimensions should be in cm.
        The dimcost is the sum of all three sides.
    """

    def __init__(self, width, depth, height):
        self.width = width
        self.depth = depth
        self.height = height
        self.update_dims()

    def update_dims(
            self):  # Update dim_cost and volume (both are private!) here.
        self.__dim_cost = self.width + self.height + self.depth
        self.__volume = self.width * self.height * self.depth

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self.update_dims()

    def get_depth(self):
        return self.depth

    def set_depth(self, depth):
        self.depth = depth
        self.update_dims()

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height
        self.update_dims()

    def get_dim_cost(self):
        return self.__dim_cost

    def get_volume(self):
        return self.__volume


class Cylinder(Container):
    """ A cylindrical tube, having length and diameter.
        It is used for shipping long things like rolled posters.
        Both dimensions should be in cm.
    """

    def __init__(self, length, diameter):
        self.length = length
        self.diameter = diameter
        self.dim_cost = pi * diameter
        self.volume = pi * (diameter / 2) ** 2


mybox = Box(10, 10, 10)
print(mybox.width, mybox.depth, mybox.height, mybox.volume)
mybox.volume = 300
print(mybox.width, mybox.depth, mybox.height, mybox.volume)
