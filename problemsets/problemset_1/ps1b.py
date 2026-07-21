## 6.100A PSet 1: Part B
## Name: David Linaria
## Time Spent: 5 mins
## Collaborators: \
from problemsets.problemset_1.ps1_tester import semi_annual_raise

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input('Please put in your yearly salary: '))
portion_saved = float(input('Please put in your portion saved: '))
cost_of_dream_home = float(input('Please put in the price of your dream home: '))
semi_annual_raise = float(input('Please put in the semi annual raise of your salary: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
months = 0
portion_down_payment = 0.25
amount_saved = 0
r = 0.05

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
months = 0

while amount_saved < portion_down_payment * cost_of_dream_home:
    months += 1
    amount_saved += amount_saved * (r / 12) + yearly_salary / 12 * portion_saved
    if months % 6 == 0:
        yearly_salary *= semi_annual_raise + 1
