import pandas

reading_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

letter = reading_csv.letter
letter_list = letter.to_list()

code = reading_csv.code
code_list = code.to_list()

mero_dic = {letter_list[i]: code_list[i] for i in range(len(letter_list))}

word = input("Enter a word: ").upper()
try:
    output_list = [mero_dic[letter] for letter in word]
except KeyError:
    print("One Letters are acceptable.")
else:
    print(output_list)
