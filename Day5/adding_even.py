# have to add the all the even numbers together from 1 to 100

# 1st method
num = 0
for even in range(0, 101, 2):
    num += even
print(num)

# 2nd method

num2 = 0
for even2 in range(1, 101):
    if even2%2 == 0:
        num2 += even2
print(num2)