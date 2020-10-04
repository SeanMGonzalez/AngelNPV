import numpy as np
"""
What is your yearly market value?
What is your venture paying you now?
What do you project your venture will pay? When?
What is your ccfg.runway?
"""

def calcCashNPV( ccfg):
    
    # ccfg.market_salary  = 2e5,
    # ccfg.venture_salary = 0,
    # ccfg.projected_salary = 3.5e5,
    # ccfg.projected_time = 4, # years
    # ccfg.runway = 2*12 # years

    inflation = 0.02

    time_steps = np.array(range(12,ccfg.projected_time+1,12))
    stay_salary = np.interp( time_steps, [0,ccfg.projected_time], [ccfg.venture_salary,ccfg.projected_venture_salary])

    cashNPVstay = np.sum(( stay_salary / ( (1+inflation)**(time_steps/12) )) - (ccfg.market_salary - stay_salary))

    # cashNPVstay = ( ccfg.projected_venture_salary / ( (1+inflation)**(ccfg.projected_time/12) )) - (ccfg.market_salary - ccfg.venture_salary)

    cashNPVplay = np.sum( ccfg.market_salary / ( (1+inflation)**(time_steps/12) )) # - stay_salary)

    return cashNPVstay, cashNPVplay