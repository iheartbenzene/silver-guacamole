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

print('''
FUNCTION CHECKLIST

    1. Does your function start with "def"
    2. Does your function name have only characters and _
        characters?
    3. Is there an open parenthesis right after the function
        name?
    4. Did you put your argumennt after the parenthesis
        separated by commas?
    5. Did you make each argument unique?
    6. Did put a close parenthesis and a colon after
        the arguments?
    7. Did you indent all lines of code that should be
        inside the function by four spaces?
    8. Did you "end" your function by going back to writing
        with no indent? Also known as "dedenting"?

When you run ("use" or "call") a function, check these things:
    1. Did you call/use/run this function by typing its name?
    2. Did you put the ( chacater after the name to run it?
    3. Did you put the values you want into the parenthesis separated by
        a comma?
    4. Did you end the function call with a ) character?
''')
