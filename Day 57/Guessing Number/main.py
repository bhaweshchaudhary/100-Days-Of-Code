import random

computer_number = random.randint(1, 100)
manual_input = int(input("Enter Number \n"))
switch = True

while(switch):
    if manual_input < computer_number:
        print("You guessed too low")
    elif manual_input > computer_number:
        print("You guessed too high")
    else:
        print("You're correct")
    switch = False