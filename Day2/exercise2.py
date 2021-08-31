# BMI Calculator exercise

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


new_height = float(height)
new_height_in_square = new_height**2
new_weight = int(weight)

bmi = int(new_weight/new_height_in_square)
print(bmi)