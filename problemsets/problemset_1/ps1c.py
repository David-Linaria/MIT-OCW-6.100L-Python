## 6.100A PSet 1: Part C
## Name: David Linaria
## Time Spent: 40 mins
## Collaborators: \

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('Please enter your initial deposit: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_house = 800000
down_payment_percentage = 0.25
months = 36
low = 0
high = 1
r = 1
amount_saved = initial_deposit * (1 + r / 12) ** months
steps = 0
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

if initial_deposit >= cost_of_house * down_payment_percentage - 100:
    r = 0.0
elif amount_saved < cost_of_house * down_payment_percentage:
        r = None
else:
    r = (low + high) / 2
    steps += 1
    while abs(cost_of_house * down_payment_percentage - amount_saved) > 100:
        if amount_saved > cost_of_house * down_payment_percentage:
            high = r
        else:
            low = r
        r = (low + high) / 2
        amount_saved = initial_deposit * (1 + r / 12) ** months
        steps += 1