students_height = input("Input a list of students height ").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])

# formula: sum of total height divided by number of height mentioned

average_height = sum(students_height)/len(students_height)

print(average_height)