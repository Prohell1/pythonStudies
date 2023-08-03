from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class PlayerTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.reset_pos()

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() >= 280:
            self.reset_pos()

    def reset_pos(self):
        self.goto(STARTING_POSITION)
