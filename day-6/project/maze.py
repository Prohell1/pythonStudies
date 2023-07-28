# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear() and not at_goal():
        turn_right()
        while front_is_clear():
            move()
            if right_is_clear():
                turn_right()
                move()
                break
    elif front_is_clear() and not at_goal():
        while front_is_clear():
            move()
            if right_is_clear():
                turn_right()
                move()
                break
    else:
        turn_left()
        while front_is_clear():
            move()
            if right_is_clear() and not at_goal():
                turn_right()
                move()
                break
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
