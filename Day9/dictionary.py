programming_dictionary = {
    "Bug": "An error in program that prevents the program to run as expected.",
    "Function": "A block of code that can be used to run over and over again.",
    "Loop": "The action of doing something over and over again."
}

# retrieving item from dictionary
# print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Python"] = "Python is a cool programming language."

# print(programming_dictionary)

# create an empty dictionary

empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "This makes program vulnerable."
# print(programming_dictionary["Bug"])

# Loop through dictionary
for thing in programming_dictionary:
    print(thing)