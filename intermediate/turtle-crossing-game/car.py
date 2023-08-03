from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        color = random.choice(COLORS)
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        start_pos = (300, random.randint(-250, 250))
        self.goto(start_pos)

    def move(self, level):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE + (level-1) * -MOVE_INCREMENT
        self.goto(new_x, self.ycor())







