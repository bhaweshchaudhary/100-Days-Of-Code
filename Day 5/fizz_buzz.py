for run in range(1, 101):
    if run%3==0 and run%5==0:
        print("FizzBuzz")
    elif run%3==0:
        print("Fizz")
    elif run%5==0:
        print("Buzz")
    else:
        print(run)