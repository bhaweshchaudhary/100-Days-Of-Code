MAIN = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

ask_user = input("What would you like? (espresso/latte/cappuccino)\n").lower()

# TODO: 2. Check the user’s input to decide what to do next.
price_espresso = MAIN["espresso"]["cost"]
price_latte = MAIN["latte"]["cost"]
price_cappuccino = MAIN["cappuccino"]["cost"]

if ask_user == "espresso":
    print("Please insert coins.\n")
    quarters = int(input("How many quarters?\n"))
    dimes = int(input("How many dimes?\n"))
    nickles = int(input("How many nickles?\n"))
    pennies = int(input("How many pennies?\n"))
    total = (0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)
    if total == price_espresso:
        print("Here is your espresso. Enjoy.")
    elif total > price_espresso:
        change = total - price_espresso
        print(f"Here is your change: {change}\n")
        print("Here is your espresso. Enjoy\n")
    else:
        print(f"You don't have enough coins\nHere is your change: {total}")

if ask_user == "latte":
    print("Please insert coins.\n")
    quarters = int(input("How many quarters?\n"))
    dimes = int(input("How many dimes?\n"))
    nickles = int(input("How many nickles?\n"))
    pennies = int(input("How many pennies?\n"))
    total = (0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)
    if total == price_latte:
        print("Here is your latte. Enjoy.")
    elif total > price_latte:
        change = total - price_latte
        print(f"Here is your change: {change}\n")
        print("Here is your latte. Enjoy\n")
    else:
        print(f"You don't have enough coins\nHere is your change: {total}")

if ask_user == "cappuccino":
    print("Please insert coins.\n")
    quarters = int(input("How many quarters?\n"))
    dimes = int(input("How many dimes?\n"))
    nickles = int(input("How many nickles?\n"))
    pennies = int(input("How many pennies?\n"))
    total = (0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)
    if total == price_cappuccino:
        print("Here is your latte. Enjoy.")
    elif total > price_cappuccino:
        change = total - price_cappuccino
        print(f"Here is your change: {change}\n")
        print("Here is your latte. Enjoy\n")
    else:
        print(f"You don't have enough coins\nHere is your change: {total}")


# TODO: 3. The prompt should show again to serve the next customer.

# TODO 4: Turn off the Coffee Machine by entering ”off" to the prompt.

# TODO 5: Print report.

# TODO 6: Check resources sufficient?

# TODO 7: Process Coins.

# TODO 8: Check transaction successful?

# TODO 9: Make Coffee.
