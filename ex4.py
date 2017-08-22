# Changing the variable names, by just making the first comments
# and then jjst making new variables under the first set
# cars = 100.0
# making all the numbers floating point
# space_in_a_car = 4.0
# you make floatung point numbers by adding .0 after your intiger
# drivers = 30.0
# passengers = 90.0
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven

c = 100
# cars
s = 4.0
# space in cars
d = 30
# drivers
p = 90
# passengers
u = c - d
# unused cars
v = d
# cars driven
t = v * s
# carpool capacity
a = p / v
# average passangers per car


print("There are", c, "cars available.")
print("There are only", d, "drivers available.")
print("There will be", u, "empty cars today.")
print("We can transport", t, "people today.")
print("We have", p, "to carpool today.")
print("We need to put about", a, "in each car.")

# watch the video now
