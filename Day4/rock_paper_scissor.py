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

game_images = [rock, paper, scissors]

# if (int(user_choice) < 0 or int(user_choice) >= 3):

try:

    user_choice = int(input("Choose between rock (press 0), paper (press 1), and scissor(press 2)\n"))
    # print("You chose:\n")
    print(f"You chose \n {game_images[int(user_choice)]}")

    computer_choice = random.randint(0,2)
    print(f"Computer chose \n {game_images[computer_choice]}")
except:
    print("Please enter a valid number.")


if (user_choice == 0 and computer_choice == 1):
    print("You loose")

if (user_choice == 1 and computer_choice == 2):
    print("You loose")

if (user_choice == 2 and computer_choice == 0):
    print("You loose")

if (user_choice == 1 and computer_choice == 0):
    print("You won")

if (user_choice == 2 and computer_choice == 1):
    print("You won")

if (user_choice == 0 and computer_choice == 2):
    print("You won")

if (user_choice == 0 and computer_choice == 0):
    print("It's a draw")

if (user_choice == 1 and computer_choice == 1):
    print("It's a draw")

if (user_choice == 2 and computer_choice == 2):
    print("It's a draw")