the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#The first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}.")

for fruit in fruits:
    print(f"A fruit of type: {fruit}.")

#for-loops can parse mixed lists too
for i in change:
    print("I've got {i}.")

#we can also build lists.
elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was {i}.")
