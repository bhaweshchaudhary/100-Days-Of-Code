from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5

# Function to check user guess against actual answer

def check_answer(guess, answer, turns):
    '''checks answer against guess. returns the number of turns remaining.'''
    if guess > answer:
        print("Too high.")
        return turns-1
    elif guess<answer:
        print("Too low")
        return turns-1
    else:
        print(f"You got it, the answer was {answer}")

# Make function to set difficulty

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURN

# Choosing random number between 1 and 100
def game():
    print("Welcome to Number Guessing Game.")
    print("I'm thinking of a Number between 1 and 100.")
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")

# Let the user guess a number
    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong

    guess = 0
    while guess != answer:
        print(f"you have {turns} number of guess left.")
        guess = int(input("Make a Guess.\n"))
        turns=check_answer(guess, answer, turns)
        if turns==0:
            print("You've run out of guesses, You lose.")
            return
        elif guess!=answer:
            print("guess again")


# Track the number of turns and reduce it by 1 if they get it wrong
game()
