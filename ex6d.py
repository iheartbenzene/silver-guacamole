types_of_people = 10
#string in string 1st instance
x = f"There are {types_of_people} in the."

binary = "binary"
do_not = "don't"

#string in string 2nd instance
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

#string in string 3rd and 4th instances
print(f"I said {x}")
print(f"I also said {y}")

hilarious = False
#bool in string
joke_evaluation = "Isn't that joke so funny?! {}"
#bool in string that looks like string in string
print (joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#concatenation
print(w + e)
