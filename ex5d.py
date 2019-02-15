name = 'Zed A. Shaw'
age = 35
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

lbs_to_kg = 1 / 2.2046 #(1/2.2046) lbs
in_to_cm = 1 / 2.54 #(1/2.54) inches

height1 = height * in_to_cm
weight1 = weight * lbs_to_kg

print(f"Let's talk about {name}. ")
print(f"He's {height} inches tall. ")
print(f"He's {weight} pounds heavy. ")
print("Actually, that's not too heavy. ")
print(f"He's got {eyes} eyes and {hair} hair. ")
print(f"His teeth are usually {teeth} depending on the coffee. ")

#This line is tricky.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}. ")

print("\n Or")

#Going to make use of the round() function so we don't have a million sig figs.
#Which rounds "x" to a precision of "n" digits in the form round(x, n)

print(f"\n Let's talk about {name}. ")
print(f"He's {round(height1, 3)} inches tall. ")
print(f"He's {round(weight1, 3)} pounds heavy. ")
print("Actually, that's not too heavy. ")
print(f"He's got {eyes} eyes and {hair} hair. ")
print(f"His teeth are usually {teeth} depending on the coffee. ")

#This line is very tricky.
total = age + height1 + weight1
print(f"If I add {age}, {round(height1, 3)}, and {round(weight1, 3)}, I get {round(total, 3)}. ")
