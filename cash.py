"""
What is your yearly market value?
What is your venture paying you now?
What do you project your venture will pay? When?
What is your runway?
"""

market_salary  = 2e5
venture_salary = 0
projected_salary = 3.5e5
projected_time = 4 # years
runway = 2 # years

inflation = 0.02

# What can I calculate?
cashNPV = ( projected_salary / ( (1+inflation)**projected_time )) - (market_salary - venture_salary)