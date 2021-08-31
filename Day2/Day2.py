# Data Types

# String (anything inside double quotation is a string)

a = "123"
b = "345"
c = a + b
print(c)

# integers

d = 123
e = 345
f = d + e
print(f)

# float

g = 3.556
h = 4.335

# Boolean

True
False

# Type error, type checking and type conversion

length = len(input("What is your name?\n"))
# output = "Your name has " + length + "character."
output = type(length) # this will print the data type
print(output)

# Above program will give us type error because we cannot concatenate integer with string.

# type conversion or type casting

new_string_length = str(length)
print("Your name has " + new_string_length + " character.")