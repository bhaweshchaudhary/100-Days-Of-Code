print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_or_right = input("Your Ex is on right and your crush is on left, where'd you want to go?\n").lower()

if left_or_right == "right":
    print("Shit man not again, the game is over.")
elif left_or_right == "left":
    swim_or_wait = input("There's a river infront of you, do you want to swim or you want to wait?\n").lower()
    if swim_or_wait == "swim":
        print("Attacked by trout, you game is now over.")
    elif swim_or_wait == "wait":
        door = input("Which is your favorite door, Red or Blue or Yellow?\n").lower()
        if door == "red":
            print("You've been burned by a fire, you game is over now.")
        elif door == "blue":
            print("Eaten by beasts. Game over.")
        elif door == "yellow":
            print("You win!")
        else:
            print("Your game is over.")
    else:
        print("Attacked by trout, you game is now over.")
else:
    print("Your game is over.")