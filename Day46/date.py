class Date:
    def __init__(self):
        self.year_choice = input("Which year do you want to travel to? Type the date in this format YYYY-"
                                 "MM-DD:\n")
        self.year_array = self.year_choice.split("-")
        self.year = self.year_array[0]
        self.month = self.year_array[1]
        self.day = self.year_array[2]
        print(self.year, self.month, self.day, sep="/")




