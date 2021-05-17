# from turtle import Turtle, Screen
#
# timmy = Turtle()
# # print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan3")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.sortby = "Type"

print(table)