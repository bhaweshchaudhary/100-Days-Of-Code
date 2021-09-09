print("Welcome to rollercoaster\n")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Please pay $5 only.")
    elif age <= 18:
        bill = 7
        print("Please pay $7 only.")
    elif age >= 47 and age <= 57:
        print("Everything is going to be okay. Have a free ride on us.")
    else:
        bill = 12
        print("Please pay $12 only.")

    wants_photo = input("Do you want to take photos? Y or N\n").upper()
    if wants_photo == "Y":
        bill = bill + 3
    print(f"Your final price is ${bill}\n")
else:
    print("Sorry you have to grow taller before you ride roller coaster.")