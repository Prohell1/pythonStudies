from turtle import Screen
from player_turtle import PlayerTurtle
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = PlayerTurtle()
cars = []
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")
screen.listen()

counter = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if counter == 6:
        new_car = Car()
        cars.append(new_car)
        counter = 1
    else:
        counter += 1
    for car in cars:
        car.move(scoreboard.level)
        # Detect collision
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # check if player reached the end
    if player.ycor() >= 270:
        scoreboard.increase_level()
        player.reset_pos()
    screen.update()


screen.exitonclick()
