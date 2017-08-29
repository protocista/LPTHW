# more formating and printing
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
# what would happen if I change the order?
print(formatter.format(3, 1, 2, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
