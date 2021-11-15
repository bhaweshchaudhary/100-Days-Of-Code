# # function with output

# def my_function():
#     result = 4*2
#     return result

# my_function()

def format_name(f_name, l_name):
    full_name = f_name + " " + l_name
    title_case_full_name = full_name.title()
    print(title_case_full_name)

format_name(f_name=input("What's your first name?\n"), l_name=input("What's your last name?\n"))