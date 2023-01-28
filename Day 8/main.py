# simple functions
def greeting():
    print("Hello world")

greeting()

# function with inputs
def greet(name): # here name in parenthesis is parameter
    print(f"Hello {name}")

greet("world") # here world is argument


# positional vs key arguments

# functions with more than one inputs
# positional arguments

def greet_with(name, location):
    print(f"Hello {name}\n")
    print(f"What is it like in {location}")

greet_with("world", "vizag") # arguments are positional arguments because it supply the value to the parameters at same location / position and it default.

# keyword arguments

def greet_with(name, location):
    print(f"Hello {name}\n")
    print(f"What is it like in {location}")

greet_with(location="vizag", name="bhawesh") # in keyword arguments we specify which arguments is the value of which parameters.