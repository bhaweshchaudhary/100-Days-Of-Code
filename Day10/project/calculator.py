from art import logo

print(logo)

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
    
num1 = int(input("What's the first number? \n"))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above\n")
num2 = int(input("What's the second number?\n"))

# one method

# result = 0
# if operation_symbol == "+":
#     result = add(n1=num1, n2=num2)
# if operation_symbol == "-":
#     result = subtract(n1=num1, n2=num2)
# if operation_symbol == "*":
#     result = multiply(n1=num1, n2=num2)
# if operation_symbol == "/":
#     result = divide(n1=num1, n2=num2)

# another metho

calculation_function = operations[operation_symbol]
result = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")