import random

computer_number = random.randint(1, 100)
manual_input = int(input("Enter Number \n"))
switch = True

while(switch):
    manual_input = int(input("Enter Number \n"))
    if (computer_number < manual_input):
        print("You guessed too high.")
    if (computer_number > manual_input):
        print("You guessed too low")
    if (computer_number == manual_input):
        print("You're correct")
    switch = False