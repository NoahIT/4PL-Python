german_cars = ["bmw", "audi", "mb", "porshe", "vw"]
japan_cars = ["toyota", "nissan", "mazda", "lexus"]

# print(type(german_cars))
# print(len(german_cars))
# print(german_cars[1])
# print(german_cars[len(german_cars) - 1])
# print(german_cars[-1])
# print(german_cars[-2])

german_cars.append("opel")
german_cars.insert(1, "Smth")
german_cars.extend(japan_cars)

german_cars.remove("toyota")
german_cars.pop(1)
german_cars.pop()

del german_cars[0]
del japan_cars

print(japan_cars)
print(german_cars)
