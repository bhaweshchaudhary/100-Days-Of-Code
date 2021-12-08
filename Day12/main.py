# Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function {enemies}.")

increase_enemies()
print(f"enemies outside function {enemies}.")

# Local scope
def hello():
    world = 1
    print(world)
hello()

# Global scope

hello_world = 4
def hellow():
    print(hello_world)
hellow()
print(hello_world)

# 2nd video: does python have block scope