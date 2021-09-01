#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number.

print("Welcome to tip calculator\n")
total_bill = input("Enter total amount of bill\n$")
total_bill_integer = int(total_bill)
tip = input("Enter tip percentage\n")
tip_integer = int(tip)
final_bill_after_tip = (tip_integer/100) * total_bill_integer + total_bill_integer
final_bill_after_tip_float = float(final_bill_after_tip)
number_of_people = input("Enter the number of people to split the bill equally\n")
number_of_people_int = int(number_of_people)
final_amount = final_bill_after_tip_float / number_of_people_int
final_amount_float = float(final_amount)
amount_to_be_paid = "{:.2f}".format(final_amount_float)
print(f"Each person should pay ${amount_to_be_paid}")
# (tip/100 * total bill ) + total bill / total number of people