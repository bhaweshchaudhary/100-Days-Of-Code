with open("file1.txt", mode="r") as file_1:
    file_1_list = file_1.readlines()
with open("file2.txt", mode="r") as file_2:
    file_2_list = file_2.readlines()

result = [int(num) for num in file_1_list if num in file_2_list]

# Write your code above 👆

print(result)

