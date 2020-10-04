"""
What percentage of the venture DO you own?
What percentage of the venture WILL you own?
How many years to complete vesting?
What is the market valuation of the venture?
What valuation would you give the venture if you stay? if you leave? By when?
"""

def calcEquityNPV( ecfg):
    """
    ecfg.your_percentage  = 0.05,
    ecfg.pot_percentage   = 0.2,
    ecfg.your_schedule    = 3,
    ecfg.your_valuation   = 1e8,
    ecfg.likely_market_valuation = 5e7,
    ecfg.time2valuation   = 5
    """
    inflation = 0.02

    equityNPVstay = ecfg.pot_percentage * ( ecfg.your_valuation / ( (1+inflation)**(ecfg.time2your_valuation/12) ))

    # equityNPVreleased = (ecfg.pot_percentage - ecfg.your_percentage) * (ecfg.likely_market_valuation / ( (1+inflation)**(ecfg.time2market_valuation/12)))

    equityNPVplay = ecfg.your_percentage * ( ecfg.likely_market_valuation / ( (1+inflation)**(ecfg.time2market_valuation/12) )) #- equityNPVreleased

    return equityNPVstay, equityNPVplay