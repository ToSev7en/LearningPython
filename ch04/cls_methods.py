class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    # instance method
    def tomorrow(self):
        self.day = self.day + 1


if __name__ == "__main__":
   today =  Date(2018, 11, 21)
   print(today)
   today.tomorrow()
   print(today)