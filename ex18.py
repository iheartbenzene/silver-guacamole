# this one is like the script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#okay, that *args is pointless since we can write
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this takes no arguments
def print_none():
    print("I've nothing to show.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
