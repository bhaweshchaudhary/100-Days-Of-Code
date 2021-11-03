word_list = ["ardvark", "baboon", "camel"]

# 1st - Randomly chose word from word_list and assign it to the variable called chosen_word
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
print(chosen_word)
listing = []
for blank in chosen_word:
    listing += "_"
print(listing)

# 2nd - Ask the user to guess the letter and assign their answer to the variable called guess. Make guess lowercase.
end_of_game = False
while not end_of_game:
    guess = input("Please guess the letter\n").lower()

    # 3rd - Check if the letter the user guessed (guess) is one of the letters in chosen word

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            listing[position] = letter
    print(listing)

    if "_" not in listing:
        end_of_game = True
        print("You win")
