from sys import argv

script, first, second, third = argv

third = input("How old are you?")

"""
argv needs the same number of variables to be entered
on the command line before the script is run
in order to actually run.

Can possibly be combined with user input for
various effects.

Though it is to be observed that the input function
does not necessarily have to be defined before the
argument is passed to the script.

Since, the computation happens in the order in which
the lines are written.

The passed in variable will now be printed regardless
of what you initially defined as your initial variable
"""
print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


#example of input computation
a = int(third) * 2
#secondary example but with change of base
a = int(third, base=16)
#note that the use of the word "base" is not necessary

print(a)

'''
Perhaps it is therefore then possible to call another
python script in this same manner.

Maybe by pathing to it directly?
'''
