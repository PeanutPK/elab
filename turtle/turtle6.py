from turtlelab6 import turtle, home, library, shop, check
from math import atan2, sqrt, degrees


def distance(x1, y1, x2, y2):
    xdif = abs(x2 - x1)
    ydif = abs(y2 - y1)
    if xdif == 0:
        degre = 90
    else:
        degre = degrees(atan2(ydif, xdif))
    displace = sqrt(xdif ** 2 + ydif ** 2)
    return degre, displace


if abs(shop.y-turtle.y) < abs(library.y-turtle.y):
    degree, displacement = distance(turtle.x, turtle.y, shop.x, shop.y)
    turtle.left(degree)
    turtle.forward(displacement)
    turtle.right(degree)

    degree2, displacement2 = distance(turtle.x, turtle.y, library.x, library.y)
    turtle.right(degree2)
    turtle.forward(displacement2)
    turtle.left(degree2)

    degree1, displacement1 = distance(turtle.x, turtle.y, home.x, home.y)
    turtle.left(degree1)
    turtle.forward(displacement1)
    turtle.right(degree1)

else:
    degree2, displacement2 = distance(turtle.x, turtle.y, library.x, library.y)
    turtle.right(degree2)
    turtle.forward(displacement2)
    turtle.left(degree2)

    degree, displacement = distance(turtle.x, turtle.y, shop.x, shop.y)
    turtle.left(degree)
    turtle.forward(displacement)
    turtle.right(degree)

    degree1, displacement1 = distance(turtle.x, turtle.y, home.x, home.y)
    turtle.right(degree1)
    turtle.forward(displacement1)
    turtle.left(degree1)

check()
