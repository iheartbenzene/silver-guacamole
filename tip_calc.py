import math


print("What is your total?")
total = float(input('> '))
tip = total * 0.15
if 0 < tip < 3:
    print("Ya cheap bastard.")
else:
    print('Hello, your total was %0.2f and your tip is %0.2f' %(total, tip))
