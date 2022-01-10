import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
reading_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

letter = reading_csv.letter
letter_list = letter.to_list()

code = reading_csv.code
code_list = code.to_list()
