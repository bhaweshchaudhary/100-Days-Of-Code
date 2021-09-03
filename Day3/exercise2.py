# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

#Write your code below this line

bmi = int(weight / (height * height))


if bmi < 18.5:
    print(f"your bmi is {bmi} so you're underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"your bmi is {bmi} so you've normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"your bmi is {bmi} so you're slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"your bmi is {bmi} so you're obese.")
elif bmi > 35:
    print(f"your bmi is {bmi}, you're clinically obese.")
else:
    print("I need values.")
