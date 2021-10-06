import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("Choose between rock (press 0), paper (press 1), and scissor(press 2)\n")

computer_choice = random.randint(0,2)

if (user_choice == 0 and computer_choice == 1):
    print("You loose and computer won")

if (user_choice == 1 and computer_choice == 2):
    print("You loose and computer won")

if (user_choice == 2 and computer_choice == 0):
    print("You loose and computer won")

if (user_choice == 1 and computer_choice == 0):
    print("You won and computer loose")

if (user_choice == 2 and computer_choice == 1):
    print("You won and computer loose")

if (user_choice == 0 and computer_choice == 2):
    print("You won and computer loose")

if (user_choice == 0 and computer_choice == 0):
    print("It's a draw")

if (user_choice == 1 and computer_choice == 1):
    print("It's a draw")

if (user_choice == 2 and computer_choice == 2):
    print("It's a draw")