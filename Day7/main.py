word_list = ["ardvark", "baboon", "camel"]

# 1st - Randomly chose word from word_list and assign it to the variable called chosen_word
import random
chosen_word = random.choice(word_list)
print(chosen_word)

# 2nd - Ask the user to guess the letter and assign their answer to the variable called guess. Make guess lowercase.

guess = input("Please guess the letter\n").lower()

# 3rd - Check if the letter the user guessed (guess) is one of the letters in chosen word

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")

# 6. challenge 2 solution -  how to replace the blank