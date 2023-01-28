weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {
    temperature: value * 9/5+32 for (temperature, value) in weather_c.items()
}

print(weather_f)
