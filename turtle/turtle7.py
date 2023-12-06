from turtlelab7 import turtle, check


def draw_polygon(n, size):
    for i in range(n):
        turtle.forward(size)
        turtle.left(180-(((n - 2) * 180)/n))


check()
