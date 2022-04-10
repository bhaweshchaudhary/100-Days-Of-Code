#   operation on Array Data Structure
#   1. Traversal

#   algorithm
#   Step 1: Take user input for the size of the array
#   Step 2: take the content to store in that array from user input
#   step 3: print the content one by one

#   using procedural programming

"""
size = int(input("Enter the size of an array\n"))
content = []
for x in range(size):
    merocontent = input("Enter the content of the array\n")
    content.append(merocontent)
print("------------\n")
for y in content:
    print(y)

"""

#   using object oriented programming

class ProgramOne:
    def __init__(self, size, content, merocontent):
        self.size = size
        self.content = content
