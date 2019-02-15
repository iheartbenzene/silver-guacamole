# TODO edit the range() for floats properly

from datetime import *
import math

income = float(input("What is your average hourly rate? \n"))
salary = income * 2080.00

print(datetime.now())
print("Then your salary is: %0.2f" % salary)

source_2018 = "https://www.irs.com/articles/2018-federal-tax-rates-personal-exemptions-and-standard-deductions"
single_deduction = 12000
married_joint_deduction = 24000
widow = married_joint_deduction
widower = widow
married_separate_deduction = single_deduction
head_of_household = 18000

# information sourced from
# https://www.irs.com/articles/2018-federal-tax-rates-personal-exemptions-and-standard-deductions

if salary in range(0, 9525):
    #first line determines tax bracket
    print("And your effective tax bracket is '10% of taxable income'.")
    #second line determines how much you will pay in taxes annually (approximately)
    print("So you pay around %0.2f in taxes each year." % (salary * 0.10))
    #third line determines net annual pay
    print("And your net annual pay is approximately %0.2f." % (salary * (1-0.1)))
    #fourth line determins monthly net pay
    print("So you have approximately %0.2f each month." % ((salary * (1-0.1) / 12)))
    #note that none of these account for unpaid holidays
elif salary in range(9526, 38700):
    print("And your effective tax bracket is '$952.50 plus 12% of the amount over 9525'.")
    print("So you pay around %0.2f in taxes each year." % (952.50 + salary * 0.12))
    print("And your net annual pay is approximately %0.2f." % (salary - (952.50 + salary * 0.12)))
    print("So you have approximately %0.2f each month." % ((salary - (952.50 + salary * 0.12)) / 12))
    #with a single_deduction standard applied
    print("However, a standard deduction of 'Single' puts you around %0.2f annually and %0.2f monthly instead." % ((salary - (952.50 + (salary - single_deduction) * 0.12)), (salary - (952.50 + (salary - single_deduction) * 0.12)) / 12))
elif salary in range(38701, 82500):
    print("And your effective tax bracket is '$4,453.50 plus 22% of the amount over $38,700'.")
    print("So you pay around %0.2f in taxes each year." % (4453.50 + salary * 0.22))
    print("And your net annual pay is approximately %0.2f." % (salary - (4453.50 + salary * 0.22)))
    print("So you have approximately %0.2f each month." % ((salary - (4453.50 + salary * 0.22)) / 12))
    print("However, a standard deduction of 'Single' puts you around %0.2f annually and %0.2f monthly instead." % ((salary - (4453.50 + (salary - single_deduction) * 0.22)), ((salary - (4453.50 + (salary - single_deduction) * 0.22)) / 12)))
elif salary in range(82501, 157500):
    print("And your effective tax bracket is '$14,089.50 plus 24% of the amount over $82,500'.")
    print("So you pay around %0.2f in taxes each year." % (14089.50 + salary * 0.24))
    print("And your net annual pay is approximately %0.2f." % (salary - (14089.50 + salary * 0.24)))
    print("So you have approximately %0.2f each month." % ((salary - (14089.50 + salary * 0.24)) / 12))
    print("However, a standard deduction of 'Single' puts you around %0.2f annually and %0.2f monthly instead." % ((salary - (14098.50 + (salary - single_deduction) * 0.24)), ((salary - (14098.50 + (salary - single_deduction) * 0.24)) / 12)))
elif salary in range(15701, 200000):
    print("And your effective tax bracket is '$32,089.50 plus 32% of the amount over $157,500'")
    print("So you pay around %0.2f in taxes each year." % (32089.50 + salary * 0.32))
    print("And your net annual pay is approximately %0.2f." % (salary - (32089.50 + salary * 0.32)))
    print("So you have approximately %0.2f each month." % ((salary - (32089.50 + salary * 0.32)) / 12))
    print("However, a standard deduction of 'Single' puts you around %0.2f annually and %0.2f monthly instead." % ((salary - (32089.50 + (salary - single_deduction) * 0.32)), ((salary - (32089.50 + (salary - single_deduction) * 0.32)) / 12)))
elif salary in range(200001, 500000):
    print("And your effective tax bracket is '$45,689.50 plus 35% of the amount over $200,000'.")
    print("So you pay around %0.2f in taxes each year." % (45689.50 + salary * 0.35))
    print("And your net annual pay is approximately %0.2f." % (salary - (45689.50 + salary * 0.35)))
    print("So you have approximately %0.2f each month." % ((salary - (45689.50 + salary * 0.35)) / 12))
    print("However, a standard deduction of 'Single' puts you around %0.2f annually and %0.2f monthly instead." % ((salary - (45689.50 + (salary - single_deduction) * 0.35)), ((salary - (45689.50 + (salary - single_deduction) * 0.35)) / 12)))
else:
    print("And your effective tax bracket is '$150,689.50 plus 37% of the amount over $500,000'.")
    print("So you pay around %0.2f in taxes each year." % (150689.50 + salary * 0.37))
    print("And your net annual pay is approximately %0.2f." % (salary - (150689.50 + salary * 0.37)))
    print("So you have approximately %0.2f each month." % ((salary - (150689.50 + salary * 0.37)) / 12))
    print("However, a standard deduction of 'Single' puts you around %0.2f annually and %0.2f monthly instead." % ((salary - (150689.50 + (salary - single_deduction) * 0.37)), ((salary - (150689.50 + (salary - single_deduction) * 0.37)) / 12)))
