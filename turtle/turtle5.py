from turtlelab5 import turtle, check, leo

if (leo.x - turtle.x) > 0:
    turtle.forward(leo.x)
    if (leo.y - turtle.y) > 0:
        turtle.left(90)
    elif (leo.y - turtle.y) < 0:
        turtle.right(90)
    turtle.forward(abs(leo.y))

elif (leo.x - turtle.x) < 0:
    turtle.left(180)
    turtle.forward(abs(leo.x))
    if (leo.y - turtle.y) > 0:
        turtle.right(90)
    elif (leo.y - turtle.y) < 0:
        turtle.left(90)
    turtle.forward(abs(leo.y))

else:
    if (leo.y - turtle.y) > 0:
        turtle.left(90)
    elif (leo.y - turtle.y) < 0:
        turtle.right(90)
    turtle.forward(abs(leo.y))

check()
