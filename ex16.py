from sys import argv
# sys is a module it is the system module(one of the core libraries, usually #1)
# its a low level connection to the interptriter in python
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
# the file is able to be written, r = read there are others
print("Trunacating the file. Goodbye!")
target.truncate()
#erasing the test file and allows it to be rewritten
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ", sep='\n', file=sys.stdin)
line2 = sys.stdin.readline()
line3 = input("line 3: ")

print("I'm going to write these to the file.")

'''target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
output = f"""{line1}
{line2}
{line3}
"""
# from sys import stdout
import sys

sys.stdout.write(output)
print('abc',             'def',
                sep='\n', file=sys.stdout)
print(line1, line2, line3, sep='\n', file=target)
# output2 = f"{line1}\n{line2}\n{line3}"
# target.write(output)
# target.write(output2)

#target.write(line1, "\n", line2, "\n", line3, "\n")
#hopeful for SQ3, wrong why is this wrong?
print("And finally, we close it.")
target.close()
