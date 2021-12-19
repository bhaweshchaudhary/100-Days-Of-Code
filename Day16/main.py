# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

main = PrettyTable()
main.field_names = ["S.N", "Student Names", "Phone Numbers"]
main.add_rows(
    [
        ["1", "Bhawesh Chaudhary", "8374734258"],
        ["2", "Shiwani Sharma", "9839384011"]
    ]
)

print(main)