import math


class Container:
    """ This is a metaclass supposed to NOT have an initializer.
        It's only to be extended upon.
    """

    def __init__(self):
        pass


class Banana(Container):
    """
    The Banana box.
    Define the volume and dim_cost using length and
    radius at the widest part.
    """

    def __init__(self, length, radius):
        if length < 4 * radius:
            raise ValueError
        self.__length = length
        self.__radius = radius

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length < (4 * self.__radius):
            raise ValueError
        self.__length = length

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if self.__length <= 4 * radius:
            raise ValueError
        self.__radius = radius

    @property
    def dim_cost(self) -> float:
        return float(self.__length + (2 * self.__radius))

    @property
    def volume(self) -> float:
        return (4 / 3) * math.pi * self.__length * (self.__radius ** 2)


try:
    l = int(input())
    r = int(input())
    b = Banana(l, r)
    print(b.length, b.radius, b.volume, b.dim_cost)

    b.length = int(input())
    print(b.length, b.radius, b.volume, b.dim_cost)

    b.radius = int(input())
    print(b.length, b.radius, b.volume, b.dim_cost)

    print(all([x.startswith('_Banana__') for x in list(vars(b))]))
except ValueError:
    print("ERROR")
