# FileNotFound Error
# with open("a_file.txt") as file:
#   file.read()

# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existence_key"]

# IndexError
# fruit_list = ["apple", "orange", "pineapple"]
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)

# FileNotFound Error (handling error)
try:
    file = open("a.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    # print("there was an error")
    file = open("a.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exists.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
