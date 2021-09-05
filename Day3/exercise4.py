print("Welcome to rollercoaster\n")
height = int(input("What is your height in cm?\n"))
if height >= 120:
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Please pay $5 only.")
    elif age <= 18:
        print("Please pay $7 only.")
    else:
        print("Please pay $12 only.")
else:
    print("Sorry you have to grow taller before you ride roller coaster.")