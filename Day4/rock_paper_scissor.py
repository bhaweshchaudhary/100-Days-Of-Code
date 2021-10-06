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

user = input("Choose between rock, paper, and scissor\n")

options = [rock, paper, scissors]
computer = random.choice(options)

if (user == rock and computer == scissors):
    print("You've won")
else if (user == scissors and computer == rock):
    print("You loose")
else if (user == rock and computer == paper):
    print("""""""""""""")




print(computer)
# rule: rock wins scissor, scissor wins paper and paper wins rocks