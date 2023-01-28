# this is a band name generator. It takes input of which city you were born and what's your pet and and combine then to generate a band name for you.

print("Welcome to band name generator\n")
birth_place = input("Enter the name of city you were born in:\n")
pet_name = input("Enter your pet name:\n")
band_name = birth_place + " " + pet_name
print("Your band name could be " + band_name)