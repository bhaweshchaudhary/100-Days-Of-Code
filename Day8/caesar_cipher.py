alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(mero_text, shift_amount, cipher_direction):
    khali_string = ""
    if cipher_direction == "encode":
        for letter in mero_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            khali_string += alphabet[new_position]
        print(f"The encoded text is {khali_string}")
    elif cipher_direction == "decode":
        for letter in mero_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            khali_string += alphabet[new_position]
        print(f"The decoded text is {khali_string}")

caesar(mero_text=text, shift_amount=shift, cipher_direction=direction)