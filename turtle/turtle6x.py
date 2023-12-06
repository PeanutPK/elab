from turtlelab6x import turtle, home, library, shop, check
from math import atan2, sqrt, degrees


def pytha(x1=0, y1=0, x2=0, y2=0):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def zeta(x1=0, y1=0, x2=0, y2=0):
    return degrees(atan2((y1 - y2), (x1 - x2)))


def p2p(distance, degree):
    turtle.left(degree)
    turtle.forward(distance)
    turtle.left(-degree)


# first step
turtle_to_lib = pytha(library.x, library.y)
zetaL = zeta(library.x, library.y)

turtle_to_shop = pytha(shop.x, shop.y)
zetaS = zeta(shop.x, shop.y)

# second step
lib_to_shop = pytha(library.x, library.y, shop.x, shop.y)
zetaSL = zeta(library.x, library.y, shop.x, shop.y)

shop_to_lib = pytha(shop.x, shop.y, library.x, library.y)
zetaLS = zeta(shop.x, shop.y, library.x, library.y)

# third step
shop_to_home = pytha(shop.x, shop.y, home.x, home.y)
zetaSH = zeta(home.x, home.y, shop.x, shop.y)

lib_to_home = pytha(library.x, library.y, home.x, home.y)
zetaLH = zeta(home.x, home.y, library.x, library.y)

if turtle_to_lib + shop_to_home > turtle_to_shop + lib_to_home:
    p2p(turtle_to_shop, zetaS)
    p2p(shop_to_lib, zetaSL)
    p2p(lib_to_home, zetaLH)
else:
    p2p(turtle_to_lib, zetaL)
    p2p(lib_to_shop, zetaLS)
    p2p(shop_to_home, zetaSH)

check()
