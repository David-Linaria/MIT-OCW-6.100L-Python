def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
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
	return months