from turtle import Screen, Turtle


screen = Screen()
screen.bgcolor("teal")
screen.title("Draw A Polygon")



pen = Turtle()
pen.hideturtle()
pen.speed(4)
pen.pensize(3)
pen.color("gold")



POLYGONS = {     
    3: "Triangle",
    4: "Quadrilateral",
    5: "Pentagon",
    6: "Hexagon",
}


def askyesorno(prompt):
    answer = input(prompt).lower()
    while answer not in ("y", "n"):
        answer = input("Please enter y or n: ").lower()
    return answer == "y"



def reset_pen():
    pen.clear()
    pen.penup()

def regular_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(80)
        turtle.right(360 / sides)
    turtle.end_fill()


def draw_unknown_quadrilateral():
    pen.penup()
    pen.goto(-80, 60)
    pen.pendown()
    pen.begin_fill()
    pen.goto(40, 100)
    pen.goto(100, -20)
    pen.goto(-20, -80)
    pen.goto(-80, 60)
    pen.end_fill()


def draw_trapezoid():
    pen.penup()
    pen.goto(-90, 0)
    pen.pendown()
    pen.begin_fill()
    pen.goto(-40, 40)
    pen.goto(30, 40)
    pen.goto(70, 0)
    pen.goto(-90, 0)
    pen.end_fill()


def draw_parallelogram():
    pen.penup()
    pen.goto(-90, 60)
    pen.pendown()
    pen.begin_fill()
    pen.goto(-20, -60)
    pen.goto(110, -60)
    pen.goto(40, 60)
    pen.goto(-90, 60)
    pen.end_fill()


def draw_rectangle():
    pen.penup()
    pen.goto(-110, 70)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(220)
        pen.right(90)
        pen.forward(120)
        pen.right(90)
    pen.end_fill()


def draw_square():
    pen.penup()
    pen.goto(-75, 75)
    pen.pendown()
    pen.begin_fill()
    for i in range(4):
        pen.forward(150)
        pen.right(90)
    pen.end_fill()


def identify_quadrilateral():
    parallel_pairs = int(input("How many pairs of parallel sides does your quadrilateral have? "))

    while parallel_pairs not in (0, 1, 2):
        parallel_pairs = int(input("Please enter 0, 1, or 2: "))

    if parallel_pairs == 0:
        return "Unknown quadrilateral", draw_unknown_quadrilateral

    if parallel_pairs == 1:
        return "Trapezoid", draw_trapezoid

    if askyesorno("Are all four side lengths equal? (y/n): "):
        return "Square", draw_square

    if askyesorno("Do all four angles have the same measure? (y/n): "):
        return "Rectangle", draw_rectangle

    return "Parallelogram", draw_parallelogram


def main():
    while True:
        sides = int(input("How many sides does your polygon have? "))
        while sides < 3:
            sides = int(input("Polygons must have at least 3 sides. Try again: "))

        reset_pen()

        if sides == 4:
            shape_name, draw_shape = identify_quadrilateral()
            print(f"Your polygon is a {shape_name}.")
            draw_shape()
        else:
            shape_name = POLYGONS.get(sides, "Unknown polygon")
            print(f"Your polygon is a {shape_name}.")
            regular_polygon(pen, sides)

        screen.exitonclick()


main()
