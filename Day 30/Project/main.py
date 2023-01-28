import pandas

reading_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

letter = reading_csv.letter
letter_list = letter.to_list()

code = reading_csv.code
code_list = code.to_list()

mero_dic = {letter_list[i]: code_list[i] for i in range(len(letter_list))}
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [mero_dic[letter] for letter in word]
    except KeyError:
        print("Only Letters in the alphabets are acceptable.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()