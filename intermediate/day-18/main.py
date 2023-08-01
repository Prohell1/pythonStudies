from turtle import Turtle, Screen, colormode
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rnd_col = (r, g, b)
    return rnd_col


def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)


def draw_dashed_line(turtle):
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_different_shapes(turtle):
    counter = 3
    while counter < 11:
        turtle.color(random_color())
        for _ in range(counter):
            turtle.right(360/counter)
            turtle.forward(100)
        counter += 1


def random_walk(turtle):
    turtle.width(10)
    turtle.speed("fastest")
    turtle.hideturtle()
    for _ in range(200):
        random_dir = random.choice(directions)
        turtle.setheading(random_dir)
        turtle.color(random_color())
        turtle.forward(30)


def draw_spirograph(turtle):
    heading = 0
    turtle.speed("fastest")
    turtle.hideturtle()
    for _ in range(72):
        turtle.setheading(heading)
        turtle.color(random_color())
        turtle.circle(100)
        heading += 5


tim = Turtle()
colormode(255)
tim.shape("turtle")
directions = [0, 90, 180, 270]


# draw_square(tim)
# draw_dashed_line(tim)
# draw_different_shapes(tim)
# random_walk(tim)
# draw_spirograph(tim)

screen = Screen()
screen.exitonclick()
