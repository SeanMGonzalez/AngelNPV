"""
Is the venture giving you creative freedom?
Could you get the same freedom elsewhere?
How long before you could be in the same creative position again?
What odds, what probability, would you place on successful use of a working thoery?
How much venture cash, equity, IP, would you be willing to bet on that success?
"""

creative_freedom = True
freedom_elsewhere = False
opportunity_time  = 2 # years
opportunity_odds = 0.5 # percent
opportunity_bet = 0.2 # percent

inflation = 0.02

creativeNPV = ( (cashNPV+ipNPV+equityNPV) / ( (1+inflation)**opportunity_time ))
