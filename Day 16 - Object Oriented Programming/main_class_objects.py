import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("coral")
my_screen = turtle.Screen()
timmy.shapesize(5)
timmy.forward(100)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name",
                 ["Pikachu", "Schiggy", "Glumanda"])
table.add_column("Type",
                 ["Electric", "Water", "Fire"])
table.align["Pokemon Name"] = "l"
table.align["Type"] = "r"
print(table)
