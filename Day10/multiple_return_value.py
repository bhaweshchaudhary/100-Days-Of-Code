def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide the valid input.\n"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(f_name=input("What's your first name?\n"), l_name=input("What's your last name?\n")))