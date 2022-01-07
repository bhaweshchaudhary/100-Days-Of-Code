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

data_dict = {
    "Students": ["Bhawesh", "Sujan", "Gato"],
    "Marks": [99, 86, 98]
}

data = pandas.DataFrame(data_dict)
print(data)