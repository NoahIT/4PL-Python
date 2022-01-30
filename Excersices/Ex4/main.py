from datetime import datetime

my_b_day = datetime(2022, 11, 7)

my_string2 = str(input('Enter Todays date(yyyy-mm-dd): '))
my_date2 = datetime.strptime(my_string2, "%Y-%m-%d")

print(my_b_day - my_date2," Till your birthday")
