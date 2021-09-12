# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

#Write your code below this line


combined_name = name1 + name2

small_name = combined_name.lower()

t = small_name.count("t")
r = small_name.count("r")
u = small_name.count("u")
e = small_name.count("e")

true = t + r + u + e

l = small_name.count("l")
o = small_name.count("o")
v = small_name.count("v")
e = small_name.count("e")

love = l + o + v + e

true_love = int(str(true) + str(love))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}%, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}%, you are alright together.")
else:
    print(f"Your score is {true_love}%.")