import random

def rollDice():
    roll = random.randint(1,100)
    return roll

# Now, just to test our dice, let's roll the dice 100 times.

x = 0
while x < 100:
    result = rollDice()
    print(result)
    x+=1

#part 2

# let us go ahead and change this to return a simple win/loss
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        print roll,'roll was 100, you lose. What are the odds?! Play again!'
        return False
    elif roll <= 50:
        print roll,'roll was 1-50, you lose.'
        return False
    elif 100 > roll >= 50:
        print roll,'roll was 51-99, you win! *pretty lights flash* (play more!)'
        return True


'''
Simple bettor, betting the same amount each time.
'''
def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        currentWager += 1
        print 'Funds:', value



simple_bettor(10000,100,100)

#part 3

import random


# let us go ahead and change this to return a simple win/loss
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        #print roll,'roll was 100, you lose. What are the odds?! Play again!'
        return False
    elif roll <= 50:
        #print roll,'roll was 1-50, you lose.'
        return False
    elif 100 > roll >= 50:
        #print roll,'roll was 51-99, you win! *pretty lights flash* (play more!)'
        return True


'''
Simple bettor, betting the same amount each time.
'''
def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        currentWager += 1

    # changed to reduce spam
    if value < 0:
        value = 'Broke!'
    print 'Funds:', value

# lots of wagers now....
x = 0

while x < 100:
    simple_bettor(10000,100,50)
    x += 1

#part 4

import random
import matplotlib
import matplotlib.pyplot as plt

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


'''
Simple bettor, betting the same amount each time.
'''
def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    # wager X
    wX = []

    #value Y
    vY = []

    # change to 1, to avoid confusion so we start @ wager 1
    # instead of wager 0 and end at 100.
    currentWager = 1

    #           change this to, less or equal.
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            # append #
            wX.append(currentWager)
            vY.append(value)

        else:
            value -= wager
            # append #
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1

    #print 'Funds:', value

    plt.plot(wX,vY)



x = 0

# start this off @ 1, then add, and increase 50 to 500, then 1000
while x < 100:
    simple_bettor(10000,100,1000)
    x += 1


plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()

#part 5
