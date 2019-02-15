import math
import numpy
import matplotlib

#add asset allocation
#add net worth
#add budget
#add FIRE
#add mortgage calculator

#net worth
asset = []
debt = [] #add a recurring line for the input

print("What is the value of your home?")
home_value = float(input("> "))
house_amnt = round(home_value, 2)

print("Do you still have a mortgage? If so, how much do you owe?")
print("If not, enter '0' for the amount.")
mortgage = float(input("> "))
mort_amnt = round(mortgage, 2)

asset.append(house_amnt)
debt.append(mort_amnt)

net_worth = float(sum(asset) - sum(debt))
net_worth = round(net_worth, 2)

print(f"So far, your net worth is {net_worth}. ")

#asset allocation

#as a summary percentage of total account value
print("What is the total account value?")
account_value = float(input("> "))
account_value = round(account_value, 2)

print("How much in stocks, or equity?")
equity = float(input("> "))
equity = equity / account_value
equity = round(equity, 2)

print("How much in bonds, or fixed income?")
fixed_income = float(input("> "))
fixed_income = fixed_income / account_value
fixed_income = round(fixed_income, 2)

print("Approximately how much in cash?")
cash = float(input("> "))
cash = cash / account_value
cash = round(cash, 2)

#print asset allocation in a pie chart

asset.append(account_value)
net_worth = float(sum(asset) - sum(debt))
net_worth = round(net_worth, 2)
print(f"So far, your net worth is {net_worth}. ")

print("Anything owed on your credit cards?")
credit_card = input("> ")
if "yes" or "Yes" or "Y" in credit_card:
    print("Approximately how much?")
    credit_card = float(input("> "))
    credit_card = round(credit_card, 2)
    debt.append(credit_card)
    net_worth = float(sum(asset) - sum(debt))
    net_worth = round(net_worth, 2)
    print(f"So far, your net worth is {net_worth}. ")
    print("Let's move on.")
else:
    print("Okay, let's move on.")

print("What about any loans?")
