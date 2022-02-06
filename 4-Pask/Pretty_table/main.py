from prettytable import prettytable
import random

x = prettytable()

x.field_names = ["City", "Area", "Population"]
x.add_row(["Adelaide", 1295, 1158259])
x.add_row(["Brisbane", 5906, 458675])
x.add_row(["Darwin", 112, 2156748])
x.add_row(["Hobart", 1357, 654687])
x.add_row(["Sydney", 2058, 54687969])

# print(x)

german_cars = ["BMW", "Audi", "MB", "Porshe", "VW"]
print(random.randint(0, 100))
print(random.randrange(10, 100, 5))

print(random.choice(german_cars))
random.shuffle(german_cars)
print(german_cars)
german_cars.sort()
print(german_cars)