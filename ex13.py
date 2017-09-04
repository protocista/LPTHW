from sys import argv # argv = argument varaible(vector) feature/module
# read the WYSS section for how to run this
script, first, second, third, fourth = argv
# removed third, then added fourth
print(">>>> argv=", repr(argv))
# added from video, repr lets you read the inputs that you assigned, debugging tool
print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)
print("The fourth variable is:", fourth)
count = input("Are there other variables you can think of? ")
print(f"""
The script {script} has multiple variables.
They are called {first}, {second},
{third} and {fourth}.
""")
# study drill 3 and 4
