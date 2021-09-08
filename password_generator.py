#!/usr/bin/python3

import string
import random

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

def get_password_length():
    length = input("Enter the password length you want to use: ")
    return int(length)
    
    
    
def password_generator(length=8):
    printable = f'{letters}{digits}{punctuation}'
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password
    
pass_one = password_generator()    
pass_length = get_password_length()
pass_two = password_generator(pass_length)

print("pass_one (" + str(len(pass_one)) + "):\t\t" + pass_one )
print("pass_two (" + str(len(pass_two)) + "):\t\t" + pass_two )