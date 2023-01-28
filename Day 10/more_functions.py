# # function with output

# def my_function():
#     result = 4*2
#     return result

# my_function()

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(f_name=input("What's your first name?\n"), l_name=input("What's your last name?\n")))