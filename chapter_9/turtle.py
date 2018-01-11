import turtle
nbrsides = 10
for name in range(nbrsides):
    turtle.forward(100)
    turtle.right(360/nbrsides)
    for steps in range(nbrsides):
        turtle.forward(50)
        turtle.right(360/nbrsides)
