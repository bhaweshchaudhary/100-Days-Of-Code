# Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# Don't change the code above 

#Write your code below this line
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 3
if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")


