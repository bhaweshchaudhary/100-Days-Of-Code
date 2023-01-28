# args is positional arguments
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(3, 3, 3))

# kwargs is keyword arguments
