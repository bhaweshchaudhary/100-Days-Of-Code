# Don't change the code below
age = input("What is your current age?\n")
# Don't change the code above

#Write your code below this line

age_in_integer = int(age)
years_remaining = 90 - age_in_integer
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365


print(f"you have {years_remaining} years or {months_remaining} months or {weeks_remaining} weeks or {days_remaining} days remaining to live.")