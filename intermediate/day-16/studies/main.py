# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('DarkGreen')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Eevee", "Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon", "Leafeon", "Glaceon", "Sylveon"])
table.add_column("Pokemon Type", ["Normal", "Water", "Electric", "Fire", "Psychic", "Dark", "Grass", "Ice", "Fairy"])
table.add_column("Have Plushy", ["No", "No", "No", "No", "No", "No", "No", "No", "No"])

table.align = "l"


print(table)
input("Press enter to exit!")
