from turtle import *
import random


pen = Turtle()
screen = Screen()



def create_turtle():
    pen = Turtle()
    pen.speed(0)
    pen.color(generate_random_hex_color())
    pen.shape('circle')
    pen.pensize(6)
    pen.setheading(random.randint(0, 360))
    return pen


def move_xy(turtle, deltaX, deltaY):
    newX = turtle.xcor() + deltaX
    newY = turtle.ycor() + deltaY

    if newX > 335 or newX < -345:
        deltaX *= -1
        newX = turtle.xcor()
    if newY > 347 or newY < -339:
        deltaY *= -1
        newY = turtle.ycor()

    turtle.goto(newX, newY)
    return deltaX, deltaY

def move_forward(turtle, turtles):
    turtle.forward(5)
    if turtle.xcor() > 335 or turtle.xcor() <-345:
        turtle.setheading(180-turtle.heading())

        turtles.append(create_turtle())
        #apend new turtle to turtles list

    if turtle.ycor() > 347 or turtle.ycor() < -339:
        turtle.setheading(turtle.heading() * -1)
        turtles.append(create_turtle())
        #append new to list

    return turtles


def generate_random_hex_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def playing_area():
    t = Turtle()
    t.color("teal")
    t.speed(0)
    t.pu()
    t.goto(-350, 350)
    t.setheading(0)
    t.pd()
    t.begin_fill()
    for i in range(4):
        t.forward(690)
        t.right(90)
    t.end_fill()

screen.bgcolor("black")
screen.setup(750, 750)


pen = Turtle()
pen.speed(0)
pen.color(generate_random_hex_color())
pen.shape('circle')
pen.pensize(6)
pen.setheading(random.randint(0, 360))
deltaX = random.randint(-5, 5)
deltaY= random.randint(-5, 5)

playing_area()


turtles = [pen]


while True:
    for obj in turtles:
        turtles = move_forward(obj, turtles)



screen.exitonclick()