"""
Are you contributing IP you own to the venture?
Will you have rights to IP developed by the venture?
Market value of developed IP? When?
Cost of developing IP separately?
"""

contributing_ip = False
ip_rights = 0.8
ip_market_value = 1e5
ip_time2market = 3
ip_init_cost = 1e6
ip_hump_cost = 2e5

inflation = 0.02

ipNPV = ( ip_market_value / ( (1+inflation)**ip_time2market )) - ip_hump_cost
if not (contributing_ip and ip_rights):
    ipNPV -= ip_init_cost

ipNPV *= ip_rights