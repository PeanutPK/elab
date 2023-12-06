from turtlelab3x import turtle, home, shop, check

from math import degrees, atan

# distance = (shop.x**2 + shop.y**2)**0.5
# angle = degrees(atan(abs(home.y/home.x)))
# turtle.left(angle)
# turtle.forward(distance)
# turtle.right(angle)

# distance2 = ((home.x-shop.x)**2 + (home.y-shop.y)**2)**0.5
# angle2 = degrees(atan(abs((home.y-shop.y)/(home.x-shop.x))))
# turtle.left(angle2)
# turtle.forward(distance2)

# check()


from turtlelab3x import turtle,home,shop,check

angle = degrees(atan(abs(shop.y/shop.x)))
distance = (shop.x**2 + shop.y**2)**0.5
distance2 = ((home.x-shop.x)**2 + (home.y-shop.y)**2)**0.5
angle2 = degrees(atan(abs((home.y-shop.y)/(home.x-shop.x))))

turtle.left(angle)
turtle.forward(distance)
turtle.right(angle)

turtle.left(angle2)
turtle.forward(distance2)

check()
