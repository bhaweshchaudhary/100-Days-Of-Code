# Roller Coster Ride Eligibility test
print("Welcome to Roller Coster Ride Eligibility test\n")

height = input("What is your height in cm?\n")
height_int = int(height)

if height_int>=120:
    print("You're eligible to ride roller coster.")
else:
    print("Sorry, see you again.")

# eligibility test according to weight.
print("\nWelcome to eligibility test according to weight.\n")

weight = input("What's your weight?\n")
weight_int = int(weight)

if weight_int == 75:
    print("Congratulation\n")
else:
    print("Try again.")

# Welcome to food taste calculator
print("\nWelcome to food taste calculator\n")
food_name = input("Which food you've tried at our mall?\n")
taste_scale = input(f"On the scale of 1 to 10, what is the number that suit the taste of {food_name}\n")
taste_scale_int = int(taste_scale)

if taste_scale_int == 10:
    print(f"Awesome, We're happy you liked {food_name}")
elif taste_scale_int <= 5 & taste_scale_int > 0:
    print(f"Sorry to hear that, We'll try to improve the taste of {food_name}")
elif taste_scale_int >= 6:
    print(f"That's awesome and we promise to increase the quality and taste of {food_name} even better.")
else:
    print(f"We need more detail to calculate the taste of {food_name}")
