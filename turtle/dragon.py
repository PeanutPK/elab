LAB = "turtlelab8.py"
import urllib.request

urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}", LAB)

from turtlelab8 import turtle, radar, check

rad = radar.ball_direction()
while rad != 'x':
    rad = radar.ball_direction()
    print(rad)
    if 'n' in rad:
        turtle.left(90)
        while 'n' in rad:
            turtle.forward(1)
            rad = radar.ball_direction()
        turtle.right(90)
    elif 's' in rad:
        turtle.right(90)
        while 's' in rad:
            turtle.forward(1)
            rad = radar.ball_direction()
        turtle.left(90)
    else:
        while 'e' in rad:
            turtle.forward(1)
            rad = radar.ball_direction()
        while 'w' in rad:
            turtle.backward(1)
            rad = radar.ball_direction()
check()
