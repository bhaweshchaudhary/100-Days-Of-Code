import random

def play():      
    ccl = ["rock", "paper", "scissor"]

    user_choice = input("'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer_choice = random.choice(ccl)

    # r > s, s > p, p > r
    if user_choice == computer_choice:
        return 'tie\n'
    elif user_choice == 'r' and computer_choice == 's':
        return 'user won\n'
    elif user_choice == 's' and computer_choice == 'p':
        return 'user won'
    elif user_choice == 'p' and computer_choice == 'r':
        return 'user won'
    else:
        return 'nothing'

    print(computer_choice)

game = play()
print(game)