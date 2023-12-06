import math


class Container:
    """ This is a meta class that's supposed to NOT have an initializer.
        It's only to be extended upon.
    """

    def __init__(self):
        pass


class Mushroom(Container):
    """ A mushroom-shaped container having a stem and a cap.
        Cap radius must be LARGER than the stem radius.
        If the user tries to make the cap too small, must throw ValueError.
        Dim Cost is: (length of stem) + (diameter of cap)
        Volume is: (volume of stem) + (volume of cap)
    """

    def __init__(self, stem_diameter, stem_length, cap_diameter):
        if cap_diameter <= stem_diameter:
            raise ValueError
        if min(stem_diameter, stem_length, cap_diameter) <= 0:
            raise ValueError
        self.__stem_diameter = stem_diameter
        self.__stem_length = stem_length
        self.__cap_diameter = cap_diameter

    @property
    def stem_diameter(self):
        return self.__stem_diameter

    @stem_diameter.setter
    def stem_diameter(self, stem_diameter):
        if self.__cap_diameter <= stem_diameter:
            raise ValueError
        if stem_diameter <= 0:
            raise ValueError
        self.__stem_diameter = stem_diameter

    @property
    def stem_length(self):
        return self.__stem_length

    @stem_length.setter
    def stem_length(self, stem_length):
        if stem_length <= 0:
            raise ValueError
        self.__stem_length = stem_length

    @property
    def cap_diameter(self):
        return self.__cap_diameter

    @cap_diameter.setter
    def cap_diameter(self, cap_diameter):
        if cap_diameter <= self.__stem_diameter:
            raise ValueError
        if cap_diameter <= 0:
            raise ValueError
        self.__cap_diameter = cap_diameter

    # Please define both dim_cost and volume PROPERTIES by yourself.
    @property
    def dim_cost(self):
        return self.__stem_length + self.__cap_diameter

    @property
    def volume(self):
        return math.pi * (
                (self.__stem_diameter / 2) ** 2 * self.__stem_length + (
                4 / 6) * (self.__cap_diameter / 2) ** 3)


try:
    stem_diameter = int(input())
    stem_length = int(input())
    cap_diameter = int(input())
    mybox = Mushroom(stem_diameter, stem_length, cap_diameter)
    print(mybox.dim_cost, mybox.volume)

    change_stem_diameter = int(input())
    mybox.stem_diameter = change_stem_diameter
    print(mybox.dim_cost, mybox.volume)

    change_stem_length = int(input())
    mybox.stem_length = change_stem_length
    print(mybox.dim_cost, mybox.volume)

    change_cap_diameter = int(input())
    mybox.cap_diameter = change_cap_diameter
    print(mybox.dim_cost, mybox.volume)

except ValueError:
    print("ERROR")
