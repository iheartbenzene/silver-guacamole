from sys import argv

script, filename = argv

#opens the file.
#If the file isn't a part of the parent directory,
#Then you'll have to path to the file manually
#even on the command line
txt = open(filename)

#Displays the file
print(f"Here is your file {filename}:")
print(txt.read())

#Even here, need to path to the file
print("Type the filename again: ")
file_again = input("> ")

#this time the path is written as user input
txt_again = open(file_again)

print(txt_again.read())
