# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.shapesize(2)
# timmy.forward(100,)

# my_screen = Screen()
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])


print(table.align)
table.align = "l"
print(table.align)

print(table)