import turtle
from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    tim.right(10)


def turn_counter_clockwise():
    tim.left(10)


def clear_screen():
    turtle.resetscreen()


tim = Turtle()
screen = Screen()
screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_clockwise, "d")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(clear_screen, "c")

screen.exitonclick()
