#int
cars = 100
#float
space_in_car = 4.0
#int
drivers = 30
#int
passengers = 90
#int
cars_not_driven = cars - drivers
#int
cars_driven = drivers
#int * float = float
carpool_capacity = cars_driven * space_in_car
#int / int = float
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
