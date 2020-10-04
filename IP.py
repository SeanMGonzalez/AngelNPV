"""
Are you contributing IP you own to the venture?
Will you have rights to IP developed by the venture?
Market value of developed IP? When?
Cost of developing IP separately?
"""

def calcIPNPV( ipcfg):

    # Expected config variables
    # ipcfg.contributing_ip = False,
    # ipcfg.ip_rights = 0.8,
    # ipcfg.ip_market_value = 1e5,
    # ipcfg.ip_time2market = 3*12,
    # ipcfg.ip_init_cost = 1e6,
    # ipcfg.ip_hump_cost = 2e5
    
    inflation = 0.02 # https://www.statbureau.org/en/inflation-api
    
    ipNPVplay = ( ipcfg.ip_market_value / ( (1+inflation)**(ipcfg.ip_time2market/12) )) - ipcfg.ip_hump_cost
    if not ipcfg.contributing_ip and ipcfg.ip_rights==0:
        ipNPVplay -= ipcfg.ip_init_cost
    
    ipNPVplay *= ipcfg.ip_rights
    
    ipNPVstay = 0 # You are already benefiting from the IP with equity in the company.

    return ipNPVstay, ipNPVplay