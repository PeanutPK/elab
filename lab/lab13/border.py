from vector import Vector


class Border:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    def __repr__(self):
        return (f"Border(corner={self.corner},"
                f" width={self.width}, height={self.height})")

    # insert your new method(s) here (don't forget the indentation)

    @property
    def corner(self):
        return self._corner

    @corner.setter
    def corner(self, val):
        if not isinstance(val, Vector):
            raise TypeError("corner must be a Vector object")
        self._corner = val

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("width must be a number")
        elif val <= 0:
            raise ValueError("width must be greater than zero")
        self._width = val

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("height must be a number")
        elif val <= 0:
            raise ValueError("height must be greater than zero")
        self._height = val

    @property
    def left(self):
        return self.corner.x

    @property
    def right(self):
        return self.corner.x + self.width

    @property
    def bottom(self):
        return self.corner.y

    @property
    def top(self):
        return self.corner.y + self.height

    @property
    def sides(self):
        return self.left, self.right, self.bottom, self.top
