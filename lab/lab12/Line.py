class Point:
    # Constuctor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def is_on_x_axis(self):
        if self.__y == 0:
            return True
        else:
            return False

    def is_on_y_axis(self):
        if self.__x == 0:
            return True
        else:
            return False

    def translate(self, dist_x, dist_y):
        self.__x = self.__x + dist_x
        self.__y = self.__y + dist_y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.slope = (x2 - x1) / (y2 - y1)
        self.y_intercept = y1 - (self.slope * x1)
        self.start_point = Point(x1, y1)
        self.end_point = Point(x2, y2)

    def contains(self, x, y):
        return ((self.y2 <= y <= self.y1) and (self.x2 <= x <= self.x1)) or ((
                                                                                     self.y2 >= y >= self.y1) and (
                                                                                     self.x2 >= x >= self.x1))

    def get_distance(self):
        x_dif = self.x2 - self.x1
        y_dif = self.y2 - self.y1
        return (x_dif ** 2 + y_dif ** 2) ** 0.5

    def get_x1(self):
        return self.x1

    def get_y1(self):
        return self.y1

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2

    def get_y(self, x):
        y = self.slope * x + self.y_intercept
        if (self.y2 <= y <= self.y1) or (self.y2 >= y >= self.y1):
            return y
        else:
            return -999.999


# n = Line(1, 1, 4, 4)
#
# print(f"{n.get_x1()} {n.get_y1()} {n.get_x2()} {n.get_y2()}")
# print(n.contains(0.0, 0.0))
# print(n.contains(1.0, 1.0))
# print(n.contains(1.0, 0.0))
# print(n.contains(0.0, 1.0))
# print(n.contains(2.0, 0.0))
# print(n.contains(0.0, 3.0))
# print(n.get_distance())
# print(n.get_y(3))
# print(n.get_y(0))

x1 = int(input('Enter x1 : '))
y1 = int(input('Enter y1 : '))
x2 = int(input('Enter x2 : '))
y2 = int(input('Enter y2 : '))
line = Line(x1, y1, x2, y2)

print(f'value of x1 on this line is {x1:.3f}\n'
      f'value of x2 on this line is {x2:.3f}\n'
      f'value of y1 on this line is {y1:.3f}\n'
      f'value of y2 on this line is {y2:.3f}\n'
      f'==========')

print('Check x and y are on this line ?')
x = int(input('Enter x : '))
y = int(input('Enter y : '))
check = line.contains(x, y)
if check:
    print(f'x = {x:.3f} and y = {y:.3f} are on this line')
else:
    print(f'x = {x:.3f} and y = {y:.3f} are not on this line')
print(
    f'Distance between startPoint and endPoint is {line.get_distance():.3f}\n'
    f'==========')

print('Find value of y that gives( x , y ) on this line')
x = int(input('Enter x : '))
y = line.get_y(x)
print(f'value of y is {y:.3f}')
if y == -999.999:
    print(f'( x , y ) = ( {x:.3f} , {y:.3f} ) is not on this line')
else:
    print(f'( x , y ) = ( {x:.3f} , {y:.3f} ) on this line')
