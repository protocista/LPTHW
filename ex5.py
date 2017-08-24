# Study drills, rename all the variables so they do not have my_ in them
# my_name = 'Lydia D. Tomeo'
# my_age = 28 # not a lie
# my_height = 65 #inches
# my_weight = 155 # lbs
# my_eyes = 'Brown'
# my_teeth = 'White'
# my_hair = 'Blue' # yes it is blue

# new vaiables being used.
title = 'Lydia D. Tomeo'
shelflife = 28
dimension = 65  # in inches
mass = 155  # in lbs
optics = 'Brown'
enamel = 'White'
pigment = 'Blue'
lb_to_kg = 0.453592
in_to_cm = 2.54
mass_in_kg = mass * lb_to_kg
dimension_in_cm = dimension * in_to_cm

# how the heak do I even use the math function!

# What does the f mean? why is it there?
print(f"Let's talk about {title}.")
# short andlight, and using the female term of adress
print(f"She's {dimension_in_cm} centimeters short.")
# making some of my own modifications to the code
print(f"She's {mass_in_kg} kilo grams light.")
print("Actually thats very heavy.")
print(f"She's got {optics} eyes and {pigment} hair.")
print(f"Her teeth are usually {enamel} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = shelflife + dimension_in_cm + mass_in_kg
print(f"If I add {shelflife}, {dimension_in_cm}, and {mass_in_kg} I get {total}.")
