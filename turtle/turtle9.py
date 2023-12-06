import urllib.request
from turtlelab9 import turtle, check

LAB = "turtlelab9.py"

urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}", LAB)


def fw():
    for i in range(5):
        turtle.forward(50)


def bw():
    for i in range(5):
        turtle.backward(50)


for j in range(4):
    fw()
    bw()
    turtle.left(180)
    fw()
    bw()
    turtle.left(45)


check()
