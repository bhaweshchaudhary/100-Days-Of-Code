import pandas

# data = pandas.read_csv("2.1 weather_data.csv")
# data_dict = data.to_dict()
# data_list = data["temp"].to_list()
# average_temp = data["temp"].mean()
# max_value = data["temp"].max()
# print(max_value)

# Get row of data with max temperature

# max_temp_row = data[data.temp == data.temp.max()]

# getting monday temperature in fahrenheit

# getting hold of monday row

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_in_celsius = (monday_temp*1.8) + 32

# Create a dataframe from the scratch.
#
# data_dict = {
#     "Students": ["Bhawesh", "Sujan", "Gato"],
#     "Marks": [99, 86, 98]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
total_gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
total_cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
total_black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(total_gray_squirrel)
print(total_cinnamon_squirrel)
print(total_black_squirrel)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Total Count": [total_gray_squirrel, total_cinnamon_squirrel, total_black_squirrel],
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")
print(data_frame)