from datetime import datetime

my_string1 = str(input('Enter date(yyyy-mm-dd): '))
my_date1 = datetime.strptime(my_string1, "%Y-%m-%d")

my_string2 = str(input('Enter date(yyyy-mm-dd): '))
my_date2 = datetime.strptime(my_string2, "%Y-%m-%d")

print(my_date1 - my_date2)
