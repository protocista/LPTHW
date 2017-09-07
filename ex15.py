'''
When he talks about a text file he just means use atom and name the file txt
rather then using another system and typing out a text file.
'''
# calling on the system to pull up a file from argv
from sys import argv
#tells us from what script to run and which file in argv
script, filename = argv
# open the mentioned file
txt = open(filename)
# formatted print statment to add pretty to the process
print(f"Here's your file {filename}:")
print(txt.read())
# reads and prints the file we chose
print("Type the filename again:")
file_again = input("> ")
# saving the file in a new varaible and calling upon it again
txt_again = open(file_again)
# prints the file again
print(txt_again.read())

'''
It is less hassle to use the argv to call upon the file then running the program
and then calling upon the file to be open
'''
# cant use pythob to look at files hate this!

txt.close()
txt_again.close()
