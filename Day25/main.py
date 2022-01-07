import pandas

data = pandas.read_csv("2.1 weather_data.csv")
# data_dict = data.to_dict()
# data_list = data["temp"].to_list()
# average_temp = data["temp"].mean()
# max_value = data["temp"].max()
# print(max_value)

# Get row of data with max temperature

print(data[data.temp == data.temp.max()])