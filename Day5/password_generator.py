#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Py Password Generator!")
try:
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))


    #Eazy Level - Order not randomised:
    new_pass = ""

    for letter in range(1, nr_letters + 1):
        new_pass += random.choice(letters)

    for symbol in range(1, nr_symbols + 1):
        new_pass += random.choice(symbols)

    for number in range(1, nr_numbers + 1):
        new_pass += random.choice(numbers)

    print(f"The easy password is {new_pass}\n")


    #Hard Level - Order of characters randomised:

    new_password = []

    for letter in range(1, nr_letters + 1):
        new_password.append(random.choice(letters))

    for symbol in range(1, nr_symbols + 1):
        new_password += random.choice(symbols)

    for number in range(1, nr_numbers + 1):
        new_password += random.choice(numbers)

    # print(new_password)
    # random.shuffle(new_password)
    # print(new_password)

    latest = ""
    for i in new_password:
        latest += i
    print(f"The hard version is {latest}")

except:
    print("Something wrong happened try again")