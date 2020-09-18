"""
What percentage of the venture will you own?
What is your vesting schedule?
What is the market valuation of the venture?
What valuation do you project? When?
"""

your_percentage = 0.2 # 20% percent
your_schedule = 3 # years
market_value = 7e6 # dollars
your_valuation = 50e6 # dollars
time2valuation = 5 # years

inflation = 0.02

equityNPV = your_percentage * ( your_valuation / ( (1+inflation)**time2valuation ))
