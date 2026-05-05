from turtle import *
import random


pen = Turtle()
screen = Screen()
player = None



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


def create_player():
    player = Turtle()
    player.speed(0)
    player.color("white")
    player.shape("triangle")
    player.pu()
    player.goto(0, 0)
    return player


def spawn_player():
    global player
    if player == None:
        player = create_player()


def player_up():
    if player != None:
        player.setheading(90)


def player_down():
    if player != None:
        player.setheading(270)


def player_left():
    if player != None:
        player.setheading(180)


def player_right():
    if player != None:
        player.setheading(0)


def move_player():
    if player != None:
        player.forward(8)
        if player.xcor() > 335 or player.xcor() < -345:
            player.setheading(180-player.heading())

        if player.ycor() > 347 or player.ycor() < -339:
            player.setheading(player.heading() * -1)


def player_kill_turtles(turtles):
    if player != None:
        for turtle_object in turtles[:]:
            if turtle_object != player and player.distance(turtle_object) < 20:
                turtle_object.hideturtle()
                turtles.remove(turtle_object)
    return turtles


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
screen.tracer(0)
screen.listen()
screen.onkeypress(spawn_player, "space")
screen.onkeypress(player_up, "w")
screen.onkeypress(player_down, "s")
screen.onkeypress(player_left, "a")
screen.onkeypress(player_right, "d")


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
    move_player()
    turtles = player_kill_turtles(turtles)
    screen.update()



screen.exitonclick()
