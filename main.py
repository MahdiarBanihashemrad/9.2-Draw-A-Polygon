from turtle import *
screen = Screen()
screen.bgcolor('teal')

pen = Turtle()
pen.hideturtle()
pen.speed(4)


polygons = {3: "TRIANGLE", 4: "a", 5: "PENTAGON", 6: "HEXAGON"}


def regularpolygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        pen.forward(250/sides)
        turtle.right(360/sides)
    turtle.end_fill()










while True:
    sides = int(input("How many sides does your polygon have? "))
    if sides != 4:
        regularpolygon(pen, sides)
    elif sides <3:
        sides =input("Polygons can't have less than 3 sides: ")
    pen.clear()
screen.exitonclick