# from turtlelab5x import turtle, mickey, raph, leo, donnie, check
#
#
# def moveto(x, y):
#     if (x - turtle.x) > 0:
#         turtle.forward(x - turtle.x)
#         if (y - turtle.y) > 0:
#             turtle.left(90)
#             turtle.forward(abs(y - turtle.y))
#             turtle.right(90)
#         elif (y - turtle.y) < 0:
#             turtle.right(90)
#             turtle.forward(abs(y - turtle.y))
#             turtle.left(90)
#     elif (x - turtle.x) < 0:
#         turtle.left(180)
#         turtle.forward(abs(x - turtle.x))
#         if (y - turtle.y) > 0:
#             turtle.right(90)
#             turtle.forward(abs(y - turtle.y))
#             turtle.right(90)
#         elif (y - turtle.y) < 0:
#             turtle.left(90)
#             turtle.forward(abs(y - turtle.y))
#             turtle.left(90)
#     else:
#         if (y - turtle.y) > 0:
#             turtle.left(90)
#             turtle.forward(abs(y - turtle.y))
#             turtle.right(90)
#         elif (y - turtle.y) < 0:
#             turtle.right(90)
#             turtle.forward(abs(y - turtle.y))
#             turtle.left(90)
#
#
# # main program
# moveto(mickey.x, mickey.y)
# moveto(raph.x, raph.y)
# moveto(leo.x, leo.y)
# moveto(donnie.x, donnie.y)
#
# check()

from turtlelab5x import turtle, mickey, raph, leo, donnie, check


def moveto(x, y):
    if x < 0:
        turtle.backward(abs(x))
        if y <= 0:
            turtle.right(90)
            turtle.forward(abs(y))
            turtle.backward(abs(y))
            turtle.left(90)
        else:
            turtle.left(90)
            turtle.forward(abs(y))
            turtle.backward(abs(y))
            turtle.right(90)
        turtle.forward(abs(x))
    else:
        turtle.forward(abs(x))
        if y <= 0:
            turtle.right(90)
            turtle.forward(abs(y))
            turtle.backward(abs(y))
            turtle.left(90)
        else:
            turtle.left(90)
            turtle.forward(abs(y))
            turtle.backward(abs(y))
            turtle.right(90)
        turtle.backward(abs(x))


# main program
moveto(mickey.x, mickey.y)
moveto(raph.x, raph.y)
moveto(leo.x, leo.y)
moveto(donnie.x, donnie.y)

check()
