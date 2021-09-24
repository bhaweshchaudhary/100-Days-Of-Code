import random
import my_module

random_numbers = random.randint(100, 200)

pi = my_module.pi

# this random() generates number between 0.0 to 1.0 but not including 1.0 for eg. it can go like 0.9999 but not 1.0
random_float = random.random()

# multiply random function with integers
# we get floating numbers from 0.0 to 5.0 but not including 5.0
new_random = random_float * 5
print(new_random)

# understanding the offset and appending item to the list 4-4

language = [
    "python", "c", "javascript"
]
language.append(".net") # add item to the end of the list
language.extend(["reactjs", "angularjs", "django"]) # add this new list to the existing list
print(language)