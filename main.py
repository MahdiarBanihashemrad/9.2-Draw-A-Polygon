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
    pen.clear()

    if sides <3:
        sides = int(input("Polygons can't have less than 3 sides: "))
    elif sides != 4:
        regularpolygon(pen, sides)
    
    elif sides == 4:
        num_parrarel = int(input("How many pairs of parrarel lines does your quadrilateral have?: "))
        if num_parrarel == 0:
            pen.pu()
            pen.goto(100, 50)
            pen.begin_fill()
            pen.pd()
            pen.goto(135, -50)
            pen.goto(45, -65)
            pen.goto(0,0)
            pen.goto(100, 50)
            pen.end_fill()

        elif num_parrarel == 1:
            pen.pu()
            pen.goto(0,0)
            pen.begin_fill()
            pen.pd()
            pen.goto(30, 60)
            pen.goto(100, 60)
            pen.goto(140, 0)
            pen.end_fill()

        elif num_parrarel == 2:
            side_lengths = input("Are all of the side lengths equal? (y/n): ")
            if side_lengths == 'y':
                pen.pu()
                pen.goto(0,0)
                pen.begin_fill()
                pen.pd()
                pen.goto(0, 60)
                pen.goto(60, 60)
                pen.goto(60, 0)
                pen.goto(0,0)
                pen.end_fill()



screen.exitonclick