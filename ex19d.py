#initial definition of the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a part!")
    print("Get a blanket. \n")

#directly feeding the function numbers
print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

#feeding the function variables instead
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#feeding the function an arithmetic problem instaed
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

#feeding the function variables + arithmetic
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

import math as m
from datetime import *
def maritime(p, q):
    e = m.e
    pi = m.pi
    print(p*e**(q*1j*pi)) #j denotes a complex number
    print("\t", p*e**(pi/100*q), "\n")

maritime(7, 6)
maritime(7-5, abs(-5))
maritime(2, 64-18)
