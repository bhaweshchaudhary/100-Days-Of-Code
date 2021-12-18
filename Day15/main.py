MENU = {
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

profit = 0

def is_resource_sufficient(order_ingredients):
    '''returns true when orders can be made and false if ingeriendients are insufficient'''
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough

def process_coins():
    '''returns the total calculated from the coins inserted'''
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    '''Returns true when payment is accepted and false if money is insufficient.'''   
    if money_received >= drink_cost:
        return True
    else:
        return False 
        print("Sorry that's not enough money, Money refunded.")
        

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}$")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink):
            payment = process_coins()

